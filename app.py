import asyncio
import re
from datetime import datetime

import pandas as pd
from fastapi import FastAPI, UploadFile,File, Depends,Form
from fastapi.middleware.cors import CORSMiddleware
from starlette.datastructures import FormData

from backend.Const.Prompt import Prompt
from backend.connector.AzureAISearchConnector import SEARCH_FROM_AZURE
from backend.llm.DefaultLLM import default_chat
from backend.llm.agent.extractQuestion import ExtractQuestion
from backend.models.DatabaseConnector import DBConnector, ExtendedDBConnector
from backend.connector.getEngine import checkConnection, getEngine
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from backend.llm.chatWithSQL import getSQL
from backend.connector.excutorQuery import execute_query
from backend.llm.Response import DefaultLLMResponse
from backend.models.Result import Result
from io import StringIO, BytesIO

# 创建 FastAPI 应用
app = FastAPI()
websocket_router = APIRouter()
# CORS 配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有方法
    allow_headers=["*"],   # 允许所有请求头
)
def clean_table_name(filename: str) -> str:
    # 去掉文件扩展名并替换不合法字符
    table_name = filename.split('.')[0]  # 去掉扩展名
    table_name = re.sub(r'\W+', '_', table_name)  # 替换非字母数字字符为下划线
    now = datetime.now()
    # 格式化时间为字符串
    timestamp_str = now.strftime('%Y-%m-%d%H%M%S')
    return table_name+timestamp_str
@app.post("/checkDB")
async def checkDB(payload: DBConnector):
    return checkConnection(payload)


@app.websocket("/chatWithSQL")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        data = await websocket.receive_json()
        dbConnectorPayload = DBConnector(**data['dbConnector'])
        extractedList = ExtractQuestion(userQuery=data['userQuery'], dbconnector=dbConnectorPayload)
        knowledgeBaseChunk=[]
        if data['AiSearch']:
            for e in extractedList:
                knowledgeBaseChunk = knowledgeBaseChunk + SEARCH_FROM_AZURE(e)
        sql_array = await getSQL(userQuery=data['userQuery'],dbconnector=dbConnectorPayload,ws=websocket,extractedList=extractedList)
        payloads = []
        for sql in sql_array:
            tmpResult = execute_query(query=sql,dbConnector=dbConnectorPayload)
            await websocket.send_json(tmpResult.model_dump_json())
            payloads.append(tmpResult.payload)
        finalPrompt = Prompt.FinalPrompt(AiSearch=data['AiSearch'],SearchInKB=str(knowledgeBaseChunk),SearchInDataBase=str(payloads))
        stream = await default_chat(user_query=data['userQuery'],prompt=finalPrompt)
        await websocket.send_json(Result(status=1,message='开始生成最终回答',payload='').model_dump_json())
        await DefaultLLMResponse(ws=websocket,stream=stream,message="最终回答")
        await websocket.close()
    except WebSocketDisconnect:
        print("Connection Closed")

@app.post("/uploadTable")
async def uploadTable(payload:ExtendedDBConnector=Form(...)):
    df = None
    try:
        contents = await payload.file.read()
        if payload.file.filename.endswith('csv'):
            df = pd.read_csv(StringIO(contents.decode('utf-8')))
        else:
            df = pd.read_excel(BytesIO(contents))
        table_name = clean_table_name(filename=payload.file.filename)
        engine = getEngine(payload)
        print(df.head())
        try:
            for col in df.select_dtypes(include=['object']).columns:
                df[col] = df[col].str.encode('utf-8').str.decode('utf-8')
            df.to_sql(table_name.lower(), engine, index=False, if_exists='replace')
        except Exception as e:
            print(e)
            return Result(status=0,message='建表失败',payload=None)
    except Exception as e:
        return Result(status=0,message=str(e),payload=None)
    return Result(status=1,message='成功',payload=None)
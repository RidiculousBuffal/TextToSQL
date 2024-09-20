import asyncio

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.llm.DefaultLLM import default_chat
from backend.models.DatabaseConnector import DBConnector
from backend.connector.getEngine import checkConnection
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from backend.llm.chatWithSQL import getSQL
from backend.connector.excutorQuery import execute_query
from backend.llm.Response import DefaultLLMResponse
from backend.models.Result import Result

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

@app.post("/checkDB")
async def checkDB(payload: DBConnector):
    return checkConnection(payload)

@app.websocket("/chatWithSQL")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        data = await websocket.receive_json()
        print(data)
        sql_array = await getSQL(userQuery=data['userQuery'],dataBaseName=data['databaseName'],ws=websocket)
        payloads = []
        for sql in sql_array:
            tmpResult = execute_query(query=sql,database=data['databaseName'])
            await websocket.send_json(tmpResult.model_dump_json())
            payloads.append(tmpResult.payload)
        stream = await default_chat(user_query=data['userQuery'],prompt=f"根据数据库查询内容回答问题:{str(payloads)}")
        await websocket.send_json(Result(status=1,message='开始生成最终回答',payload='').model_dump_json())
        await DefaultLLMResponse(ws=websocket,stream=stream,message="最终回答")
        await websocket.close()
    except WebSocketDisconnect:
        print("Connection Closed")
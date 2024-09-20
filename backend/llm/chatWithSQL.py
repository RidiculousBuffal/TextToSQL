from starlette.websockets import WebSocket

from backend.llm.Response import DefaultLLMResponse
from backend.llm.agent.extractQuestion import ExtractQuestion
from backend.llm.agent.getSqlSentence import getSQLSentence
from backend.models.Result import Result


async def getSQL(userQuery: str, dataBaseName: str, ws: WebSocket):
    # 分解问题
    extractedList = ExtractQuestion(userQuery=userQuery, dataBaseName=dataBaseName)
    await ws.send_json(Result(status="1", message="转化问题", payload=f"{extractedList}").model_dump_json())
    res = []
    for q in extractedList:
        await ws.send_json(Result(status="1", message="自然语言转化", payload=f"{q} ").model_dump_json())
        stream = await getSQLSentence(userQuery=q, dataBaseName=dataBaseName)
        str_ = await DefaultLLMResponse(ws=ws,message="解析到SQL语句", stream=stream)
        res.append(str_)
    return res

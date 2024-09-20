from openai.types.chat import ChatCompletion
from starlette.websockets import WebSocket

from backend.models.Result import Result


async def DefaultLLMResponse(ws: WebSocket, stream: ChatCompletion,message:str="发送字符串成功"):
    _str = ''
    for chunk in stream:

        if chunk.choices[0].delta.content is not None:
            content =  chunk.choices[0].delta.content
            _str = _str + content
            await ws.send_json(Result(status="1", message=message, payload=content).model_dump_json())
    return _str

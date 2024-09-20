from typing import Optional
from typing import Any
from pydantic import BaseModel
class Result(BaseModel):
    status:str|int
    message:Optional[str]=None
    payload:Optional[Any]=None
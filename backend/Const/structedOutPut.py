from pydantic import BaseModel

class ExtractQuery(BaseModel):
    result:list[str]
from typing import Optional

from pydantic import BaseModel


class DBConnector(BaseModel):
    DB_URL:str
    DB_USERNAME:str
    DB_PASSWORD:str
    DB_PORT:str
    DB_NAME:Optional[str]=None
from typing import Optional

from fastapi import UploadFile,File
from pydantic import BaseModel


class DBConnector(BaseModel):
    DB_URL:str
    DB_USERNAME:str
    DB_PASSWORD:str
    DB_PORT:str
    DB_NAME:Optional[str]=None
class ExtendedDBConnector(DBConnector):
    file: Optional[UploadFile] =None  # 添加 file 字段
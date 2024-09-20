import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from backend.models.DatabaseConnector import DBConnector
from backend.models.Result import Result

# 加载 .env 文件
load_dotenv()
# 从环境变量中获取数据库连接信息
username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')


def getEngine(dataBase: str):
    # 创建数据库引擎
    engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@{host}:{port}/{dataBase}')
    return engine


def checkConnection(payload: DBConnector):
    # 自定义数据库引擎
    engine = create_engine(
        f'mysql+mysqlconnector://{payload.DB_USERNAME}:{payload.DB_PASSWORD}@{payload.DB_URL}:{payload.DB_PORT}/')
    try:
        # 创建一个连接
        with engine.connect() as connection:
            # 执行获取所有数据库的查询
            result = connection.execute(text("SHOW DATABASES;"))

            # 提取数据库名称
            databases = [row[0] for row in result]

        result_instance = Result(status="1", message="操作成功",payload=databases)
        return result_instance
    except Exception as e:
        result_instance = Result(status="0", message="链接失败了!")
        return result_instance

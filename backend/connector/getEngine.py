from sqlalchemy import create_engine, text, Engine

from backend.models.DatabaseConnector import DBConnector
from backend.models.Result import Result


def create_database_if_not_exists(engine: Engine, db_name: str):
    """创建数据库（如果不存在），并指定字符集和排序规则"""
    with engine.connect() as connection:
        # 使用 `CREATE DATABASE` 语句创建数据库，并指定字符集和排序规则
        connection.execute(text(f"""
            CREATE DATABASE IF NOT EXISTS `{db_name}` 
            CHARACTER SET utf8mb4 
            COLLATE utf8mb4_general_ci
        """))


def getEngine(payload: DBConnector):
    temp_engine = create_engine(
        f'mysql+mysqlconnector://{payload.DB_USERNAME}:{payload.DB_PASSWORD}@{payload.DB_URL}:{payload.DB_PORT}/')
    create_database_if_not_exists(temp_engine, payload.DB_NAME)
    engine = create_engine(
        f'mysql+pymysql://{payload.DB_USERNAME}:{payload.DB_PASSWORD}@{payload.DB_URL}:{payload.DB_PORT}/{payload.DB_NAME}?charset=utf8mb4')
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

        result_instance = Result(status="1", message="操作成功", payload=databases)
        return result_instance
    except Exception as e:
        result_instance = Result(status="0", message="链接失败了!")
        return result_instance

from ast import literal_eval

from starlette.websockets import WebSocket

from backend.connector.getEngine import getEngine
from backend.models.DatabaseConnector import DBConnector
from backend.models.Result import Result
from sqlalchemy import text
def execute_query(query: str, dbConnector: DBConnector) -> Result:
    # 获取数据库引擎
    engine = getEngine(dbConnector)

    # 使用数据库引擎执行查询
    with engine.connect() as connection:
        result = connection.execute(text(query))
        rows = result.fetchall()
        result = []
        for row in rows:
            result.append(dict(row._mapping))
        return Result(status=1,message="SQL查询结果",payload=result)

if __name__ == '__main__':
   res =  execute_query("select * from company","jbs_company_test")
   print(res.model_dump_json())

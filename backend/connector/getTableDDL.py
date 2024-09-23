from sqlalchemy import inspect, text
from backend.connector.getEngine import getEngine
from backend.models.DatabaseConnector import DBConnector


def get_table_ddl(connection, table_name):
    inspector = inspect(connection)
    columns = inspector.get_columns(table_name)
    primary_keys = inspector.get_pk_constraint(table_name)
    foreign_keys = inspector.get_foreign_keys(table_name)
    # 构建 DDL 语句
    ddl = f"CREATE TABLE `{table_name}` (\n"

    column_defs = []
    for column in columns:
        column_def = f"    `{column['name']}` {column['type']}"

        # 添加注释
        if 'comment' in column:
            column_def += f" COMMENT '{column['comment']}'"

        column_defs.append(column_def)

    # 添加主键
    if primary_keys['constrained_columns']:
        column_defs.append(f"    PRIMARY KEY (`{', '.join(primary_keys['constrained_columns'])}`)")

    # 添加外键
    for fk in foreign_keys:
        fk_column = fk['constrained_columns'][0]
        ref_table = fk['referred_table']
        ref_column = fk['referred_columns'][0]
        ddl += f"    FOREIGN KEY (`{fk_column}`) REFERENCES `{ref_table}` (`{ref_column}`) ON DELETE CASCADE ON UPDATE CASCADE"

    ddl += ",\n".join(column_defs) + "\n) DEFAULT CHARSET=utf8 ENGINE=INNODB;"
    return ddl


def getTableDDLAsString(dbConnector:DBConnector):
    res = ''
    engine = getEngine(dbConnector)
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SHOW TABLES;"))
            for row in result:
                table_name = row[0]
                ddl = get_table_ddl(connection, table_name)
                res = res + "DDL for table" + table_name + ":\n" + ddl + "\n"
    except Exception as e:
        print("Error connecting to the database:", e)
    return res
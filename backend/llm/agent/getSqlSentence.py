from backend.llm.getLLM import getLLM
from backend.Const.Prompt import Prompt
from backend.connector.getTableDDL import getTableDDLAsString
async def getSQLSentence(userQuery: str, dataBaseName: str):
    DDL = getTableDDLAsString(dataBaseName)
    client = getLLM()
    stream = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[{
            'role': 'system',
            'content': Prompt.SQL_prompt
        }, {
            'role': 'user',
            'content': DDL,
        },
        {
             'role': 'user',
             'content': f'Query:{userQuery}'
        }
        ],
        stream=True
    )
    return stream
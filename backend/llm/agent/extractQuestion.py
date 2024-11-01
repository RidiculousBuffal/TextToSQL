from backend.connector.getTableDDL import getTableDDLAsString
from backend.llm.getLLM import getLLM
from backend.Const.structedOutPut import ExtractQuery
from backend.Const.Prompt import Prompt
from backend.models.DatabaseConnector import DBConnector


def ExtractQuestion(userQuery: str, dbconnector:DBConnector):
    DDL = getTableDDLAsString(dbconnector)
    client = getLLM()
    resp = client.beta.chat.completions.parse(
        model='gpt-4o-2024-08-06',
        messages=[{
            'role': 'system',
            'content': Prompt.Extract_Prompt,
        }, {
            'role': 'user',
            'content': DDL,
        },
            {
                'role': 'user',
                'content': f'Query:{userQuery}'
            }
        ],
        response_format=ExtractQuery
    )
    return resp.choices[0].message.parsed.result

if __name__ == '__main__':
    res = ExtractQuestion(userQuery="Tech Innovators 公司拥有的员工,拥有的项目",dataBaseName="jbs_company_test")
    print(res)
    # ''
    # result = ['Tech Innovators公司的员工', 'Tech Innovators公司拥有的项目']
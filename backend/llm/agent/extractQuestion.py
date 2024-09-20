from backend.connector.getTableDDL import getTableDDLAsString
from backend.llm.getLLM import getLLM
from backend.Const.structedOutPut import ExtractQuery
from backend.Const.Prompt import Prompt

def ExtractQuestion(userQuery: str, dataBaseName: str):
    DDL = getTableDDLAsString(dataBaseName)
    client = getLLM()
    resp = client.beta.chat.completions.parse(
        model='gpt-4o-mini',
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
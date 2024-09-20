from backend.llm.getLLM import getLLM

async def default_chat(prompt: str, user_query: str):
    client = getLLM()
    stream = client.chat.completions.create(
        model='gpt-4o-mini',
        stream=True,
        messages=[
            {
                'role': 'system',
                'content': prompt
            },
            {
                'role': 'user',
                'content': user_query
            }
        ]
    )
    return stream

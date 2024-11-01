import os
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
def SEARCH_FROM_AZURE(query):
    # [START semantic_ranking]

    service_endpoint = os.getenv("SERVICE_ENDPOINT")
    index_name = os.getenv("INDEX_NAME")
    key = os.getenv("KEY")
    credential = AzureKeyCredential(key)
    client = SearchClient(endpoint=service_endpoint, index_name=index_name, credential=credential)
    results = list(
        client.search(
            search_text=query,
            query_type="semantic",
            semantic_configuration_name="default",
            query_language="zh-cn",
            top=10
        )
    )
    ls = []
    for result in results:
        ls.append( result['content'])
    return ls

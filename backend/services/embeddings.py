from openai import AzureOpenAI
from services import embeddings_endpoint, embeddings_key, embeddings_api_version, embeddings_model

embeddings_client = AzureOpenAI(
    api_key=embeddings_key,
    azure_endpoint=embeddings_endpoint,
    api_version=embeddings_api_version
    )
def embed(input):
    response = embeddings_client.embeddings.create(
    input=input,
    model=embeddings_model
    )
    return response
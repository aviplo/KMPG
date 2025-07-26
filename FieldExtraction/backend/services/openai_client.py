from openai import AzureOpenAI
from services import chat_endpoint, chat_key, chat_deployment, chat_api_version

client = AzureOpenAI(
    azure_endpoint=chat_endpoint,
    api_key=chat_key,
    api_version=chat_api_version,
)

def chat(messages):
    print("Sending messages to OpenAI API")
    response = client.chat.completions.create(
        model=chat_deployment,
        messages=messages,
    )
    return response.choices[0].message.content

def prepare_messages(user_input, system_prompt):
    return [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": user_input
        }
    ]
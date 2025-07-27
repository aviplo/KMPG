from openai import AsyncAzureOpenAI
from services import chat_endpoint, chat_key, chat_deployment, chat_api_version

client = AsyncAzureOpenAI(
    azure_endpoint=chat_endpoint,
    api_key=chat_key,
    api_version=chat_api_version,
)

async def chat(messages):
    try:
        print("Sending messages to OpenAI API")
        response = await client.chat.completions.create(
            model=chat_deployment,
            messages=messages,
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error in OpenAI API call: {e}")
        raise e

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
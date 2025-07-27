from openai import AsyncAzureOpenAI
from services import chat_endpoint, chat_key, chat_deployment, chat_api_version
from utils.logging import setup_logging

logger = setup_logging()

client = AsyncAzureOpenAI(
    azure_endpoint=chat_endpoint,
    api_key=chat_key,
    api_version=chat_api_version,
)

async def chat(messages):
    try:
        logger.info(f"Sending messages to OpenAI: {messages}")
        response = await client.chat.completions.create(
            model=chat_deployment,
            messages=messages,
        )
        return response.choices[0].message.content
    except Exception as e:
        logger.error(f"Error in chat(): {e}")
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
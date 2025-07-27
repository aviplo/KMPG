import json
from utils.logging import setup_logging
from services.openai_client import chat

logger = setup_logging()

async def safe_json_with_retries(messages, max_retries=5):
    for attempt in range(max_retries):
        try:
            response_content = await chat(messages)
            return json.loads(response_content)
        except json.JSONDecodeError as e:
            messages.append({"role": "system", "content": "MAKE SURE To RESPOND IN JSON FORMAT"})
            logger.error(f"[Attempt {attempt + 1}] Failed to parse JSON: {e}")
            logger.debug(f"Response content: {response_content}")
            if attempt == max_retries - 1:
                raise ValueError("Failed to parse JSON after retries.")
        except Exception as e:
            logger.error(f"[Attempt {attempt + 1}] Unexpected error from chat(): {e}")
            if attempt == max_retries - 1:
                raise
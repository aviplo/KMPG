from fastapi import APIRouter, HTTPException
from classes.chat_request import ChatRequest
from services.openai_client import chat, prepare_messages
from prompts.user_info import system_prompt_info_collection
import json
from utils.logging import setup_logging

logger = setup_logging()

router = APIRouter()

async def safe_json_with_retries(messages, max_retries=5):
    for attempt in range(max_retries):
        try:
            messages.append({"role": "system", "content": "MAKE SURE To RESPOND IN JSON FORMAT"})
            response_content = await chat(messages)
            return json.loads(response_content)
        except json.JSONDecodeError as e:
            logger.error(f"[Attempt {attempt + 1}] Failed to parse JSON: {e}")
            logger.debug(f"Response content: {response_content}")
            if attempt == max_retries - 1:
                raise ValueError("Failed to parse JSON after retries.")
        except Exception as e:
            logger.error(f"[Attempt {attempt + 1}] Unexpected error from chat(): {e}")
            if attempt == max_retries - 1:
                raise

@router.post("/collect_info")
async def user_info_endpoint(request: ChatRequest) -> dict:   
    try:
        logger.info(json.dumps({"Received user collection message:": request.message}, ensure_ascii=False))
        messages = prepare_messages(request.message, system_prompt_info_collection)
        
        messages.extend(request.history)
        messages.append({"role": "user", "content": request.message})
        try:
            result = await safe_json_with_retries(messages)
            return result
        except ValueError:
            return {
                "answer": "Please try again or rephrase your question.",
                "user_info": request.user_info or {},
                "status": "error"
                }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    
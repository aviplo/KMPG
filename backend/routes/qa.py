from fastapi import APIRouter, HTTPException
import json
from services.openai_client import prepare_messages, chat
from prompts.qa import system_prompt_qa
from classes.chat_request import ChatRequest
from utils.logging import setup_logging
from helpers.json_format_checker import safe_json_with_retries

logger = setup_logging()

router = APIRouter()

@router.post("/qa")
async def qa_endpoint(request: ChatRequest) -> dict:
    try:
        logger.info(json.dumps({"Received QA message:": request.message}, ensure_ascii=False))
        messages = prepare_messages(request.message, system_prompt_qa)
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
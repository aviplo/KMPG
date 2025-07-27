from services.openai_client import chat, prepare_messages
from prompts.user_info import system_prompt_info_collection
import json
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

class UserInfoRequest(BaseModel):
    prompt: str
    message: str
    history: list = []
    user_info: dict = {}


router = APIRouter()

@router.post("/collect_info")
async def user_info_endpoint(request: UserInfoRequest) -> dict:
    try:
        messages = prepare_messages(request.message, system_prompt_info_collection)
        print(f"Received user info request: {json.dumps(request.dict(), ensure_ascii=False, indent=2)}")
        for msg in request.history:
            messages.append(msg)
        
        messages.append({"role": "user", "content": request.message})
        
        response_content = await chat(messages)
        print(f"Response from OpenAI: {response_content}")
        try:
            result = json.loads(response_content)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON response: {e}")
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
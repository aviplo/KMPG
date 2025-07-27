from fastapi import APIRouter, HTTPException
import json
from services.openai_client import prepare_messages, chat
from prompts.qa import system_prompt_qa
from classes.chat_request import ChatRequest

router = APIRouter()

@router.post("/qa")
async def qa_endpoint(request: ChatRequest) -> dict:
    max_retries = 5
    try:
        print(f"Received question: {json.dumps(request.dict(), ensure_ascii=False, indent=2)}")
        messages = prepare_messages(request.message, system_prompt_qa)
        for msg in request.history:
            messages.append(msg)
        
        messages.append({"role": "user", "content": request.message})
        
        for attempt in range(max_retries):
            try:
                response_content = await chat(messages)
                print(f"Response from OpenAI (attempt {attempt + 1}): {response_content}")
                result = json.loads(response_content)
                print(f"Successfully parsed JSON on attempt {attempt + 1}")
                return result
                
            except json.JSONDecodeError as e:
                print(f"JSON parsing failed on attempt {attempt + 1}: {e}")
                print(f"Raw response: {response_content}")
                
                if attempt < max_retries - 1:
                    print(f"Retrying... (attempt {attempt + 2}/{max_retries})")
                    continue
                else:
                    print("Failed to parse JSON, returning fallback response")
                    return {
                        "answer": "I apologize, but I'm having trouble processing your request right now. Please try again or rephrase your question.",
                        "user_info": request.user_info if hasattr(request, 'user_info') else {},
                        "status": "error"
                    }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

import requests
from services.config import BACKEND_URL
from prompts.info_collet import build_info_collection_prompt
from prompts.qa import user_prompt_qa
from helpers.validation import validate_user_info

def chatbot_fn(message, history, user_info=None, phase="info_collection"):
    if not message:
        return history or [], user_info or {}, phase
    
    if history is None:
        history = []
    if user_info is None:
        user_info = {}
    
    if phase == "info_collection":
        endpoint = f"{BACKEND_URL}/collect_info"
        prompt = build_info_collection_prompt(user_info)
    else:
        endpoint = f"{BACKEND_URL}/qa"
        prompt = user_prompt_qa(user_info)

    payload = {
        "prompt": prompt,
        "message": message,
        "history": history,
        "user_info": user_info,
    }
    
    try:
        response = requests.post(
            endpoint,
            json=payload,
            timeout=30
        )
        response.raise_for_status()
        response_data = response.json()
        answer = response_data.get("answer", "No answer found.")
        if phase == "info_collection":
            if "user_info" in response_data:
                extracted_data = response_data["user_info"]
                user_info.update(extracted_data)
            
            status = response_data.get("status", "")
            if status == "complete":
                is_valid, _ = validate_user_info(user_info)
                if is_valid:
                    phase = "qa"
                    print(f"Phase transition to QA. Final user_info: {user_info}")
        
    except requests.RequestException as e:
        answer = f"Error communicating with backend: {str(e)}"
    except Exception as e:
        answer = f"Unexpected error: {str(e)}"

    updated_history = history.copy()
    updated_history.append({"role": "user", "content": message})
    updated_history.append({"role": "assistant", "content": answer})

    return updated_history, user_info, phase
from pydantic import BaseModel

class ChatRequest(BaseModel):
    prompt: str
    message: str
    history: list = []
    user_info: dict = {}
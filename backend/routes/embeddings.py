from services.embeddings import embed
from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.post("/embed")
async def embed_endpoint(text: str) -> list[float]:
    return embed(text)

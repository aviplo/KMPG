from fastapi import FastAPI
from routes.ocr import router as ocr_router
from routes.qa import router as qa_router
from routes.info_collection import router as info_collection
from routes.embeddings import router as embed_router

app = FastAPI()

app.include_router(ocr_router, prefix="/upload_files")
app.include_router(qa_router)
app.include_router(info_collection)
app.include_router(embed_router, prefix="/embed")

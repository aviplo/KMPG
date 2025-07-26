from fastapi import FastAPI
from routers.ocr import extract_files_to_json
from routers.qa import qa_endpoint
from routers.embeddings import embed_endpoint

app= FastAPI()

app.route("/upload_files", methods=["POST"])(extract_files_to_json)
app.route("/qa", methods=["POST"])(qa_endpoint)
app.route("/embed", methods=["POST"])(embed_endpoint)
    
    

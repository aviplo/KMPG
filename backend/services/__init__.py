import os
import json

from dotenv import load_dotenv

load_dotenv()

ocr_endpoint = os.getenv("AZURE_OCR_ENDPOINT")
ocr_key = os.getenv("AZURE_OCR_API_KEY")
chat_endpoint = os.getenv("AZURE_CHAT_ENDPOINT")
chat_key = os.getenv("AZURE_CHAT_KEY")
embeddings_endpoint = os.getenv("AZURE_EMBEDDINGS_ENDPOINT")
embeddings_key = os.getenv("AZURE_EMBEDDINGS_KEY")
embeddings_api_version = os.getenv("AZURE_EMBEDDINGS_API_VERSION", "2023-05-15")
chat_deployment = os.getenv("AZURE_CHAT_DEPLOYMENT", "gpt-4o")
chat_api_version = os.getenv("AZURE_CHAT_API_VERSION", "2025-01-01-preview")
embeddings_model = os.getenv("AZURE_EMBEDDINGS_MODEL", "text-embedding-ada-002")
ocr_model = os.getenv("AZURE_OCR_MODEL", "prebuilt-layout") #prebuilt-document
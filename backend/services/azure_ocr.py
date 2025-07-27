from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential

from classes.languages import Language
from services import ocr_endpoint, ocr_key, ocr_model
from services.openai_client import chat, prepare_messages
from prompts.insurance import user_prompt, system_prompt
from prompts.schemas import hebrew_schema, english_schema
from helpers.detect_language import detect_primary_language
from services.validation import parse_and_validate_response

client = DocumentAnalysisClient(endpoint=ocr_endpoint, credential=AzureKeyCredential(ocr_key))


def extract_text_from_pdf(file_obj):
    print("Extracting text from PDF using Azure OCR")
    poller = client.begin_analyze_document(ocr_model, document=file_obj)
    result = poller.result()
    return result.pages

async def get_json_structured_ocr(ocr_input):
    language = detect_primary_language(ocr_input[0].lines)
    schema_to_use = hebrew_schema if language.value == Language.HEBREW.value else english_schema
    print("Detected primary language:", language.value)
    user_input = user_prompt(schema_to_use, ocr_input)
    messages = prepare_messages(user_input, system_prompt)
    response = await chat(messages)
    return parse_and_validate_response(response, schema_to_use)
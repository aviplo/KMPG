from fastapi import APIRouter, File, UploadFile, HTTPException
from services.azure_ocr import extract_text_from_pdf, get_json_structured_ocr
from utils.logging import setup_logging

logger = setup_logging()

router = APIRouter()

@router.post("/")
async def extract_files_to_json(files: list[UploadFile] = File(...)):
    try:
        logger.info(f"Starting OCR processing for {len(files)} file(s)")
        results = []
        for i, file in enumerate(files):
            logger.info(f"Processing file {i+1}/{len(files)}: {file.filename}")
            contents = await file.read()
            logger.info(f"File {file.filename} read successfully, size: {len(contents)} bytes")
            result = extract_text_from_pdf(contents)
            logger.info(f"Text extraction completed for {file.filename}")
            structured_result = await get_json_structured_ocr(result)
            results.append(structured_result)
            logger.info(f"JSON structuring completed for {file.filename}")
        
        logger.info(f"OCR processing completed successfully for all {len(files)} file(s)")
        return results
    except ValueError as ve:
        logger.error(f"ValueError in OCR processing: {ve}")
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        logger.error(f"Unexpected error in OCR processing: {e}")
        raise HTTPException(status_code=500, detail=str(e))

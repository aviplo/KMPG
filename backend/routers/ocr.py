from fastapi import APIRouter, File, UploadFile, HTTPException

from services.azure_ocr import extract_text_from_pdf, get_json_structured_ocr

router = APIRouter()

@router.post("/upload_files")
async def extract_files_to_json(files: list[UploadFile] = File(...)):
    try:
        results = []
        for file in files:
            contents = await file.read()
            result = await extract_text_from_pdf(contents)
            results.append(get_json_structured_ocr(result))
        return results
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

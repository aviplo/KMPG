import requests
from services.config import BACKEND_URL


def extract_fields(files):
    if files is None:
        return {}

    if isinstance(files, str):
        files = [files]

    upload_files = []
    file_handles = []
    for f in files:
        fh = open(f, "rb")
        file_handles.append(fh)
        upload_files.append(("files", (f, fh, "application/pdf")))

    try:
        response = requests.post(f"{BACKEND_URL}/upload_files", files=upload_files)
        return response.json()
    except Exception as e:
        return {"error": str(e)}
    finally:
        for fh in file_handles:
            fh.close()

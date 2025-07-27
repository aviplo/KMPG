import json

with open("config.json") as f:
    config = json.load(f)

BACKEND_URL = config.get("backend_url", "http://localhost:8000")
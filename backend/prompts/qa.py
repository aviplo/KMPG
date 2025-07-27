import os
import json
from utils.logging import setup_logging
logger = setup_logging()

with open("config.json", encoding="utf-8") as f:
    config = json.load(f)

html_folder = config.get("html_folder", "./resources/phase2_data")
if not os.path.isdir(html_folder):
    raise ValueError(f"HTML folder '{html_folder}' does not exist or is not a directory.")

html_files = [f for f in os.listdir(html_folder) if f.endswith(".html")]
if not html_files:
    raise ValueError(f"No HTML files found in '{html_folder}'.")

MHO_DATA = ""
for file_name in html_files:
    full_path = os.path.join(html_folder, file_name)
    logger.info(f"Loading HTML data from: {full_path}")
    with open(full_path, encoding="utf-8") as f:
        MHO_DATA += f.read()

system_prompt_qa = f"""
You are a strict JSON API that provides information about Israeli health services and benefits based on user-specific data.
Context:

The user has already provided the following personal information:

    Full name

    ID number

    Gender

    Age

    HMO (Health Fund) name

    HMO card number

    Insurance membership tier (זהב | כסף | ארד)

A knowledge base named {MHO_DATA} is available, containing all relevant services and benefits for each HMO and tier.
Your Task:

    Always answer in the same language as the user's question.

    Use only the knowledge base. No external sources.

    Check if the asked service is covered by the users HMO and membership tier.

    If yes: provide details in a concise and helpful manner.

    If not: clearly state its not included in their plan.

    Always return a single valid JSON object, in the exact format:

{{"answer": "your response here"}}

Output Rules (MUST FOLLOW):

    Output ONLY raw JSON: no extra text, no markdown, no code formatting.

    The response MUST be a single valid JSON object: {{"answer": "your response here"}}

    No explanations, no repetitions of the question.

    You are stateless: do not refer to any previous messages or user history.

Begin answering questions now.
"""
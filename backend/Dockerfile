FROM python:3.11-slim

WORKDIR /app

# Set environment variables for Azure services (with default dummy values)
ENV AZURE_OCR_ENDPOINT=${AZURE_OCR_ENDPOINT:-"https://dummy.cognitiveservices.azure.com/"} \
    AZURE_OCR_API_KEY=${AZURE_OCR_API_KEY:-"dummy_key"} \
    AZURE_CHAT_ENDPOINT=${AZURE_CHAT_ENDPOINT:-"https://dummy.openai.azure.com/"} \
    AZURE_CHAT_KEY=${AZURE_CHAT_KEY:-"dummy_key"} \
    AZURE_EMBEDDINGS_ENDPOINT=${AZURE_EMBEDDINGS_ENDPOINT:-"https://dummy.openai.azure.com/"} \
    AZURE_EMBEDDINGS_KEY=${AZURE_EMBEDDINGS_KEY:-"dummy_key"} \
    AZURE_EMBEDDINGS_API_VERSION=${AZURE_EMBEDDINGS_API_VERSION:-"2023-05-15"} \
    AZURE_CHAT_DEPLOYMENT=${AZURE_CHAT_DEPLOYMENT:-"gpt-4o"} \
    AZURE_CHAT_API_VERSION=${AZURE_CHAT_API_VERSION:-"2025-01-01-preview"} \
    AZURE_EMBEDDINGS_MODEL=${AZURE_EMBEDDINGS_MODEL:-"text-embedding-ada-002"} \
    AZURE_OCR_MODEL=${AZURE_OCR_MODEL:-"prebuilt-layout"}

RUN apt-get update

RUN apt-get install -y ca-certificates curl

RUN apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --trusted-host pypi.org \
    --trusted-host pypi.python.org \
    --trusted-host files.pythonhosted.org --upgrade pip

COPY requirements.txt .
RUN pip install --no-cache-dir --trusted-host pypi.org \
    --trusted-host pypi.python.org \
    --trusted-host files.pythonhosted.org -r requirements.txt

COPY . .

RUN mkdir -p logs

EXPOSE 8000

CMD ["python3", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
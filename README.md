# GenAI Medical Services Chatbot

## Project Overview

This project is a medical services chatbot that combines OCR field extraction from PDFs with an intelligent conversational interface. The system has two main phases:

1. **Phase 1**: OCR and field extraction from medical documents
2. **Phase 2**: Conversational chatbot for medical services information

## Project Structure

```
projects/
│
├── backend/
│   ├── main.py                  # FastAPI app entry point
│   ├── config.json              # Configuration file
│   ├── requirements.txt         # Backend dependencies
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── ocr.py              # OCR & field extraction endpoints
│   │   ├── info_collection.py  # User info collection endpoints
│   │   ├── qa.py               # Q&A chatbot endpoints
│   │   ├── embeddings.py       # Vector embeddings endpoints
│   ├── services/
│   │   ├── __init__.py
│   │   ├── azure_ocr.py        # Azure Document Intelligence integration
│   │   ├── openai_client.py    # Azure OpenAI integration
│   │   ├── embeddings.py       # Vector embeddings service
│   │   ├── validation.py       # Data validation utilities
│   ├── prompts/
│   │   ├── insurance.py        # Insurance-related prompts
│   │   ├── qa.py               # Q&A prompts
│   │   ├── schemas.py          # Data schemas
│   │   ├── user_info.py        # User info collection prompts
│   ├── classes/
│   │   ├── chat_request.py     # Chat request data models
│   │   ├── languages.py        # Language detection utilities
│   ├── helpers/
│   │   ├── __init__.py
│   │   ├── detect_language.py  # Language detection helper
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── logging.py          # Logging setup/utilities
│   │   ├── error_handling.py   # Error handling utilities
│   ├── resources/
│   │   ├── phase1_data/        # PDF documents for OCR
│   │   ├── phase2_data/        # HTML knowledge base files
│   ├── logs/
│   │   ├── app.log             # Application logs
│
├── frontend/
│   ├── app.py                  # Gradio UI entry point
│   ├── config.json             # Frontend configuration
│   ├── requirements.txt        # Frontend dependencies
│   ├── services/
│   │   ├── __init__.py
│   │   ├── chatbot.py          # Chatbot service logic
│   │   ├── config.py           # Configuration management
│   │   ├── file_upload.py      # File upload handling
│   ├── prompts/
│   │   ├── info_collet.py      # Info collection prompts
│   │   ├── qa.py               # Q&A prompts
│   ├── helpers/
│   │   ├── __init__.py
│   │   ├── validation.py       # Validation helpers
│
├── README.md                   # This file
```

## Setup Instructions

### Prerequisites
- Python 3.11 or higher
- Azure Document Intelligence API key
- Azure OpenAI API key

### 1. Clone and Setup Environment
```bash
git clone https://github.com/aviplo/KMPG.git
```

### 2. Backend Setup
```bash
cd backend
pip install -r requirements.txt
```

### 3. Frontend Setup
```bash
cd ../frontend
pip install -r requirements.txt
```

### 4. Configuration
Configure your Azure credentials in the respective `config.json` files in both backend and frontend directories.

## Running the Application

### Start the Backend Server
```bash
cd backend
python3 -m uvicorn main:app --reload
```
The backend API will be available at `http://localhost:8000`

### Start the Frontend Application
```bash
cd frontend
python3 app.py
```
The frontend interface will be available at `http://localhost:7860`

## Features

### Phase 1: OCR Field Extraction
- Upload PDF documents for text extraction
- Automatic language detection (Hebrew/English)
- Structured field extraction using AI
- JSON output with extracted fields

### Phase 2: Medical Services Chatbot
- Interactive conversational interface
- User information collection
- Medical services Q&A
- Context-aware responses
- Multilingual support

## API Endpoints

### Backend Endpoints
- `POST /upload_files/` - Upload and process PDF files
- `POST /collect_info` - Collect user information
- `POST /qa` - Question and answer interactions
- `POST /embed/` - Generate embeddings

## Technology Stack

- **Backend**: FastAPI, Azure Document Intelligence, Azure OpenAI
- **Frontend**: Gradio
- **Language Support**: Hebrew, English
- **File Processing**: PDF OCR and text extraction
- **AI**: GPT models for conversation and field extraction

## Logging

Application logs are stored in:
- Backend: `backend/logs/app.log`
- Frontend: Console output

## Development

The application supports hot reload for development:
- Backend uses `--reload` flag with uvicorn
- Frontend can be restarted as needed

## Notes

- All conversation state is managed on the frontend
- The system supports both Hebrew and English languages
- OCR processing includes automatic language detection
- Vector embeddings are used for knowledge base queries 
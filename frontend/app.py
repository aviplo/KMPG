import gradio as gr
import requests
import io
import json

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
        response = requests.post("http://localhost:8000/upload_files", files=upload_files)
        return response.json()
    except Exception as e:
        return {"error": str(e)}
    finally:
        for fh in file_handles:
            fh.close()

def chatbot_fn(message, history):
    # TODO: Call backend API for chatbot response
    return "Chatbot response will appear here.", history + [[message, "Chatbot response will appear here."]]

with gr.Blocks() as layout:
    gr.Markdown("# GenAI Field Extraction")
    with gr.Tab("Field Extraction"):
        file_input = gr.File(label="Upload PDF", file_types=[".pdf"], file_count="multiple")
        json_output = gr.JSON(label="Extracted Fields")
        file_input.change(extract_fields, inputs=file_input, outputs=json_output)
    with gr.Tab("Phase 2: Medical Chatbot"):
        chatbot = gr.Chatbot(type="messages")
        msg = gr.Textbox(label="Prompt")
        msg.submit(chatbot_fn, inputs=[msg, chatbot], outputs=[chatbot, chatbot])

layout.launch()

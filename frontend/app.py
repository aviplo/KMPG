import gradio as gr
from services.file_upload import extract_fields
from services.chatbot import chatbot_fn

def handle_chat_message(message, history, user_info, phase):
    """
    Handle chat message and manage state in the frontend
    """
    updated_history, updated_user_info, updated_phase = chatbot_fn(
        message, history, user_info, phase
    )
    return updated_history, "", updated_user_info, updated_phase

with gr.Blocks() as layout:
    gr.Markdown("# GenAI Field Extraction")
    with gr.Tab("Field Extraction"):
        file_input = gr.File(label="Upload PDF", file_types=[".pdf"], file_count="multiple")
        json_output = gr.JSON(label="Extracted Fields")
        file_input.change(extract_fields, inputs=file_input, outputs=json_output)
    
    with gr.Tab("Medical Chatbot"):
        user_info_state = gr.State({})
        phase_state = gr.State("info_collection")
        
        gr.Markdown("## Medical Services Chatbot")
        gr.Markdown("I'll help you with information about medical services. First, I need to collect some information about you.")
        
        chatbot = gr.Chatbot(type="messages", label="Chat")
        msg = gr.Textbox(label="Type your message here...", placeholder="Hello, I need information about medical services")
        
        clear_btn = gr.Button("Start New Conversation")
        
        msg.submit(
            handle_chat_message, 
            inputs=[msg, chatbot, user_info_state, phase_state], 
            outputs=[chatbot, msg, user_info_state, phase_state]
        )
        
        def clear_conversation():
            return [], {}, "info_collection"
        
        clear_btn.click(
            clear_conversation,
            outputs=[chatbot, user_info_state, phase_state]
        )

layout.launch()

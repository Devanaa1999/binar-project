import re
import gradio as gr

def data_processing (text):
    text = text.lower ()
    text = re.sub(r"[^a-zA-Z0-9]", "", text)
    return text.split () [0]

gradio_ui = gr.Interface(
    fn=data_processing,
    title="Data Processing and Modeling",
    description="Aplikasi Web Data Processing dan Modeling", 
    inputs=gr.Textbox(lines=10, label="Paste some text here"),
    outputs=[
        gr.Textbox(label="Result"),
    ]
)

if __name__ == "__main__":
    gradio_ui. launch()
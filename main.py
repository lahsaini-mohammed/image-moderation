from dotenv import load_dotenv
import gradio as gr
from modules.utils import process_image

# Load environment variables
load_dotenv()

def launch():
    with gr.Blocks(theme=gr.themes.Default(primary_hue="orange"), css="#title { text-align: center; margin-bottom: 10px; font-size: 24px; }") as demo:
        with gr.Column(elem_id="app-container"):
            gr.Markdown("# 🖼️ Image Safety Check", elem_id="title")

            gr.Markdown("Upload an image file or paste an image URL")
            
            with gr.Row():
                with gr.Column(scale=1):
                    image_input = gr.Image(type="pil", label="Upload Image:", height=200, sources=["upload"])
                with gr.Column(scale=1):
                    url_input = gr.Textbox(label="Or Paste Image URL:", lines=1)
                    analyze_button = gr.Button("🚀 Analyze Image", variant="primary")
            
            with gr.Row():
                with gr.Column():
                    analysis_output = gr.Textbox(label="Image Analysis with LlaVA 1.5 7B:", lines=6)
                with gr.Column():
                    safety_output = gr.Textbox(label="Safety Check with Llama Guard 3 8B:", lines=6)
            
            analyze_button.click(
                fn=process_image,
                inputs=[image_input, url_input],
                outputs=[analysis_output, safety_output]
            )
    
    demo.launch()

if __name__ == "__main__":
    launch()
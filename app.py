from transformers import pipeline
import gradio as gr

model = pipeline('summarization')

def predict(text):
    summary = model(text)[0]['summary_text']
    return summary

with gr.Blocks() as ui:
    textbox = gr.Textbox(placeholder='Enter text to summarize', label='input')
    gr.Interface(fn=predict, inputs=textbox, outputs='text')

if __name__ == '__main__':
    ui.launch()
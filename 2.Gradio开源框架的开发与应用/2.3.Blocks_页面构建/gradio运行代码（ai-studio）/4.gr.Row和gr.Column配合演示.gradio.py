import gradio as gr

def greet(name):
    return "Hello" + name + "!"

with gr.Blocks() as demo:
    with gr.Column():
        with gr.Row():
            name = gr.Textbox(label="Name")
            output = gr.Textbox(label = "Output Box")
    with gr.Column():
        greet_btn = gr.Button("Greet")
        greet_btn.click(fn=greet, inputs=name, outputs=output)

demo.launch()       
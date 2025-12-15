import gradio as gr

def greet(name):
    return "Hello" + name + "!"

with gr.Blocks() as demo:
    name = gr.Textbox(label="Name")
    output = gr.Textbox(label="Output Box")
    greet_btn = gr.Button("Greet") # 直接写入字符串（默认是 label = "Greet"
    greet_btn.click(fn=greet, inputs=name, outputs=output)

demo.launch()
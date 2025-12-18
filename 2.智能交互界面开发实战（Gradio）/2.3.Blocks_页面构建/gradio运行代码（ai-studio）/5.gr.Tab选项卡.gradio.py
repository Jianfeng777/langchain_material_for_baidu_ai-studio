import gradio as gr

with gr.Blocks() as demo:
    with gr.Tab("图片生成"):
        gr.Textbox(label="请输入提示词")
        gr.Image(label="生成结果")
    
    with gr.Tab("聊天机器人"):
        gr.Chatbot()
        gr.Textbox(label="请输入问题")

demo.launch()
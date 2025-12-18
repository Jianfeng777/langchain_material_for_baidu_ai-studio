import gradio as gr

with gr.Blocks() as demo:
    gr.Markdown("## 没有使用 gr.Group: ")
    gr.Textbox(label="姓名")
    gr.Textbox(label="邮箱")
    gr.Button("提交")
    
    gr.Markdown("## 使用 gr.Group: ")
    with gr.Group():
        gr.Textbox(label="姓名")
        gr.Textbox(label="邮箱")
        gr.Button("提交")

demo.launch()
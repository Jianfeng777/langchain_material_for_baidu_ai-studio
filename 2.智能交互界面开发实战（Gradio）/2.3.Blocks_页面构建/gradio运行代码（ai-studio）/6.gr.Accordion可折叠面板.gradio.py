import gradio as gr

with gr.Blocks() as demo:
    with gr.Accordion("更多设置", open=False): # 默认关闭
        gr.Slider(0, 100, value=50, label="音量")
        gr.Checkbox(label="启用高级模式")

    gr.Textbox(label="主要输出")

demo.launch()
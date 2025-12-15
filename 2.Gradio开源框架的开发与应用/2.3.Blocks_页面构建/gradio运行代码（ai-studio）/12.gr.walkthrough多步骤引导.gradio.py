import gradio as gr

with gr.Blocks() as demo:
    with gr.Walkthrough(selected=0) as walkthrough:  # selected=0 表示初始显示第 0 步
        # 第一步：上传图片
        with gr.Step("上传图片", id=0):
            img = gr.Image()
            btn1 = gr.Button("下一步")
            btn1.click(lambda: gr.Walkthrough(selected=1), outputs=walkthrough)

        # 第二步：输入提示词
        with gr.Step("输入提示词", id=1):
            prompt = gr.Textbox()
            btn2 = gr.Button("生成结果")
            btn2.click(lambda: gr.Walkthrough(selected=2), outputs=walkthrough)

        # 第三步：查看结果
        with gr.Step("查看结果", id=2):
            gr.Markdown("这里显示生成的图片或文本")

demo.launch()
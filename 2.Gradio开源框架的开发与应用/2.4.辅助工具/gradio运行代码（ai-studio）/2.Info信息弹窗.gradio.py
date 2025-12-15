import gradio as gr

def show_info():
  gr.Info("提示：这是一个 Info 弹窗！")
  return "函数已执行完毕"

demo = gr.Interface(fn=show_info, inputs=None, outputs="text",)

demo.launch() 
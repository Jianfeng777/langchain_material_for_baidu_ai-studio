import gradio as gr

def show_info():
  gr.Warning("提示：这是一个 Warning 弹窗！")
  return "函数已执行完毕"

demo = gr.Interface(fn=show_info, inputs=None, outputs="text",)

demo.launch() 
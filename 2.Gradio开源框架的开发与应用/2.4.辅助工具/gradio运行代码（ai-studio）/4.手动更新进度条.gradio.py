import gradio as gr
import time

def long_task(name, progress=gr.Progress()):
  progress(0.0, desc="开始处理…")
  time.sleep(1)
  progress(0.3, desc="正在加载数据…")
  time.sleep(1)
  progress(0.6, desc="正在处理数据…")
  time.sleep(1)
  progress(1.0, desc="处理完成！")
  return f"你好，{name}！任务已经完成。"

demo = gr.Interface(fn=long_task, inputs="text", outputs="text")
demo.launch()
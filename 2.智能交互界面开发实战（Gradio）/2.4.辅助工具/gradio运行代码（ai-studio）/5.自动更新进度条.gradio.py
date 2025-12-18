import gradio as gr
import time

def auto_progress_task(n, progress=gr.Progress()):
  # tqdm 自动更新进度条
  for i in progress.tqdm(range(n), desc="处理中…"):
    time.sleep(1)
  return f"循环了 {n} 次，全部完成！"

demo = gr.Interface(fn=auto_progress_task, inputs=gr.Number(label="循环次数"), outputs="text")

demo.launch()
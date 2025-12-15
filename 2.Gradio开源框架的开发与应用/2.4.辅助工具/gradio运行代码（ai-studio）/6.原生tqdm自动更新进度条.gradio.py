import gradio as gr
import time
from tqdm import tqdm

def auto_progress_task(n, progress=gr.Progress(track_tqdm=True)):
  for i in tqdm(range(n), desc="处理中…"): # 原生 tqdm
    time.sleep(1)
  return f"循环了 {n} 次，全部完成！"

demo = gr.Interface(
  fn=auto_progress_task, inputs=gr.Number(label="循环次数"), outputs="text")

demo.launch()
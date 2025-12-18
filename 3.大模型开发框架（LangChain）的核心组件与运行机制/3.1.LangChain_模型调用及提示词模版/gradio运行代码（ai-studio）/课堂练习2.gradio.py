# TODO：请使用提示词模版对其进行改造
from langchain_openai import ChatOpenAI
import gradio as gr
import os

def llm_development(question):
  llm = ChatOpenAI(model="ernie-3.5-8k",
  openai_api_key=os.environ.get("OPENAI_API_KEY"),
  base_url="https://aistudio.baidu.com/llm/lmapi/v3")
  response = llm.invoke(question)
  return response.content

with gr.Blocks() as demo:
  with gr.Row():
    with gr.Column():
      input = gr.Textbox()
      send = gr.Button('发送')
    output = gr.Textbox()
  send.click(fn=llm_development, inputs=input,outputs=output)
demo.launch()
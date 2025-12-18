import os
from openai import OpenAI
import gradio as gr

def greet(name, intensity):
    return "Hello, " + name + "!" * intensity

demo1 = gr.Interface(
    fn=greet,
    inputs=["text", gr.Slider(value=2, minimum=1, maximum=10, step=1)],
    outputs=[gr.Textbox(label="greeting", lines=3)],
    title='测试', 
    description='测试页面')

def llm_response(content):
  client = OpenAI(
  api_key=os.environ.get("OPENAI_API_KEY"), 
  base_url="https://aistudio.baidu.com/llm/lmapi/v3", 
  )

  chat_completion = client.chat.completions.create(
  messages=[
    {'role': 'system', 'content': '你是 AI Studio 实训AI开发平台的开发者助理，你精通开发相关的知识，负责给开发者提供搜索帮助建议。'},
    {'role': 'user', 'content': content}
  ],
  model="ernie-3.5-8k",
  )

  return chat_completion.choices[0].message.content

def chat_fn(message, history):
  reply = llm_response(message)
  return reply

demo2 = gr.ChatInterface(
  fn=chat_fn,
  title="AI Studio 小助理",
  description="能够提供开发相关的知识，给开发者提供搜索帮助建议。",
  examples=[
    "我在使用AI Studio实训平台时遇到了问题，应该如何寻求帮助？",
    "AI Studio实训平台支持哪些编程语言？",
    "如何在AI Studio实训平台上部署我的模型？",
  ],
  cache_examples=False,
  save_history = True,
)

demo = gr.TabbedInterface(
  interface_list=[demo1, demo2], 
  tab_names=["interface", "chatbot"])

demo.launch()
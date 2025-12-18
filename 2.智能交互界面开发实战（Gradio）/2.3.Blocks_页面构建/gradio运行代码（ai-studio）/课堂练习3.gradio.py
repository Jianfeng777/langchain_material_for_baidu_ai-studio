# 请先更新函数

import os
from openai import OpenAI
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

print(llm_response("你是谁？"))

# TODO：请实现 gradio Walkthrough 界面实现代码：
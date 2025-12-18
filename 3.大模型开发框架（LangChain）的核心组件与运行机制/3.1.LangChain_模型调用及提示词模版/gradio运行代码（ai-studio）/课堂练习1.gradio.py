# TODO：修改以下代码以完成任务

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
  model="ernie-3.5-8k",
  openai_api_key=os.environ.get("OPENAI_API_KEY"),
  base_url="https://aistudio.baidu.com/llm/lmapi/v3" 
)

response = llm.invoke("你好，请介绍一下你自己")

print(response.content)
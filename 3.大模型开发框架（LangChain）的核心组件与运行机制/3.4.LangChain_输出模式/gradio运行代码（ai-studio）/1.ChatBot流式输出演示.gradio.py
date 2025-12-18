from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
import os

llm = ChatOpenAI(
model="ernie-3.5-8k",
openai_api_key=os.environ.get("OPENAI_API_KEY"),
base_url="https://aistudio.baidu.com/llm/lmapi/v3")

prompt = ChatPromptTemplate.from_messages([
  ("system", "You are a helpful assistant."),
  MessagesPlaceholder(variable_name="chat_history"), 
  ("human", "{input}")])

chain = prompt | llm

session_store = {}

def get_session_history(session_id):
  if session_id not in session_store:
    session_store[session_id] = ChatMessageHistory()
  return session_store[session_id]

chain_with_history = RunnableWithMessageHistory(
  runnable=chain,
  get_session_history=get_session_history,
  input_messages_key="input",
  history_messages_key="chat_history"
)

import gradio as gr

session_id = "session_test5"

def chat_stream(message, history):
  history = history or []
  full_reply = ""

  # 使用 stream() 逐步输出
  for chunk in chain_with_history.stream(
    {"input": message},
    config={"configurable": {"session_id": session_id}}):
    delta = getattr(chunk, "content", None) or ""
    full_reply += delta

    # 逐步返回累积的完整内容
    yield "", history + [
      {"role": "user", "content": message},
      {"role": "assistant", "content": full_reply}]
    
with gr.Blocks() as demo:
  gr.Markdown("## 🤖 流式聊天机器人（带记忆功能）")
  chatbot = gr.Chatbot(label="LangChain ChatBot")
  msg = gr.Textbox(placeholder="和我聊聊吧...", lines=1)

  # 用 stream 函数绑定 msg.submit
  msg.submit(chat_stream, [msg, chatbot], [msg, chatbot])

  gr.ClearButton([msg, chatbot])

demo.launch()
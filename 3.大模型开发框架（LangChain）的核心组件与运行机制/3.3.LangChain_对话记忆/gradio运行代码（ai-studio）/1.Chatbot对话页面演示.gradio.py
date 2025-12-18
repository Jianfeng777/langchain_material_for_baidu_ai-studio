from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
import gradio as gr
import os

llm = ChatOpenAI(model="ernie-3.5-8k",
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

session_id = "session_test5"
def chat(message, history):
    history = history or []
    resp = chain_with_history.invoke(
        {"input": message},
        config={"configurable": {"session_id": session_id}},
    )
    reply = resp.content if hasattr(resp, "content") else str(resp)
    history = history + [
        {"role": "user", "content": message},
        {"role": "assistant", "content": reply},
    ]
    return "", history

with gr.Blocks() as demo:
    gr.Markdown("## 🤖 聊天机器人（内置记忆）")
    chatbot = gr.Chatbot(label="LangChain ChatBot")
    msg = gr.Textbox(placeholder="和我聊聊吧...", lines=1)
    msg.submit(chat, [msg, chatbot], [msg, chatbot])
    gr.ClearButton([msg, chatbot])

demo.launch()
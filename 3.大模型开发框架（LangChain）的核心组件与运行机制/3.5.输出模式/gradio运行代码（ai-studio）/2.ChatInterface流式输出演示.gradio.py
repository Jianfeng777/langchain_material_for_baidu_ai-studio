import os
import gradio as gr

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

session_store = {}

def get_session_history(session_id: str):
    if session_id not in session_store:
        session_store[session_id] = ChatMessageHistory()
    return session_store[session_id]


llm = ChatOpenAI(
    model="ernie-3.5-8k",
    openai_api_key=os.environ.get("OPENAI_API_KEY"),
    base_url="https://aistudio.baidu.com/llm/lmapi/v3")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}")
])

chain = prompt | llm

chain_with_history = RunnableWithMessageHistory(
    runnable=chain,
    get_session_history=get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history",
)

def llm_response(message, history):
    session_id = "session_test6"
    stream = chain_with_history.stream(
        {"input": message},
        config={"configurable": {"session_id": session_id}})

    partial_text = ""
    
    for chunk in stream: 
        if hasattr(chunk, "content") and chunk.content:
            partial_text += chunk.content
            yield partial_text


demo = gr.ChatInterface(fn=llm_response)

demo.launch()
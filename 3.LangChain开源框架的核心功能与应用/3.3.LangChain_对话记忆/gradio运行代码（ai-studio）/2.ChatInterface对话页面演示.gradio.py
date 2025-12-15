from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
import os

def get_session_history(session_id: str):
    if session_id not in session_store:
        session_store[session_id] = ChatMessageHistory()
    return session_store[session_id]

session_store = {}

def llm_response(content, history):
    llm = ChatOpenAI(
        model="ernie-3.5-8k",
        openai_api_key=os.environ.get("OPENAI_API_KEY"),
        base_url="https://aistudio.baidu.com/llm/lmapi/v3",
    )
    
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
    resp = chain_with_history.invoke(
            {"input": content},
            config={"configurable": {"session_id": session_id}},
        )
    reply = resp.content if hasattr(resp, "content") else str(resp)
    return reply

demo = gr.ChatInterface(fn=llm_response)

demo.launch()
from langchain_community.document_loaders import (
  WebBaseLoader,
  YoutubeLoader)
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_chroma import Chroma
import os
from langchain_community.document_loaders import (
  TextLoader,
  PyMuPDFLoader,
  Docx2txtLoader,
  UnstructuredMarkdownLoader,
  UnstructuredExcelLoader)
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# 初始化向量数据库
persist_directory='./chroma'
embeddings = DashScopeEmbeddings(
 dashscope_api_key=os.getenv('DASHSCOPE_API_KEY'), 
 model="text-embedding-v1")
vectordb = Chroma(persist_directory=persist_directory, embedding_function=embeddings)
# 初始化文本切分方法
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500,
 chunk_overlap=150)

def load_web_content(url: str):
  # 判断内容类型
  if 'youtube.com' in url or 'youtu.be' in url:
    loader = YoutubeLoader(url)
  else:
    loader = WebBaseLoader(url)
  docs = loader.load()
  # 文本切分
  splits = text_splitter.split_documents(docs)
  vectordb = Chroma.from_documents(
    documents=splits,
    persist_directory=persist_directory,
    embedding=embeddings)
  return f"已成功在 {persist_directory} 文件夹生成向量数据库"

def load_document(file_path: str):
 # 获取文件后缀名
 file_type = file_path.split('.')[-1].lower()
 # 根据文件类型选择合适的 Loader
 if file_type == 'txt':
  loader = TextLoader(file_path)
 elif file_type == 'pdf':
  loader = PyMuPDFLoader(file_path)
 elif file_type == 'docx':
  loader = Docx2txtLoader(file_path)
 elif file_type == 'md':
  loader = UnstructuredMarkdownLoader(file_path)
 elif file_type == 'xlsx':
  loader = UnstructuredExcelLoader(file_path)
 else:
  raise ValueError(f"不支持的文件类型: {file_type}")
 # 加载文档
 docs = loader.load()
 # 文本切分
 splits = text_splitter.split_documents(docs)
 vectordb = Chroma.from_documents(
  documents=splits,
  persist_directory=persist_directory,
  embedding=embeddings)
 return f"已成功在 {persist_directory} 文件夹生成向量数据库"

def format_docs(docs):
 return "\n\n".join(doc.page_content for doc in docs)
def chat(question, chat_history):
 # 初始化聊天模型
 llm = ChatOpenAI(model="ernie-4.0-turbo-128k",
 openai_api_key=os.environ.get("OPENAI_API_KEY"),
 base_url="https://aistudio.baidu.com/llm/lmapi/v3")
 # 构建提示词模版
 template = """请使用以下上下文信息回答最后的问题。
 如果您不知道答案，就直接说您不知道，不要试图编造答案。
 回答最多使用三句话。请尽可能简洁地回答。最后一定要说“谢谢提问！”。
 上下文：{context}
 问题：{question}
 有帮助的回答："""
 QA_CHAIN_PROMPT = PromptTemplate.from_template(template)
 retriever = vectordb.as_retriever(search_type="mmr", 
 search_kwargs={"k": 1, "fetch_k": 10, "lambda_mult": 0.25})
 qa_chain = (
 {"context": retriever | format_docs,
  "question": RunnablePassthrough()}
 | QA_CHAIN_PROMPT
 | llm
 | StrOutputParser())
 result = qa_chain.invoke({question}) 
 chat_history.append({"role": "user", "content": question})
 chat_history.append({"role": "assistant", "content": result})
 return chat_history, chat_history, ""

import gradio as gr
with gr.Blocks() as demo:
  gr.Markdown('# 基础 RAG 对话平台')
  with gr.Row():
    # 创建左侧列
    with gr.Column():
      # 创建一个文本框接收网页地址
      url = gr.Textbox(label='请输入网页地址')
      url_loader_button = gr.Button('点击生成向量数据库')
      # 创建一个文件上传组件接收文件
      document = gr.File(label='请上传文件')
      document_loader_button = gr.Button('点击生成向量数据库')
      # 创建一个 Markdown 块接收数据库生成的情况
      information = gr.Markdown()
      url_loader_button.click(fn = load_web_content, inputs= url , outputs= information)
      document_loader_button.click(fn = load_document, inputs = document, outputs = information)

    # 创建右侧列
    with gr.Column():
      # 创建一个 Chatbot 组件记录聊天内容
      chat_history = gr.Chatbot(label='聊天记录')
      # 创建一个文本区域记录要问的问题
      input_message = gr.TextArea(label='内容输入')
      state = gr.State([])
      input_message.submit(fn = chat, inputs=[input_message, state],outputs=[chat_history, state, input_message])
demo.launch()
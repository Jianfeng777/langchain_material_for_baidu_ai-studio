from langchain_community.chat_models import ChatTongyi
import os
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import create_agent

llm = ChatTongyi(api_key=os.environ.get("DASHSCOPE_API_KEY"), model="qwen-turbo")
tools = load_tools(["arxiv"])

from langchain.agents.middleware import HumanInTheLoopMiddleware

human_middleware = HumanInTheLoopMiddleware(
    interrupt_on={
        "arxiv": {
            "allowed_decisions": ["approve", "edit", "reject"],
            "description": "请确认是否调用 arXiv 工具查询论文。",
        }
    },
)

agent = create_agent(model=llm, 
                     tools=tools,
                     middleware=[human_middleware],
                     system_prompt="You are a helpful assistant")

# 请使用 arxiv 工具查询论文编号 1605.08386
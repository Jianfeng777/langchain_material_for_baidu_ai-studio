from langchain_community.chat_models import ChatTongyi
import os
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import create_agent

llm = ChatTongyi(api_key=os.environ.get("DASHSCOPE_API_KEY"), model="qwen-turbo")
tools = load_tools(["arxiv"])

from typing import Any
from langchain.agents.middleware import after_model
from langchain.agents.middleware import AgentState
from langgraph.runtime import Runtime
from langchain.messages import AIMessage

@after_model(can_jump_to=["end"])
def validate_output(state: AgentState, runtime: Runtime) -> dict[str, Any] | None:
    last_message = state["messages"][-1]
    if "BLOCKED" in last_message.content:
        return {"messages": [AIMessage("I cannot respond to that request.")],
            "jump_to": "end"}
    return None

agent = create_agent(model=llm, 
                     tools=tools,
                     middleware=[validate_output],
                     system_prompt="You are a helpful assistant")

# 请使用 arxiv 工具查询论文编号 1605.08386
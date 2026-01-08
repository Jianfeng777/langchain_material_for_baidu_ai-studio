from langchain_community.chat_models import ChatTongyi
import os
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import create_agent
from langchain.agents.middleware import AgentState
llm = ChatTongyi(api_key=os.environ.get("DASHSCOPE_API_KEY"), model="qwen-turbo")
tools = load_tools(["arxiv"])

class CustomAgentState(AgentState):
    user_id: str
    preferences: dict

agent = create_agent(model=llm, 
                     tools=tools,
                     state_schema=CustomAgentState,
                     system_prompt="You are a helpful assistant")
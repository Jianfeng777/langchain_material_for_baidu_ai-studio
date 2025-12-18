import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from langchain_community.chat_models import ChatTongyi
import os
# 若没有配置系统环境变量，请先获取阿里云百炼大模型 api_key 写入下方
# os.environ["DASHSCOPE_API_KEY"] = "sk-yyyyyyyy"

async def main():
    client = MultiServerMCPClient({
    "fetch": {
        "transport": "stdio",
        "command": "uvx",
        "args": ["mcp-server-fetch"]
    }
    })
    tools = await client.get_tools() # 异步加载 MCP 工具
    print(tools)

    agent = create_agent(model=ChatTongyi(model="qwen-max"), 
    tools=tools, 
    system_prompt="You are a helpful assistant", 
    checkpointer=InMemorySaver())
    # 异步调用 agent
    result1 = await agent.ainvoke({"messages": [{"role": "user", "content": "帮忙看看这个网页讲了什么？https://aistudio.baidu.com/overview"}]}, config={"configurable": {"thread_id": "user_1"}})
    print(result1)

asyncio.run(main())
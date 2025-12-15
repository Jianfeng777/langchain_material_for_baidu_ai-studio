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
            "transport": "http",
            "url": "https://mcp.api-inference.modelscope.net/2d1609a7c8fe45/mcp",
            "headers": {
                "Authorization": "Bearer ms-dec9499d-dc29-405d-8976-a3eed24b0918"
            }
        }
    })

    # 1. 加载 MCP 工具
    tools = await client.get_tools()
    print("Loaded tools:", tools)

    # 2. 创建 Agent
    agent = create_agent(
        model=ChatTongyi(model="qwen-max"),
        tools=tools,
        system_prompt="You are a helpful assistant",
        checkpointer=InMemorySaver()
    )

    # 3. 调用 Agent
    result = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "帮忙看看这个网页讲了什么？https://aistudio.baidu.com/overview"}]},
        config={"configurable": {"thread_id": "user_1"}}
    )

    print(result)

asyncio.run(main())
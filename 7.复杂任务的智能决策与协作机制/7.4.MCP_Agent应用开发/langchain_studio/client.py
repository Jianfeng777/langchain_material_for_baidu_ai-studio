import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_community.chat_models import ChatTongyi
from langgraph.checkpoint.memory import InMemorySaver
import os
# 若没有配置系统环境变量，请先获取阿里云百炼大模型 api_key 写入下方
# os.environ["DASHSCOPE_API_KEY"] = "sk-yyyyyyyy"

async def main():
  # 1. 创建 MCP 客户端
  client = MultiServerMCPClient({
    "DogUtils": {
      "transport": "stdio",
      "command": "python",
      "args": [r"7.智能体进阶实战\7.4.MCP_Agent应用开发\langchain_studio\server.py"]}}) # 替换本地路径
  # 异步加载 MCP 工具
  tools = await client.get_tools()
  agent = create_agent(model=ChatTongyi(model="qwen-max"), 
      tools=tools, 
      system_prompt="You are a helpful assistant", 
      checkpointer=InMemorySaver())
  # 异步调用 agent
  result1 = await agent.ainvoke({"messages": [{"role": "user", "content": "I have 2 dogs, a border collie and a scottish terrier. What is their combined weight? Could you double it?"}]}, config={"configurable": {"thread_id": "user_1"}})
  print(result1)
# ✅ 顶层执行异步函数
if __name__ == "__main__":
  asyncio.run(main())
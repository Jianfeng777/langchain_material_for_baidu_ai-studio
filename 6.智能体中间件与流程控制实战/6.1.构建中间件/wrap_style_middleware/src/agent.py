from langchain_community.chat_models import ChatTongyi
import os
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import create_agent

llm = ChatTongyi(api_key=os.environ.get("DASHSCOPE_API_KEY"), model="qwen-turbo")
tools = load_tools(["arxiv"])

from langchain.agents.middleware import wrap_model_call, ModelRequest, ModelResponse
from typing import Callable, Awaitable

@wrap_model_call
async def retry_model(
    request: ModelRequest,
    handler: Callable[[ModelRequest], Awaitable[ModelResponse]],
) -> ModelResponse:
    for attempt in range(3):
        try:
            return await handler(request)
        except Exception as e:
            if attempt == 2:
                raise
            print(f"Retry {attempt + 1}/3 after error: {e}")

agent = create_agent(model=llm, 
                     tools=tools,
                     middleware=[retry_model],
                     system_prompt="You are a helpful assistant")

# 请使用 arxiv 工具查询论文编号 1605.08386
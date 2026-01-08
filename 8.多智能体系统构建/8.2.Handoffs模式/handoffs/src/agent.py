"""
Customer Support State Machine Example

This example demonstrates the state machine pattern.
A single agent dynamically changes its behavior based on the current_step state,
creating a state machine for sequential information collection.
"""

import uuid

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import Command
from typing import Callable, Literal
from typing_extensions import NotRequired

from langchain.agents import AgentState, create_agent
from langchain.agents.middleware import wrap_model_call, ModelRequest, ModelResponse, SummarizationMiddleware
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage, ToolMessage
from langchain.tools import tool, ToolRuntime
from langchain_community.chat_models import ChatTongyi
import os

model = ChatTongyi(
    api_key=os.environ.get("DASHSCOPE_API_KEY"),
    model="qwen-max"
)


# Define the possible workflow steps
SupportStep = Literal["warranty_collector", "issue_classifier", "resolution_specialist"]


class SupportState(AgentState):
    """State for customer support workflow."""

    current_step: NotRequired[SupportStep]
    warranty_status: NotRequired[Literal["in_warranty", "out_of_warranty"]]
    issue_type: NotRequired[Literal["hardware", "software"]]


from langchain.tools import tool, ToolRuntime
from langchain.messages import ToolMessage
from langgraph.types import Command
from typing import Literal

@tool
def record_warranty_status(
    status: Literal["in_warranty", "out_of_warranty"],
    runtime: ToolRuntime[None, SupportState],
) -> Command:
    """记录客户保修状态，并切换到【问题分类】阶段。"""
    return Command(
        update={
            "messages": [
                ToolMessage(
                    content=f"保修状态已记录：{status}",
                    tool_call_id=runtime.tool_call_id,
                )
            ],
            "warranty_status": status,
            "current_step": "issue_classifier",
        }
    )

@tool
def record_issue_type(
    issue_type: Literal["hardware", "software"],
    runtime: ToolRuntime[None, SupportState],
) -> Command:
    """记录问题类型，并切换到【解决方案】阶段。"""
    return Command(
        update={
            "messages": [
                ToolMessage(
                    content=f"问题类型已记录：{issue_type}",
                    tool_call_id=runtime.tool_call_id,
                )
            ],
            "issue_type": issue_type,
            "current_step": "resolution_specialist",
        }
    )


@tool
def escalate_to_human(reason: str) -> str:
    """升级到人工支持。"""
    return f"已为你升级到人工支持。原因：{reason}"


@tool
def provide_solution(solution: str) -> str:
    """向客户提供解决方案。"""
    return f"已提供解决方案：{solution}"

@tool
def go_back_to_warranty(runtime: ToolRuntime[None, SupportState]) -> Command:
    """回到保修确认阶段。"""
    return Command(
        update={"messages": [
                ToolMessage(
                    content="已返回保修确认阶段",
                    tool_call_id=runtime.tool_call_id)],
            "current_step": "warranty_collector"})

@tool
def go_back_to_classification(
    runtime: ToolRuntime[None, SupportState]) -> Command:
    """回到问题分类阶段。"""
    return Command(update={
            "messages": [
                ToolMessage(
                    content="已返回问题分类阶段",
                    tool_call_id=runtime.tool_call_id)],
            "current_step": "issue_classifier"})

# Define prompts as constants
WARRANTY_COLLECTOR_PROMPT = """你是一名售后客服助手，正在帮助用户解决设备问题。

【当前阶段：确认保修】
你需要：
1. 友好地问候用户
2. 询问设备是否仍在保修期（或是否能提供购买时间/订单信息来判断）
3. 一旦信息足够明确，必须调用 record_warranty_status 记录结果并进入下一阶段

要求：语气自然、友好，不要一次问太多问题。"""

ISSUE_CLASSIFIER_PROMPT = """你是一名售后客服助手，正在帮助用户解决设备问题。
【当前阶段：问题分类】
已知信息：保修状态 = {warranty_status}
你需要：
1. 引导用户描述问题现象
2. 判断问题属于【硬件】还是【软件】
3. 一旦判断足够明确，必须调用 record_issue_type 记录分类并进入下一阶段

如果用户纠正了信息：
- 用 go_back_to_warranty 回到保修确认

如果不明确，可以继续追问，但不要武断下结论。"""

RESOLUTION_SPECIALIST_PROMPT = """你是一名专业的售后支持工程师，正在帮助用户解决设备问题。
【当前阶段：给出解决方案】
已知信息：
- 保修状态 = {warranty_status}
- 问题类型 = {issue_type}
你需要：
1. 如果是【软件问题】：调用 provide_solution 给出清晰的排查/修复步骤（从低风险到高风险）
2. 如果是【硬件问题】：
  - 在保修期：调用 provide_solution 说明官方保修维修流程、备份与注意事项
  - 不在保修期：调用 escalate_to_human 转人工说明付费维修选择
如果用户纠正了信息：
- 用 go_back_to_warranty 回到保修确认
- 用 go_back_to_classification 回到问题分类
要求：回复具体、可执行、条理清晰。"""


# Step configuration: maps step name to (prompt, tools, required_state)
STEP_CONFIG = {
    "warranty_collector": {
        "prompt": WARRANTY_COLLECTOR_PROMPT,
        "tools": [record_warranty_status],
        "requires": [],
    },
    "issue_classifier": {
        "prompt": ISSUE_CLASSIFIER_PROMPT,
        "tools": [record_issue_type, go_back_to_warranty],
        "requires": ["warranty_status"],
    },
    "resolution_specialist": {
        "prompt": RESOLUTION_SPECIALIST_PROMPT,
        "tools": [provide_solution, escalate_to_human, go_back_to_warranty, go_back_to_classification],
        "requires": ["warranty_status", "issue_type"],
    },
}

import inspect
@wrap_model_call
async def apply_step_config(   # 👈 注意：async
    request: ModelRequest,
    handler: Callable[[ModelRequest], ModelResponse],
) -> ModelResponse:
    current_step = request.state.get("current_step", "warranty_collector")
    step_config = STEP_CONFIG[current_step]

    for key in step_config["requires"]:
        if request.state.get(key) is None:
            raise ValueError(f"{key} must be set before reaching {current_step}")

    system_prompt = step_config["prompt"].format(**request.state)

    request = request.override(
        system_prompt=system_prompt,
        tools=step_config["tools"],
    )

    # 关键：handler 可能是 sync，也可能是 async
    if inspect.iscoroutinefunction(handler):
        return await handler(request)
    else:
        return handler(request)


# Collect all tools from all step configurations
all_tools = [record_warranty_status, record_issue_type, provide_solution, 
       escalate_to_human, go_back_to_warranty, go_back_to_classification]


summarizer = ChatTongyi(
    api_key=os.environ.get("DASHSCOPE_API_KEY"),
    model="qwen-plus",
    temperature=0.2,
)


# Create the agent with step-based configuration and summarization
agent = create_agent(
    model,
    tools=all_tools,
    state_schema=SupportState,
    middleware=[
        apply_step_config,
        SummarizationMiddleware(
            model=summarizer,
            trigger=("tokens", 4000),
            keep=("messages", 10)
        )
    ]
)


# ============================================================================
# Test the workflow
# ============================================================================

if __name__ == "__main__":
    thread_id = str(uuid.uuid4())
    config = {"configurable": {"thread_id": thread_id}}

    result = agent.invoke(
        {"messages": [HumanMessage("Hi, my phone screen is cracked")]},
        config
    )

    result = agent.invoke(
        {"messages": [HumanMessage("Yes, it's still under warranty")]},
        config
    )

    result = agent.invoke(
        {"messages": [HumanMessage("The screen is physically cracked from dropping it")]},
        config
    )

    result = agent.invoke(
        {"messages": [HumanMessage("What should I do?")]},
        config
    )
    for msg in result['messages']:
        msg.pretty_print()
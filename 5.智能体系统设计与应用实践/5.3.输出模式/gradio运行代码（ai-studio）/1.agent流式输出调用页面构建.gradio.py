from langchain_community.chat_models import ChatTongyi
import os

llm = ChatTongyi(
  api_key=os.environ.get("DASHSCOPE_API_KEY"), 
  model="qwen-max")

from langgraph.checkpoint.memory import InMemorySaver 
memory = InMemorySaver()

system_prompt = "You are a helpful assistant"

from langchain.tools import tool

@tool
def calculate(what: str) -> str:
  """
  calculate:
  e.g. calculate: 4 * 7 / 3
  Runs a calculation and returns the number - uses Python so be sure to use floating point syntax if necessary
  """
  return str(eval(what))

@tool
def average_dog_weight(name: str) -> str:
  """
  average_dog_weight:
  e.g. average_dog_weight: Collie
  returns average weight of a dog when given the breed
  """
  name = name.lower()
  if "scottish terrier" in name:
    return "Scottish Terriers average 20 lbs"
  elif "border collie" in name:
    return "A Border Collie's average weight is 37 lbs"
  elif "toy poodle" in name:
    return "A Toy Poodle's average weight is 7 lbs"
  else:
    return "An average dog weighs 50 lbs"
  
tools = [calculate, average_dog_weight]


from langchain.agents import create_agent
agent = create_agent(model=llm, tools=tools, system_prompt=system_prompt, checkpointer=memory)

import gradio as gr
def agent_response_stream_updates(content, history):
    # 🚨 不使用 Gradio 传入的 history
    round_history = []

    inputs = {
        "messages": [{"role": "user", "content": content}]
    }

    config = {
        "configurable": {"thread_id": "user_1"}  # Agent 记忆仍然保留
    }

    for chunk in agent.stream(
        inputs,
        config=config,
        stream_mode="updates"
    ):
        for step, data in chunk.items():
            blocks = data["messages"][-1].content_blocks

            for block in blocks:
                block_type = block.get("type")

                # ===== 1. model -> tool_call =====
                if step == "model" and block_type == "tool_call":
                    round_history.append(
                        {
                            "role": "assistant",
                            "content": f"{block['name']}({block.get('args')})",
                            "metadata": {"title": "🧠 Tool call"}
                        }
                    )
                    yield round_history

                # ===== 2. tools -> text =====
                elif step == "tools" and block_type == "text":
                    round_history.append(
                        {
                            "role": "assistant",
                            "content": block["text"],
                            "metadata": {"title": "🛠️ Tool result"}
                        }
                    )
                    yield round_history

                # ===== 3. model -> text =====
                elif step == "model" and block_type == "text":
                    round_history.append(
                        {
                            "role": "assistant",
                            "content": block["text"]
                        }
                    )
                    yield round_history

demo = gr.ChatInterface(
    fn=agent_response_stream_updates
)

demo.launch()

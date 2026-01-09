from typing import TypedDict

class Skill(TypedDict):
    """A skill that can be progressively disclosed to the agent."""
    name: str
    description: str
    content: str


SKILLS: list[Skill] = [
    {
        "name": "sales_analytics",
        "description": "Database schema and business logic for sales data analysis including customers, orders, and revenue.",
        "content": """# Sales Analytics Schema

## Tables

### customers
- customer_id (PRIMARY KEY)
- name
- email
- signup_date
- status (active/inactive)
- customer_tier (bronze/silver/gold/platinum)

### orders
- order_id (PRIMARY KEY)
- customer_id (FOREIGN KEY -> customers)
- order_date
- status (pending/completed/cancelled/refunded)
- total_amount
- sales_region (north/south/east/west)

### order_items
- item_id (PRIMARY KEY)
- order_id (FOREIGN KEY -> orders)
- product_id
- quantity
- unit_price
- discount_percent

## Business Logic

**Active customers**: status = 'active' AND signup_date <= CURRENT_DATE - INTERVAL '90 days'

**Revenue calculation**: Only count orders with status = 'completed'. Use total_amount from orders table, which already accounts for discounts.

**Customer lifetime value (CLV)**: Sum of all completed order amounts for a customer.

**High-value orders**: Orders with total_amount > 1000

## Example Query

-- Get top 10 customers by revenue in the last quarter
SELECT
    c.customer_id,
    c.name,
    c.customer_tier,
    SUM(o.total_amount) as total_revenue
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE o.status = 'completed'
  AND o.order_date >= CURRENT_DATE - INTERVAL '3 months'
GROUP BY c.customer_id, c.name, c.customer_tier
ORDER BY total_revenue DESC
LIMIT 10;
""",
    },
    {
        "name": "inventory_management",
        "description": "Database schema and business logic for inventory tracking including products, warehouses, and stock levels.",
        "content": """# Inventory Management Schema

## Tables

### products
- product_id (PRIMARY KEY)
- product_name
- sku
- category
- unit_cost
- reorder_point (minimum stock level before reordering)
- discontinued (boolean)

### warehouses
- warehouse_id (PRIMARY KEY)
- warehouse_name
- location
- capacity

### inventory
- inventory_id (PRIMARY KEY)
- product_id (FOREIGN KEY -> products)
- warehouse_id (FOREIGN KEY -> warehouses)
- quantity_on_hand
- last_updated

### stock_movements
- movement_id (PRIMARY KEY)
- product_id (FOREIGN KEY -> products)
- warehouse_id (FOREIGN KEY -> warehouses)
- movement_type (inbound/outbound/transfer/adjustment)
- quantity (positive for inbound, negative for outbound)
- movement_date
- reference_number

## Business Logic

**Available stock**: quantity_on_hand from inventory table where quantity_on_hand > 0

**Products needing reorder**: Products where total quantity_on_hand across all warehouses is less than or equal to the product's reorder_point

**Active products only**: Exclude products where discontinued = true unless specifically analyzing discontinued items

**Stock valuation**: quantity_on_hand * unit_cost for each product

## Example Query

-- Find products below reorder point across all warehouses
SELECT
    p.product_id,
    p.product_name,
    p.reorder_point,
    SUM(i.quantity_on_hand) as total_stock,
    p.unit_cost,
    (p.reorder_point - SUM(i.quantity_on_hand)) as units_to_reorder
FROM products p
JOIN inventory i ON p.product_id = i.product_id
WHERE p.discontinued = false
GROUP BY p.product_id, p.product_name, p.reorder_point, p.unit_cost
HAVING SUM(i.quantity_on_hand) <= p.reorder_point
ORDER BY units_to_reorder DESC;
""",
    },
]

from langchain.agents.middleware import AgentState
from typing import NotRequired

class CustomState(AgentState):
    skills_loaded: NotRequired[list[str]]

from langgraph.types import Command
from langchain.tools import tool, ToolRuntime
from langchain.messages import ToolMessage

@tool
def load_skill(skill_name: str, runtime: ToolRuntime) -> Command:
    """
    将指定技能（skill）的完整内容加载到智能体的上下文中。

    当需要处理某一类特定请求、并且必须了解该业务领域的
    详细说明、业务规则或操作规范时，使用此工具。

    参数：
        skill_name：要加载的技能名称
    """
    # 查找并返回对应的技能
    for skill in SKILLS:
        if skill["name"] == skill_name:
            skill_content = f"已加载技能：{skill_name}\n\n{skill['content']}"

            # 更新系统状态，用于记录已加载的技能
            return Command(
                update={
                    "messages": [
                        ToolMessage(
                            content=skill_content,
                            tool_call_id=runtime.tool_call_id,
                        )
                    ],
                    # 在 agent 的 state 中记录已加载的技能名称
                    "skills_loaded": [skill_name],
                }
            )

    # 未找到对应技能
    available = ", ".join(s["name"] for s in SKILLS)
    return Command(
        update={
            "messages": [
                ToolMessage(
                    content=f"未找到技能“{skill_name}”。可用技能包括：{available}",
                    tool_call_id=runtime.tool_call_id,
                )
            ]
        }
    )


@tool
def write_sql_query(
    query: str,
    vertical: str,
    runtime: ToolRuntime,
) -> str:
    """
    为指定的业务领域编写并校验一条 SQL 查询。

    该工具用于对 SQL 查询进行格式化与校验。
    在使用该工具之前，必须先加载对应的 skill，
    以确保已经理解该业务领域的数据库结构（schema）。

    参数说明：
        query：要编写/校验的 SQL 查询语句
        vertical：业务领域名称（sales_analytics 或 inventory_management）
    """
    # 从运行时状态中读取已经加载过的技能列表
    skills_loaded = runtime.state.get("skills_loaded", [])

    # 如果所需的业务领域 skill 尚未加载，则返回错误提示
    if vertical not in skills_loaded:
        return (
            f"错误：在编写 SQL 查询之前，必须先加载 '{vertical}' 技能，"
            f"以便理解对应的数据库结构。"
            f"请先使用 load_skill('{vertical}') 来加载该 schema。"
        )

    # 校验并格式化 SQL 查询（此处为示例实现）
    return (
        f"{vertical} 业务领域的 SQL 查询如下：\n\n"
        f"```sql\n{query}\n```\n\n"
        f"✓ 查询已通过 {vertical} schema 校验\n"
        f"可以安全地在数据库中执行。"
    )

from langchain.agents.middleware import ModelRequest, ModelResponse, AgentMiddleware
from langchain.messages import SystemMessage
from typing import Callable, NotRequired
from typing import Awaitable

class SkillMiddleware(AgentMiddleware):
    state_schema = CustomState
    tools = [load_skill, write_sql_query]

    def __init__(self):
        skills_list = []
        for skill in SKILLS:
            skills_list.append(
                f"- **{skill['name']}**：{skill['description']}"
            )
        self.skills_prompt = "\n".join(skills_list)

    # =====================
    # 同步版本（你已有）
    # =====================
    def wrap_model_call(
        self,
        request: ModelRequest,
        handler: Callable[[ModelRequest], ModelResponse],
    ) -> ModelResponse:
        modified_request = self._inject_skills(request)
        return handler(modified_request)

    # =====================
    # 🔥 新增：异步版本
    # =====================
    async def awrap_model_call(
        self,
        request: ModelRequest,
        handler: Callable[[ModelRequest], Awaitable[ModelResponse]],
    ) -> ModelResponse:
        modified_request = self._inject_skills(request)
        return await handler(modified_request)

    # =====================
    # 抽出来的公共逻辑
    # =====================
    def _inject_skills(self, request: ModelRequest) -> ModelRequest:
        skills_addendum = (
            f"\n\n## 可用技能（Available Skills）\n\n{self.skills_prompt}\n\n"
            "当你需要处理某一类具体请求的详细信息时，"
            "请使用 load_skill 工具来加载对应技能的完整内容。"
        )

        new_content = list(request.system_message.content_blocks) + [
            {"type": "text", "text": skills_addendum}
        ]

        new_system_message = SystemMessage(content=new_content)

        return request.override(system_message=new_system_message)

    def wrap_model_call(
        self,
        request: ModelRequest,
        handler: Callable[[ModelRequest], ModelResponse],
    ) -> ModelResponse:
        """同步执行：在模型调用前，将技能描述注入到 system prompt 中。"""
        # 构建技能说明的补充内容
        skills_addendum = (
            f"\n\n## 可用技能（Available Skills）\n\n{self.skills_prompt}\n\n"
            "当你需要处理某一类具体请求的详细信息时，"
            "请使用 load_skill 工具来加载对应技能的完整内容。"
        )

        # 将技能说明追加到系统消息的内容块中
        new_content = list(request.system_message.content_blocks) + [
            {"type": "text", "text": skills_addendum}
        ]

        # 构造新的系统消息
        new_system_message = SystemMessage(content=new_content)

        # 用新的 system message 覆盖原有请求中的 system message
        modified_request = request.override(system_message=new_system_message)

        # 将修改后的请求继续交给下一个处理器（模型）执行
        return handler(modified_request)
    
from langchain.agents import create_agent
from langchain_community.chat_models import ChatTongyi
import os
model = ChatTongyi(api_key=os.environ.get("DASHSCOPE_API_KEY"), model="qwen-turbo")

agent = create_agent(
    model,
    system_prompt=(
        "你是一个 SQL 查询助手，"
        "负责帮助用户针对企业级业务数据库编写 SQL 查询。"
    ),
    middleware=[SkillMiddleware()]
)
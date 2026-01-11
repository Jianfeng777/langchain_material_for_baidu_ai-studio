# 大语言模型（LLM）应用开发完整教程

<div align="center">

面向**初学者**的 LLM 应用开发全栈课程：从模型调用到 RAG、Agent、多智能体、评估与部署。  
配套完整中文 Notebook + 可运行代码，帮助你从 0 到 1 构建可落地的 LLM 应用。

![Python](https://img.shields.io/badge/Python-3.12%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)

</div>

---

## 🎯 课程定位

这是一个**体系完整、结构清晰、面向工程实践**的 LLM 应用开发课程。内容覆盖 LangChain 文档的大部分核心能力，并补充了旧版本中仍常用的实践，同时剔除了已弃用的内容。  
你将从「模型调用」出发，逐步掌握 Gradio、LangChain、RAG、Agent、多智能体、LangGraph 与 LangSmith，完成一条完整的工程学习路径。

---

## ✨ 你将收获什么？

- ✅ **从 0 到 1 的完整路线**：基础调用 → RAG → Agent → 多智能体 → 评估部署
- ✅ **面向初学者**：中文讲解 + Notebook 逐步引导
- ✅ **工程化视角**：强调可复现、可调试、可扩展
- ✅ **贴近真实业务**：包含 LangChain / Gradio / LangGraph / LangSmith 实战

---

## 📖 内容导航（按章节）

### 1️⃣ 大语言模型应用基础
- 环境配置与 API Key 获取（AI Studio / 百炼平台）
- 模型调用：非流式 / 流式 / 切换模型
- 提示词与基础调用范式

### 2️⃣ 智能交互界面开发实战（Gradio）
- Interface 快速搭建与参数配置
- Blocks 布局组件：Row / Column / Tab / Accordion
- 弹窗系统、进度条、事件与状态管理

### 3️⃣ LangChain 核心组件与运行机制
- 模型调用：OpenAI 格式 / LangChain 格式 / 多轮并发
- PromptTemplate 与 ChatPromptTemplate
- 链式流程与 LCEL（RunnableLambda、函数节点）
- 对话记忆：全量记忆 / 摘要 / 压缩策略
- 流式输出与输出解析器（Parser）

### 4️⃣ 检索增强搜索（RAG）应用实战
- 文档载入：txt / pdf / csv / url / ipynb
- 文档切分：Character / Recursive / Markdown
- Embedding 与向量库存储（InMemory / Chroma）
- 检索策略：相似度搜索 / MMR
- 提示词与前端展示

### 5️⃣ 智能体系统设计与应用实践
- 原生 ReAct Agent 构建（LLM / Memory / Tool / Prompt）
- LangChain Agent 结构化搭建
- 流式输出模式与 ChatInterface 实现
- LangSmith Studio 部署与可视化

### 6️⃣ 智能体中间件与流程控制实战
- 自定义中间件（Decorator / Class / Node-style hooks）
- 内置中间件：模型降级、工具重试、调用限制
- 记忆管理：裁剪 / 删除 / 摘要
- 安全防护：PII 脱敏 / 人工审核 / 安全审查

### 7️⃣ 智能体工具能力进阶
- RAG Agent 实战
- SQL Agent 实战
- Search Agent 实战
- MCP Agent：Studio / streamable-http / 外部工具

### 8️⃣ 多智能体系统构建
- Subagents：子工具与子智能体组合
- Handoffs：状态管理与任务交接
- Skills：技能载入与技能中间件
- Router + LangGraph：图结构路由与多智能体协作

### 9️⃣ 大模型系统的测试、评估与部署
- Callback 与链路回调
- LangSmith Tracing：wrap_openai / @traceable
- 评估体系：数据集、评估器、评估流程
- 自动化测试：轨迹匹配与严格评估

---

## 🚀 快速开始

### 前置要求

- Python **3.12+**
- Conda（推荐）或 Pip / venv
- 内存建议 **4GB+**

建议先阅读 `environment.yml` / `requirements.txt` 并配置模型 API Key。

### 环境配置（Conda，推荐）

```bash
# 1) 克隆仓库
git clone git@github.com:SmartFlowAI/langchain_material_for_baidu_ai-studio.git
cd langchain_material_for_baidu_ai-studio

# 2) 创建环境
conda env create -f environment.yml

# 3) 激活环境
conda activate langchain_course
```

### 环境配置（Pip）

```bash
# 1) 克隆仓库
git clone <your-repo-url>
cd <your-repo-name>

# 2) 创建虚拟环境
python -m venv venv

# 3) 激活虚拟环境
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# 4) 安装依赖
pip install -r requirements.txt
```

### 运行 Notebook

```bash
# Jupyter Notebook
jupyter notebook

# 或使用 JupyterLab（推荐）
jupyter lab
```

### 运行 Gradio 示例

```bash
# 进入示例目录（按你的实际路径选择）
cd "2.智能交互界面开发实战（Gradio）/2.2.Interface_页面构建/gradio运行代码（ai-studio）"

# 运行示例
python "1.快速创建.gradio.py"
```

---

## 🧭 学习指引（建议路径）

### 0️⃣ 快速上手（30~60 分钟）
1. 完成第 1 章「模型调用」与「流式输出」
2. 运行第 2 章 Interface 示例，搭建第一个可交互页面
3. 浏览第 4 章「文档切分 + 向量检索」，体验 RAG 流程

### 1️⃣ 系统掌握（推荐主线）
1. 第 1 章 → 第 3 章：打牢模型调用与 LangChain 组件基础
2. 第 4 章：完成 RAG 全流程
3. 第 5-6 章：掌握 Agent 与流程控制
4. 第 7-8 章：扩展工具与多智能体架构
5. 第 9 章：掌握评估、测试与可观测性

---

## 📂 项目结构

```text
.
├── environment.yml
├── requirements.txt
├── README.md
│
├── 1.大语言模型应用基础/
├── 2.智能交互界面开发实战（Gradio）/
├── 3.大模型开发框架（LangChain）的核心组件与运行机制/
├── 4.检索增强搜索（RAG）应用实战/
├── 5.智能体系统设计与应用实践/
├── 6.智能体中间件与流程控制实战/
├── 7.智能体工具能力进阶/
├── 8.多智能体系统构建/
└── 9.大模型系统的测试、评估与部署/
```

---

## 🤝 如何贡献

欢迎提交 Issue / PR / 建议。建议流程：

1. Fork 本仓库并创建分支：`feat/xxx` 或 `fix/xxx`
2. 保持目录结构与命名一致，示例需可运行
3. 提交 PR 并说明修改内容与动机

---

## 📜 开源协议

本项目基于 **MIT License** 开源，详见 [LICENSE](LICENSE)。

---

## 🙏 致谢

感谢以下团队与社区对本项目的支持：

- **机智流**
- **百度飞桨星河社区（AI Studio）**
- **LangChain 团队**
- **Gradio 团队**

---

## 📮 联系方式

如有问题或建议，欢迎通过以下方式联系：

- 提交 GitHub Issues
- 邮箱：[763915794@qq.com](mailto:763915794@qq.com)

---

**最后更新：2026-01-10**  
持续更新中…

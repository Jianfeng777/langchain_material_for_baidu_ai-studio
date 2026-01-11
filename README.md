# 大语言模型（LLM）应用开发完整教程

<div align="center">

<img src="./images/cover.png" width="90%" />

面向 **初学者** 的 LLM 应用开发全栈课程：  
从模型调用到 RAG、Agent、多智能体、评估与部署。  

![Python](https://img.shields.io/badge/Python-3.12%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)

</div>


---

## 🎯 课程定位

本课程是一门**体系完整、结构清晰、面向工程实践**的 LLM 应用开发课程。内容覆盖 LangChain 文档的大部分核心能力，并补充了旧版本中仍常用的实践，同时剔除了已弃用的内容。  

你将从「模型调用」出发，逐步掌握 Gradio、LangChain、RAG、Agent、Multi-Agent、LangGraph 与 LangSmith，完成一条完整的工程学习路径。

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
- Interface 快速搭建
- Blocks 布局实操
- 弹窗系统、进度条、事件与状态管理等辅助功能

### 3️⃣ LangChain 核心组件与运行机制
- 模型调用
- PromptTemplate 与 ChatPromptTemplate
- 链式流程（LCEL）
- 对话记忆：全量记忆 / 摘要 / 压缩策略
- 流式输出与输出解析器（Parser）

### 4️⃣ 检索增强搜索（RAG）应用实战
- 文档载入：txt / pdf / csv / url / ...
- 文档切分：Character / Recursive / ...
- Embedding 与向量库存储：InMemory / Chroma / ...
- 检索策略：相似度搜索 / MMR / ...

### 5️⃣ 智能体系统设计与应用实践
- 原生 ReAct Agent 构建
- 基于 LangChain V1 的 Agent 搭建
- Agent 流式输出与结构化输出
- LangSmith Studio 部署与可视化

### 6️⃣ 智能体中间件与流程控制实战
- 自定义中间件（Decorator / Class）
- 内置中间件：模型降级、工具重试、调用限制...
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
- 大模型跟踪：wrap_openai / @traceable / ...
- 评估体系：数据集、评估器、评估流程...
- 自动化测试：轨迹匹配与基于大模型的评估测试

---

## 🚀 快速开始

### 环境配置（Conda，推荐）

```bash
# 1) 克隆仓库
git clone git@github.com:SmartFlowAI/langchain_material_for_baidu_ai-studio.git
cd langchain_material_for_baidu_ai-studio

# 2) 创建环境
conda create -n langchain_course python=3.12 -y
conda activate langchain_course
pip install -r requirements.txt

# 或直接通过 environment.yml 进行安装
# conda env create -f environment.yml

# 3) 激活环境
conda activate langchain_course
```

---

## 📂 项目结构

```text
.
├── environment.yml
├── requirements.txt
├── README.md
├── images/
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
---

## 📮 联系方式

如有问题或建议，欢迎通过以下方式联系：

- 提交 GitHub Issues
- 邮箱：[763915794@qq.com](mailto:763915794@qq.com)

---

**最后更新：2026-01-10**  
持续更新中…
# 大语言模型（LLM）应用开发完整教程

<div align="center">

一套**从入门到进阶**的大语言模型应用开发课程库（含完整代码示例与项目实战），覆盖 LLM 应用开发全流程。

![Python](https://img.shields.io/badge/Python-3.12%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)

</div>

---

## 目录

- [项目简介](#项目简介)
- [核心特性](#核心特性)
- [课程结构](#课程结构)
- [快速开始](#快速开始)
  - [环境配置（Conda）](#环境配置conda推荐)
  - [环境配置（Pip）](#环境配置pip)
  - [运行 Notebook](#运行-notebook)
  - [运行 Gradio 示例](#运行-gradio-示例)
- [依赖说明](#依赖说明)
- [学习路径建议](#学习路径建议)
- [主要技术点](#主要技术点)
- [项目结构](#项目结构)
- [常见问题](#常见问题)
- [推荐阅读](#推荐阅读)
- [贡献指南](#贡献指南)
- [许可证](#许可证)
- [致谢](#致谢)
- [联系方式](#联系方式)

---

## 项目简介

本项目是一套完整的大语言模型（Large Language Models, LLM）应用开发教程，覆盖从基础概念到高级工程实战的系统内容。课程采用**循序渐进**的设计方式，并配套大量可运行示例，帮助开发者快速掌握现代 LLM 应用开发所需的关键技能与工程方法。

---

## 核心特性

- ✅ **体系完整**：覆盖 LLM 应用开发全生命周期（构建 → 工具集成 → 多智能体 → 评估与部署）
- ✅ **实战导向**：每个模块均提供可运行示例与项目化练习，便于迁移到真实业务
- ✅ **框架全面**：集成 LangChain、Gradio、LangGraph 等主流框架与常用组件
- ✅ **讲解深入**：兼顾原理与工程实践，强调可复现、可调试、可扩展
- ✅ **开箱即用**：提供 Conda / Pip 两套环境配置，降低上手成本

---

## 课程结构

### 1️⃣ 大语言模型应用基础
掌握 LLM 的核心概念与基本应用模式：模型调用、参数设置、Prompt Engineering 入门等。

### 2️⃣ 智能交互界面开发实战（Gradio）
学习用 Gradio 构建交互式 LLM 应用：Interface、Blocks、事件机制、状态管理等。

### 3️⃣ 大模型开发框架（LangChain）核心组件与运行机制
深入理解 LangChain 的关键抽象与工程组织：模型、链、记忆、输出结构、运行机制等。

### 4️⃣ 检索增强生成（RAG）应用实战
从文档加载、切分、向量化到检索与生成，构建完整 RAG 流程并掌握关键工程细节。

### 5️⃣ 智能体系统设计与应用实践
从零构建智能体：工具调用、规划与执行、输出模式、部署与工程化落地。

### 6️⃣ 智能体中间件与流程控制实战
掌握高级流程控制：中间件机制、记忆管理、安全策略、可控性增强与工程化约束。

### 7️⃣ 智能体工具能力进阶
扩展智能体工具箱：RAG 工具、SQL 工具、Web Search 工具与 MCP 工具接入。

### 8️⃣ 多智能体系统构建
构建多智能体协作架构：Subagents、Handoffs、Skills、Router 等模式与组合实践。

### 9️⃣ 大模型系统的测试、评估与部署
面向生产质量：回调与跟踪、评估体系、自动化测试、部署与可观测性实践。

---

## 快速开始

### 前置要求

- Python **3.12+**
- Conda（推荐）或 Pip / venv
- 内存建议 **4GB+**

> 建议先阅读本仓库的 `environment.yml` / `requirements.txt`，并按需配置各模型服务的 API Key。

---

### 环境配置（Conda，推荐）

```bash
# 1) 克隆仓库
git clone <your-repo-url>
cd <your-repo-name>

# 2) 创建环境
conda env create -f environment.yml

# 3) 激活环境
conda activate langchain_course
````

---

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

---

### 运行 Notebook

```bash
# Jupyter Notebook
jupyter notebook

# 或使用 JupyterLab（推荐）
jupyter lab
```

然后在浏览器中打开对应的 `.ipynb` 文件即可。

---

### 运行 Gradio 示例

```bash
# 进入示例目录（按你的实际路径选择）
cd "2.智能交互界面开发实战（Gradio）/2.2.Interface_页面构建/gradio运行代码（ai-studio）"

# 运行示例
python "1.快速创建.gradio.py"
```

---

## 依赖说明

### 核心依赖（示例）

| 库                   |     版本 | 说明             |
| ------------------- | -----: | -------------- |
| LangChain           |  1.2.0 | LLM 应用开发框架     |
| LangChain-OpenAI    |  1.1.6 | OpenAI 集成      |
| LangChain-Community |  0.4.1 | 社区工具集          |
| Gradio              |  6.2.0 | Web UI 构建      |
| Chroma              |  1.4.0 | 向量数据库          |
| OpenAI              | 2.11.0 | OpenAI API 客户端 |

完整依赖请查看：[requirements.txt](requirements.txt)（约 241 个包）

---

## 学习路径建议

### 初学者路径

1. 第 1 章：大语言模型应用基础
2. 第 2 章：Gradio 交互界面开发
3. 第 3 章：LangChain 核心组件与机制

### 中级开发者路径

1. 第 3 章：LangChain 核心组件
2. 第 4 章：RAG 应用实战
3. 第 5 章：智能体系统设计

### 高级开发者路径

1. 第 5 章：智能体系统设计
2. 第 6 章：中间件与流程控制
3. 第 7 章：工具能力进阶
4. 第 8 章：多智能体系统
5. 第 9 章：评估、测试与部署

---

## 主要技术点

### 大语言模型（LLM）

* GPT / Claude / Llama 等模型调用与应用组织
* Prompt Engineering 与提示词工程实践
* 典型优化策略：缓存、批量、超时与重试、成本控制等

### LangChain 框架

* LCEL（LangChain Expression Language）
* Chain / Runnable / Agent 设计
* Memory 与 Context 管理
* Tool 与结构化输出集成

### RAG 系统

* 文档加载与清洗（Document Loading / Processing）
* 分块策略（Text Splitting / Chunking）
* Embedding 与向量存储（Vector Store）
* 检索与排序（Retrieval / Ranking）

### 智能体系统

* Agent 架构与工具调用
* 决策逻辑与执行策略
* 记忆管理与可控性
* 中间件与安全机制

### Web UI 开发

* Gradio Interface / Blocks
* 事件系统与状态管理
* 部署与分享

---

## 项目结构

```text
.
├── environment.yml
├── requirements.txt
├── README.md
│
├── 1.大语言模型应用基础/
│   └── *.ipynb
│
├── 2.智能交互界面开发实战（Gradio）/
│   ├── 2.1.（选看）函数/
│   ├── 2.2.Interface_页面构建/
│   ├── 2.3.Blocks_页面构建/
│   ├── 2.4.辅助工具/
│   └── gradio运行代码（ai-studio）/
│
├── 3.大模型开发框架（LangChain）.../
│   ├── 3.1.LangChain_模型调用及提示词模版/
│   ├── 3.2.LangChain_链式调用/
│   ├── 3.3.LangChain_对话记忆/
│   └── 3.4.LangChain_输出模式/
│
├── 4.检索增强搜索（RAG）应用实战/
│   ├── 4.1.文档载入/
│   ├── 4.2.文档切分/
│   ├── 4.3.向量数据库生成/
│   └── 4.4.向量数据库检索/
│
├── 5.智能体系统设计与应用实践/
│   ├── 5.1.原生开发/
│   ├── 5.2.框架开发/
│   ├── 5.3.输出模式/
│   └── 5.4.智能体部署/
│
├── 6.智能体中间件与流程控制实战/
│   ├── 6.1.构建中间件/
│   ├── 6.2.内置中间件/
│   ├── 6.3.智能体记忆/
│   └── 6.4.智能体安全/
│
├── 7.智能体工具能力进阶/
│   ├── 7.1.RAG工具/
│   ├── 7.2.SQL工具/
│   ├── 7.3.Web_Search工具/
│   └── 7.4.MCP工具/
│
├── 8.多智能体系统构建/
│   ├── 8.1.Subagents模式/
│   ├── 8.2.Handoffs模式/
│   ├── 8.3.Skills模式/
│   └── 8.4.Router模式/
│
└── 9.大模型系统的测试、评估与部署/
    ├── 9.1.大模型回调/
    ├── 9.2.大模型跟踪/
    ├── 9.3.大模型评估/
    └── 9.4.大模型测试/
```

---

## 常见问题

### Q: 如何选择模型？

优先选择能力更稳定的模型（如 GPT-4 系列），也可替换为 Claude、Llama 等。不同模型需配置对应的 API Key / Base URL / 计费策略。

### Q: 向量数据库怎么选？

* **Chroma**：适合快速原型
* **FAISS**：适合本地大规模向量检索
* **Milvus**：更偏生产级部署与集群化

### Q: 如何处理 API 超时或不稳定？

建议组合使用：合理的 `timeout`、指数退避重试、异步调用、缓存、降级策略与监控追踪。

### Q: 能否离线使用？

可以使用本地开源模型（如 Llama 系列），但需要相应硬件与推理框架支持，且效果与成本需要权衡。

### Q: 如何优化成本？

可从缓存、提示词长度、批量请求、模型分层（便宜模型做前置过滤）等方向入手。

---

## 推荐阅读

* [LangChain 官方文档](https://python.langchain.com/)
* [Gradio 官方文档](https://www.gradio.app/)
* [OpenAI API 文档](https://platform.openai.com/docs)
* [Prompt Engineering Guide](https://www.promptingguide.ai/)

---

## 贡献指南

欢迎提交 Issue / PR / 建议。建议贡献流程：

1. Fork 本仓库并创建分支：`feat/xxx` 或 `fix/xxx`
2. 保持目录结构与命名一致，示例需可运行
3. 提交 PR 并说明修改内容与动机

---

## 许可证

本项目基于 **MIT License** 开源，详见 [LICENSE](LICENSE)。

---

## 致谢

感谢以下团队与社区对本项目的支持：

* **百度飞桨星河社区（AI Studio）**：感谢其提供算力与平台资源支持
* **LangChain 团队**：提供了强大的 LLM 应用开发框架
* **Gradio 团队**：提供了高效易用的 Web UI 构建工具

---

## 联系方式

如有问题或建议，欢迎通过以下方式联系：

* 提交 GitHub Issues
* 邮箱：[763915794@qq.com](mailto:763915794@qq.com)

---

**最后更新：2026-01-09**
持续更新中…
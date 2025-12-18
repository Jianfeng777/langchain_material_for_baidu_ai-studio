# LangChain 大模型应用开发完整教程

这是一套完整的大语言模型（LLM）应用开发教程，涵盖从基础理论到高级应用的全程学习路径。通过本课程，你将学会如何使用大模型 API、开发智能交互界面、构建 LangChain 应用、实现 RAG 系统、设计智能体系统，以及对模型进行测试和部署。

## 📚 课程结构

### 1. **大语言模型原理与应用基础** 
   - 学习大语言模型的基本原理
   - 掌握 OpenAI SDK 的使用方式
   - 集成百度 AI Studio 和阿里云百炼平台的模型调用
   - 实现基础的文本生成和对话功能

### 2. **智能交互界面开发实战（Gradio）**
   - 使用 Gradio 快速构建 Web 交互界面
   - **2.1 函数基础**：Python 函数编程基础知识
   - **2.2 Interface 页面构建**：简单快速的 Gradio 应用构建
   - **2.3 Blocks 页面构建**：灵活的自定义界面布局
   - **2.4 辅助工具**：State、Textbox 等高级组件使用

### 3. **大模型开发框架（LangChain）的核心组件与运行机制**
   - **3.1 模型调用及提示词模版**：LangChain 核心概念，LLM、提示词工程、模板引擎
   - **3.2 链式调用**：通过 Chain 实现多步骤工作流
   - **3.3 对话记忆**：实现有上下文感知的对话系统
   - **3.4 输出模式**：结构化输出解析，集成 Pydantic

### 4. **检索增强搜索（RAG）应用实战**
   - 理解 RAG 的核心思想：检索 + 生成
   - 使用向量数据库（Chroma）进行文档存储和检索
   - 构建完整的 RAG 管道
   - 前端 Gradio Web 界面集成

### 5. **智能体系统设计与应用实践**
   - **5.1 原生 ReAct Agent**：基础 Agent 实现原理
   - **5.2 旧版 LangChain ReAct Agent**：LangChain 0.x 版本实现
   - **5.3 LangChain V1 ReAct Agent**：最新 LangChain 实现方式
   - **5.4 输出模式**：Agent 结构化输出解析

### 6. **智能体中间件与流程控制实战**
   - **6.1 中间件创建**：自定义中间件开发
   - **6.2 内置中间件**：LangChain 提供的中间件
   - **6.3 智能体记忆**：Agent 的上下文和状态管理
   - **6.4 智能体安全**：安全防护和权限控制

### 7. **复杂任务的智能决策与协作机制**
   - **7.1 RAG Agent**：结合检索和 Agent 的高级应用
   - **7.2 SQL Agent**：数据库查询 Agent
   - **7.3 Search Agent**：网络搜索 Agent
   - **7.4 MCP Agent**：Model Context Protocol Agent
   - **7.5 多智能体应用**：多 Agent 协作系统

### 8. **大模型系统的测试、评估与部署**
   - **8.1 大模型回调实战**：使用回调实现可观测性
   - **8.2 LangSmith Tracing**：系统级别的追踪和调试
   - **8.3 LangSmith Evaluation**：模型输出质量评估
   - **8.4 LangSmith Studio**：可视化开发工具

## 🚀 快速开始

### 前置条件

- Python 3.12 或更高版本
- 需要获取以下大模型 API Key：
  - **百度 AI Studio**：[获取 API Key](https://aistudio.baidu.com/account/accessToken)
  - **阿里云百炼**：[获取 API Key](https://bailian.console.aliyun.com/?tab=model#/api-key)
  - **OpenAI API**（可选）

### 安装步骤

#### 1. 克隆仓库
```bash
git clone https://github.com/your-username/langchain_material_for_baidu_ai-studio.git
cd langchain_material_for_baidu_ai-studio
```

#### 2. 创建虚拟环境（推荐）

**使用 Conda**（推荐）：
```bash
# 使用项目根目录的 environment.yml
conda env create -f environment.yml

# 激活环境
conda activate langchain_2025_12_15
```

**使用 venv**：
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

#### 3. 安装依赖

如果没有使用 Conda 环境文件，可以通过 pip 安装：
```bash
pip install -r requirements.txt
```

#### 4. 配置 API Key

**方式一：环境变量（推荐）**

创建 `.env` 文件或设置系统环境变量：

```bash
# Windows (PowerShell)
$env:OPENAI_API_KEY="your-api-key-here"
$env:DASHSCOPE_API_KEY="your-dashscope-key-here"

# macOS/Linux (bash)
export OPENAI_API_KEY="your-api-key-here"
export DASHSCOPE_API_KEY="your-dashscope-key-here"
```

**方式二：代码中配置**

在 Notebook 或 Python 脚本中：
```python
import os
os.environ["OPENAI_API_KEY"] = "your-api-key-here"
os.environ["DASHSCOPE_API_KEY"] = "your-dashscope-key-here"
```

### 运行 Jupyter Notebook

启动 Jupyter Notebook 服务器：
```bash
jupyter notebook
```

然后在浏览器中打开相应章节的 `.ipynb` 文件进行学习。

## 📖 学习路线建议

### 初级（基础概念）
1. 第 1 章：大语言模型原理与应用基础
2. 第 2 章：智能交互界面开发（2.1-2.2）
3. 第 3 章：LangChain 核心组件（3.1-3.2）

### 中级（实战应用）
4. 第 2 章：Blocks 和辅助工具（2.3-2.4）
5. 第 3 章：记忆和输出模式（3.3-3.4）
6. 第 4 章：RAG 应用实战
7. 第 5 章：Agent 系统（5.1-5.3）

### 高级（系统设计）
8. 第 6 章：中间件与流程控制
9. 第 7 章：复杂任务和多 Agent 协作
10. 第 8 章：测试、评估与部署

## 🛠️ 核心依赖库

| 库 | 版本 | 用途 |
|---|---|---|
| `langchain` | Latest | LLM 应用框架 |
| `openai` | 2.11.0+ | OpenAI 兼容 API 调用 |
| `dashscope` | 1.25.4+ | 阿里云百炼 API 调用 |
| `gradio` | 6.1.0+ | Web UI 构建 |
| `chromadb` | 1.3.7+ | 向量数据库 |
| `beautifulsoup4` | 4.14.3+ | 网页解析 |

完整的依赖列表详见 [requirements.txt](requirements.txt)。

## 💡 常见问题

### Q1: 我应该选择哪个大模型平台？

- **百度 AI Studio**：免费额度充足，国内速度快，特别适合学习
- **阿里云百炼**：功能全面，支持多种模型，生产级别选择
- **OpenAI**：功能最全，国际通用，需要付费

### Q2: 如何在本地运行 Gradio 应用？

每个章节的 `gradio运行代码/` 目录都包含可直接运行的 Gradio 脚本：

```bash
python gradio_script.py
```

然后访问终端输出的 URL（通常是 `http://localhost:7860`）。

### Q3: 我需要学习所有章节吗？

不需要。根据你的目标选择对应章节：
- **只想快速构建 AI 应用**：学习 1、2、3.1-3.2、4 章
- **想深入学习 Agent**：学习 1、3、5、6、7 章
- **想部署生产级应用**：学习 1、3、4、5、7、8 章

### Q4: 如何处理 API 请求超时？

这通常是网络问题。尝试：
1. 检查网络连接
2. 增加超时时间：
```python
from openai import OpenAI
client = OpenAI(timeout=30.0)
```
3. 使用代理（如需要）

### Q5: 向量数据库怎样才能持久化保存？

示例代码：
```python
from chromadb.config import Settings
import chromadb

# 指定持久化路径
settings = Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory="./chroma_data",
    anonymized_telemetry=False,
)
client = chromadb.Client(settings)
```

## 📝 项目结构说明

```
langchain_material_for_baidu_ai-studio/
├── README.md                           # 本文件
├── requirements.txt                    # Python 依赖列表
├── environment.yml                     # Conda 环境文件
├── 1.大语言模型原理与应用基础/
│   ├── 1. 大语言模型调用实战.ipynb
│   └── environment.yml
├── 2.智能交互界面开发实战（Gradio）/
│   ├── 2.1.（选看）函数/
│   ├── 2.2.Interface_页面构建/
│   ├── 2.3.Blocks_页面构建/
│   ├── 2.4.辅助工具/
│   └── environment.yml
├── 3.大模型开发框架（LangChain）的核心组件与运行机制/
│   ├── 3.1.LangChain_模型调用及提示词模版/
│   ├── 3.2.LangChain_链式调用/
│   ├── 3.3.LangChain_对话记忆/
│   ├── 3.4.LangChain_输出模式/
│   └── environment.yml
├── 4.检索增强搜索（RAG）应用实战/
│   ├── 4.LangChain_RAG_应用实战.ipynb
│   ├── gradio运行代码/
│   └── environment.yml
├── 5.智能体系统设计与应用实践/
│   ├── 5.1.原生ReAct_Agent应用开发/
│   ├── 5.2.旧版LangChain_ReAct_Agent应用开发/
│   ├── 5.3.LangChain_V1_ReAct_Agent应用开发/
│   ├── 5.4.LangChain_V1_ReAct_Agent输出模式/
│   └── environment.yml
├── 6.智能体中间件与流程控制实战/
│   ├── 6.1.中间件创建/
│   ├── 6.2.内置中间件/
│   ├── 6.3.智能体记忆/
│   ├── 6.4.智能体安全/
│   └── environment.yml
├── 7.复杂任务的智能决策与协作机制/
│   ├── 7.1.RAG_Agent应用开发/
│   ├── 7.2.SQL_Agent应用开发/
│   ├── 7.3.Search_Agent应用开发/
│   ├── 7.4.MCP_Agent应用开发/
│   ├── 7.5.多智能体应用开发/
│   └── environment.yml
└── 8.大模型系统的测试、评估与部署/
    ├── 8.1.大模型回调实战/
    ├── 8.2.LangSmith_Tracing_实战/
    ├── 8.3.LangSmith_Evaluation_实战/
    ├── 8.4.LangSmith_Studio_实战/
    └── environment.yml
```

每个章节都有独立的 `environment.yml` 和 `requirements.txt`，但建议使用根目录的文件以保证所有依赖兼容。

## 🔗 相关资源

- [LangChain 官方文档](https://python.langchain.com/)
- [Gradio 官方文档](https://www.gradio.app/)
- [OpenAI API 文档](https://platform.openai.com/docs/)
- [百度 AI Studio](https://aistudio.baidu.com/)
- [阿里云百炼](https://bailian.console.aliyun.com/)
- [Chroma 向量数据库文档](https://docs.trychroma.com/)

## 📧 反馈和支持

遇到问题？

1. 检查 [常见问题](#常见问题) 部分
2. 查看对应章节的 Notebook 中的说明
3. 提交 Issue 或 Discussion

## 📄 许可证

本项目的所有代码和教程内容仅供学习使用。

## 🎯 学习成果

完成本课程学习后，你将能够：

✅ 理解大语言模型的基本原理和调用方式  
✅ 使用 Gradio 构建专业的 AI 应用 Web 界面  
✅ 掌握 LangChain 框架的核心组件和最佳实践  
✅ 实现检索增强生成（RAG）系统  
✅ 设计和开发智能体（Agent）系统  
✅ 使用中间件进行流程控制和安全管理  
✅ 构建多 Agent 协作系统  
✅ 对 LLM 应用进行测试、评估和部署  

祝你学习愉快！🚀

# 大语言模型（LLM）应用开发完整教程

<div align="center">

一套**从入门到进阶**的大语言模型应用开发课程库（含完整代码示例与项目实战），覆盖 LLM 应用开发全流程。

![Python](https://img.shields.io/badge/Python-3.12%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)

</div>

---

## 🎯 项目介绍

> 本项目是一套完整的大语言模型（Large Language Models, LLM）应用开发教程，覆盖从基础概念到高级工程实战的系统内容。课程采用**循序渐进**的设计方式，并配套大量可运行示例，帮助开发者快速掌握现代 LLM 应用开发所需的关键技能与工程方法。

### ✨ 你将收获什么？

- 📚 **体系完整**：覆盖 LLM 应用开发全生命周期（构建 → 工具集成 → 多智能体 → 评估与部署）
- 🔍 **深入理解**：掌握 Transformer 架构、Prompt Engineering 等核心技术
- 🏗️ **动手实践**：从零构建 LLM 应用，涵盖 RAG、Agent 等前沿技术
- 🚀 **开箱即用**：提供 Conda / Pip 两套环境配置，降低上手成本

---

## 📖 内容导航

| 章节 | 关键内容 | 状态 |
| --- | --- | --- |
| [第 1 章：大语言模型应用基础](./1.大语言模型应用基础/) | 掌握 LLM 的核心概念与基本应用模式 | ✅ |
| [第 2 章：智能交互界面开发实战（Gradio）](./2.智能交互界面开发实战（Gradio）/) | 学习用 Gradio 构建交互式 LLM 应用 | ✅ |
| [第 3 章：LangChain 核心组件与运行机制](./3.大模型开发框架（LangChain）的核心组件与运行机制/) | 深入理解 LangChain 的关键抽象与工程组织 | ✅ |
| [第 4 章：检索增强生成（RAG）应用实战](./4.检索增强搜索（RAG）应用实战/) | 构建完整 RAG 流程并掌握关键工程细节 | ✅ |
| [第 5 章：智能体系统设计与应用实践](./5.智能体系统设计与应用实践/) | 从零构建智能体，掌握工具调用与部署 | ✅ |
| [第 6 章：智能体中间件与流程控制实战](./6.智能体中间件与流程控制实战/) | 掌握中间件机制、记忆管理与安全策略 | ✅ |
| [第 7 章：智能体工具能力进阶](./7.智能体工具能力进阶/) | 扩展智能体工具箱，集成 RAG、SQL 等工具 | ✅ |
| [第 8 章：多智能体系统构建](./8.多智能体系统构建/) | 构建多智能体协作架构与实践 | ✅ |
| [第 9 章：大模型系统的测试、评估与部署](./9.大模型系统的测试、评估与部署/) | 面向生产质量的测试、评估与部署实践 | ✅ |

---

## 🚀 快速开始

### 环境配置（Conda，推荐）

```bash
# 1) 克隆仓库
git clone <your-repo-url>
cd <your-repo-name>

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

## 📦 依赖说明

| 库                   |     版本 | 说明             |
| ------------------- | -----: | -------------- |
| LangChain           |  1.2.0 | LLM 应用开发框架     |
| Gradio              |  6.2.0 | Web UI 构建      |
| Chroma              |  1.4.0 | 向量数据库          |
| OpenAI              | 2.11.0 | OpenAI API 客户端 |

完整依赖请查看：[requirements.txt](requirements.txt)

---

## 🤝 如何贡献

我们欢迎任何形式的贡献！

- 🐛 **报告 Bug** - 发现问题请提交 Issue
- 💡 **功能建议** - 有好想法就告诉我们
- 📝 **内容完善** - 帮助改进教程内容
- 🔧 **代码优化** - 提交 Pull Request

---

## 🙏 致谢

感谢以下团队与社区对本项目的支持：

- **机智流**
- **百度飞桨星河社区（AI Studio）**
- **LangChain 团队**
- **Gradio 团队**

---

## 📜 开源协议

本项目基于 **MIT License** 开源，详见 [LICENSE](LICENSE)。
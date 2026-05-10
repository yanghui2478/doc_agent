# AI Document Agent

基于 RAG（检索增强生成）的 AI 文档智能体。

支持 PDF 上传、文档解析、智能问答、自动摘要等功能，能够基于文档内容进行上下文问答与信息检索。

---

# 🚀 功能特性

- 📄 PDF 文档上传
- 🧠 基于 RAG 的智能问答
- 🔍 文档向量检索（FAISS）
- 🤖 大模型回答生成（DashScope / 通义千问）
- 📌 自动文档摘要
- 💬 多轮聊天界面
- ✨ Markdown 渲染
- ⏳ AI思考等待提示
- 📝 本地聊天记录保存

---

# 🛠 技术栈

## 后端

- Python
- FastAPI
- Sentence-Transformers
- FAISS
- PyMuPDF

## 前端

- HTML
- CSS
- JavaScript

## AI能力

- RAG（检索增强生成）
- DashScope API（通义千问）

---

# 📂 项目结构

```bash
doc_agent/
│
├── main.py
├── rag.py
├── pdf_reader.py
├── requirements.txt
├── Procfile
│
├── uploads/
│
└── static/
    └── index.html

---

#⚙️ 本地运行
1. 安装依赖
pip install -r requirements.txt
2. 配置 API KEY

在 main.py 中配置：

API_KEY = "你的API_KEY"
3. 启动项目
python -m uvicorn main:app --reload
4. 打开网页

浏览器访问：

http://127.0.0.1:8000

---

#🎯 核心功能演示
文档上传

用户上传 PDF 文档后：

自动解析文本
自动构建向量索引
自动生成文档摘要
智能问答

系统通过：

文档检索
向量召回
Prompt 拼接
大模型生成

实现基于文档内容的精准问答。

---


#📌 后续优化方向
多文档知识库
文档来源引用
LangChain Agent
多用户会话
Docker 部署
云端向量数据库

---

#👨‍💻 作者

杨晖

GitHub：
yanghui2478

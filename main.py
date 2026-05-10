from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil
import requests
from fastapi.responses import FileResponse
@app.get("/")
async def home():
    return FileResponse("static/index.html")
from pdf_reader import read_pdf
from rag import build_index, search

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY = "sk-5b0adfd00d464404990b52ff2bf65997"

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = read_pdf(file_path)

    build_index(text)

    return {"message": "PDF上传成功"}

@app.post("/ask")
async def ask(question: str):

    context = search(question)

    prompt = f"""
根据以下内容回答问题：

{context}

问题：
{question}
"""

    response = requests.post(
        "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "qwen-plus",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
    )

    result = response.json()

    answer = result["choices"][0]["message"]["content"]

    return {
    "answer": answer,
    "context": context
}
@app.post("/summary")
async def summary():

    prompt = f"""
请总结这份文档的内容。

要求：

1. 文档主题
2. 核心内容
3. 关键结论
4. 风险点（如果有）

内容：

{search("总结全文")}
"""

    response = requests.post(
        "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "qwen-plus",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
    )

    result = response.json()

    print(result)

    answer = result["choices"][0]["message"]["content"]

    return {"summary": answer}
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from typing import List
from app.pdf_utils import extract_text_chunks
from app.embed_utils import generate_embeddings
from app.vector_db import VectorDB
from app.rag import answer_query
import os

app = FastAPI()
vector_db = VectorDB()
UPLOAD_DIR = "data"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/upload_pdf/")
def upload_pdf(files: List[UploadFile] = File(...)):
    total_chunks = 0
    for file in files:
        filepath = os.path.join(UPLOAD_DIR, file.filename)
        with open(filepath, "wb") as f:
            f.write(file.file.read())
        chunk_pairs = extract_text_chunks(filepath)  # List[(text, meta)]
        embeddings = generate_embeddings(chunk_pairs)
        vector_db.add_documents(chunk_pairs, embeddings, file.filename)
        total_chunks += len(chunk_pairs)
    return {"status": "success", "chunks": total_chunks}

@app.post("/query/")
def query_pdf(query: str = Form(...), top_k: int = Form(5)):
    results = vector_db.search(query, top_k=top_k)
    answer, context = answer_query(query, results)
    return JSONResponse({"answer": answer, "context": context, "sources": results})

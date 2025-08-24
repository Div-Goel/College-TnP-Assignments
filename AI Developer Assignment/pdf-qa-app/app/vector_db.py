import faiss
import numpy as np
from app.embed_utils import embed_query, EMBED_DIM
import pickle
import os

class VectorDB:
    def __init__(self, index_path="data/faiss.index", meta_path="data/meta.pkl"):
        self.index_path = index_path
        self.meta_path = meta_path
        self.index = None
        self.chunks = []  # list[str]
        self.metadatas = []  # list[dict]
        self.load()

    def add_documents(self, chunks, embeddings, pdf_name):
        # Ensure index is initialized
        if self.index is None:
            self.index = faiss.IndexFlatL2(EMBED_DIM)
        self.index.add(np.array(embeddings))
        for i, item in enumerate(chunks):
            text, meta = (item if isinstance(item, (list, tuple)) else (item, {}))
            meta = meta or {}
            meta.update({"pdf": pdf_name, "chunk_id": len(self.chunks)})
            self.chunks.append(text)
            self.metadatas.append(meta)
        self.save()

    def search(self, query, top_k=5):
        if self.index is None or len(self.chunks) == 0:
            return []
        q_emb = embed_query(query)
        D, I = self.index.search(np.array([q_emb]), top_k)
        results = []
        for score, idx in zip(D[0], I[0]):
            if idx == -1:
                continue
            results.append({
                "text": self.chunks[idx],
                "metadata": self.metadatas[idx],
                "score": float(score)
            })
        return results

    def save(self):
        if self.index is not None:
            faiss.write_index(self.index, self.index_path)
        with open(self.meta_path, "wb") as f:
            pickle.dump((self.chunks, self.metadatas), f)

    def load(self):
        if os.path.exists(self.index_path):
            try:
                self.index = faiss.read_index(self.index_path)
            except Exception:
                self.index = None
        else:
            self.index = None
        if os.path.exists(self.meta_path):
            try:
                with open(self.meta_path, "rb") as f:
                    self.chunks, self.metadatas = pickle.load(f)
            except Exception:
                self.chunks, self.metadatas = [], []
        else:
            self.chunks, self.metadatas = [], []

from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')
EMBED_DIM = model.get_sentence_embedding_dimension()

def generate_embeddings(chunks):
    # chunks can be list of str or list of (text, meta)
    texts = [c[0] if isinstance(c, (list, tuple)) else c for c in chunks]
    return np.array(model.encode(texts, normalize_embeddings=True), dtype='float32')

def embed_query(query):
    return np.array(model.encode([query], normalize_embeddings=True)[0], dtype='float32')

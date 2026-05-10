from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

chunks = []
index = None

def split_text(text, chunk_size=300):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def build_index(text):
    global chunks, index

    chunks = split_text(text)

    embeddings = model.encode(chunks)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings))

def search(query):
    query_embedding = model.encode([query])

    D, I = index.search(np.array(query_embedding), k=3)

    results = [chunks[i] for i in I[0]]

    return "\n".join(results)
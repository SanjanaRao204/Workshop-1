import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

class Retriever:
    def __init__(self, file_path):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.texts = self.load_data(file_path)
        self.index = self.build_index()

    def load_data(self, file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return [line.strip() for line in f.readlines()]

    def build_index(self):
        embeddings = self.model.encode(self.texts)
        dimension = embeddings.shape[1]

        index = faiss.IndexFlatL2(dimension)
        index.add(np.array(embeddings))

        self.embeddings = embeddings
        return index

    def retrieve(self, query, k=2):
        query_embedding = self.model.encode([query])
        distances, indices = self.index.search(np.array(query_embedding), k)
        return [self.texts[i] for i in indices[0]]
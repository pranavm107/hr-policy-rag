"""Step 4: store chunk embeddongs in FAISS so we ca search them"""

import os
from langchain_community.vectorstores import FAISS
from hr_assistant import config
from hr_assistant.embeddings import get_embedding_model

# build_vector_store using FAISS

def build_vector_store(chunks):
    """
    Embed every chunk and build
    a searchable FAISS index in memore."""
    embeddings_model = get_embedding_model()
    return FAISS.from_documents(chunks, embeddings_model) # this function convert the text into numbers


# whatever we index we create it need to store
## save vector store

def save_vector_store(vector_store, path : str = config.VECTOR_STORE_PATH):
    """Save the FAISSMindex to disk
    so we don't have to rebuild it every time."""
    vector_store.save_local(path)


def load_vector_store(path : str = config.VECTOR_STORE_PATH):
    """Load a previosuly saved FAISS index from disk"""
    embedding_model = get_embedding_model()
    # allow_dangerous_deserialization is safe here because we only ever load 
    # an index that this same app created and saved
    return FAISS.load_local(path, embedding_model, allow_dangerous_deserialization=True) # our llm need this load_local method

def vector_store_exists(path: str = config.VECTOR_STORE_PATH) -> bool:
    """check if a saved FAISS index already on disk."""
    return os.path.exists(os.path.join(path, "index.faiss"))

def get_retriever(vector_store, k: int = config.TOP_K_DOCUMENTS): #it results retriver
    """Turn a vector store into a retriever that returns the top-k matching chunks"""
    return vector_store.as_retriever(search_kwargs={"k" : k})

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
    return FAISS.from_documents(chunks, embedding_model) # this function convert the text into numbers


# whatever we index we create it need to store
## save vector store

def save_vector_store(vector_store, path : str = config.VECTOR_STORE_PATH):
    vector_store.save_local(path)


def load_vector_store(path : str = config.VECTOR_STORE_PATH
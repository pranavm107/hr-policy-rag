"""Step 3: turn text into numbers (vecotrs) using Jina """

from langchain_community.embeddings import JinaEmbeddings

from hr_assistant import config

def get_embedding_model():
    """
    Return Jina Embeddings model
    Reads JINA_API_KEY from environment variables.
    """
    return JinaEmbeddings(
        model_name=config.EMBEDDING_MODEL_NAME,
        api_key=config.JINA_API_KEY
    )
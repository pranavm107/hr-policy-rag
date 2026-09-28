# We write a logic from the data

"""Step 1: read the raw document from the data folder."""

from langchain_community.document_loaders import TextLoader
from hr_assistant import config

def load_document(file_path: str = config.DATA_FILE_PATH):
    """Load a .txt file and return it as a list of Langchain Document objects."""

    lodaer = TextLoader(file_path, encoding="utf-8") #utf for computer understand

    return loader.load()
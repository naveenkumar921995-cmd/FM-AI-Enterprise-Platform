import os

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

DB_PATH = "vectorstore"

embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)


def load_vectorstore():

    if os.path.exists(DB_PATH):

        return FAISS.load_local(
            DB_PATH,
            embeddings,
            allow_dangerous_deserialization=True
        )

    return None


def save_vectorstore(vs):

    vs.save_local(DB_PATH)

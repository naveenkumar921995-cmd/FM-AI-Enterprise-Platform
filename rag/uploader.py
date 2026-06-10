from rag.loader import load_documents
from rag.chunker import split_documents
from rag.retriever import create_vectorstore


def process_new_document():

    docs = load_documents()

    chunks = split_documents(docs)

    create_vectorstore(chunks)

    return "Knowledge base updated"

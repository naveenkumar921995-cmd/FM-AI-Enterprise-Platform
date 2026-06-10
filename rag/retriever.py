import chromadb

from langchain_chroma import Chroma

from rag.embeddings import get_embeddings


DB_PATH = "vectorstore"


def create_vectorstore(chunks):

    embeddings = get_embeddings()

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=DB_PATH
    )

    vectordb.persist()

    print("Vector database created")


def load_vectorstore():

    embeddings = get_embeddings()

    vectordb = Chroma(
        persist_directory=DB_PATH,
        embedding_function=embeddings
    )

    return vectordb


def retrieve_documents(query, k=5):

    vectordb = load_vectorstore()

    docs = vectordb.similarity_search(
        query=query,
        k=k
    )

    return docs
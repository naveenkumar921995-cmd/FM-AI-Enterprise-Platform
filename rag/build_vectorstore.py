from rag.loader import load_documents
from rag.chunker import split_documents
from rag.retriever import create_vectorstore


def main():

    docs = load_documents()

    chunks = split_documents(docs)

    create_vectorstore(chunks)

    print("Vectorstore created successfully")


if __name__ == "__main__":
    main()
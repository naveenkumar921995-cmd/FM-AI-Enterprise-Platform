from langchain_community.document_loaders import PyPDFLoader

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from langchain_community.vectorstores import FAISS

from rag.vectorstore_manager import (
    embeddings,
    load_vectorstore,
    save_vectorstore
)


def process_pdf(pdf_path):

    loader = PyPDFLoader(pdf_path)

    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(
        documents
    )

    existing_db = load_vectorstore()

    if existing_db:

        existing_db.add_documents(
            chunks
        )

        save_vectorstore(existing_db)

    else:

        db = FAISS.from_documents(
            chunks,
            embeddings
        )

        save_vectorstore(db)

    return len(chunks)

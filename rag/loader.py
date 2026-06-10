import os

from langchain_community.document_loaders import PyPDFLoader


DATA_PATH = "data"


def load_documents():

    documents = []

    for system in os.listdir(DATA_PATH):

        system_path = os.path.join(DATA_PATH, system)

        if os.path.isdir(system_path):

            for file in os.listdir(system_path):

                if file.endswith(".pdf"):

                    file_path = os.path.join(system_path, file)

                    loader = PyPDFLoader(file_path)

                    pages = loader.load()

                    for page in pages:

                        page.metadata.update(
                            {
                                "system": system,
                                "source_file": file,
                                "page_number": page.metadata.get("page", 0)
                            }
                        )

                    documents.extend(pages)

    return documents
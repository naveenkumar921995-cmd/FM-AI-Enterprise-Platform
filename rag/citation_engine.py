def build_citations(docs):

    citations = []

    for doc in docs:

        citations.append({
            "file":
                doc.metadata.get("source_file"),

            "page":
                doc.metadata.get("page_number")
        })

    return citations

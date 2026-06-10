def build_citations(docs):

    citations = []

    for doc in docs:

        citations.append(
            {
                "file":
                    doc.metadata.get(
                        "source_file",
                        "Unknown"
                    ),

                "page":
                    doc.metadata.get(
                        "page",
                        "N/A"
                    )
            }
        )

    return citations

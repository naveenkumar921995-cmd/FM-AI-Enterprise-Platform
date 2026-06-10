from rag.retriever import retrieve_documents


def fire_agent(query):

    docs = retrieve_documents(query)

    sources = []

    answer = []

    for doc in docs[:3]:

        answer.append(doc.page_content[:500])

        sources.append({
            "file": doc.metadata.get("source_file"),
            "page": doc.metadata.get("page_number")
        })

    return {
    "agent": "Fire Agent",
    "answer": "\n".join(answer),
    "sources": sources,
    "recommendation":
        "Check fire alarm panel logs, detector status, loop communication and field device connectivity."
}
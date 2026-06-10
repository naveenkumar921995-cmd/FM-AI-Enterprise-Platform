from rag.retriever import retrieve_documents
from backend.llm import llm


def hvac_agent(query):

    docs = retrieve_documents(query)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
You are a senior HVAC engineer.

Answer using only the provided context.

Context:
{context}

Question:
{query}
"""

    response = llm.invoke(prompt)

    sources = []

    for doc in docs:

        sources.append({
            "file": doc.metadata.get("source_file"),
            "page": doc.metadata.get("page_number")
        })

    return {
        "agent": "HVAC Agent",
        "answer": response.content,
        "sources": sources,
        "recommendation":
            "Follow OEM maintenance procedures before escalation."
    }
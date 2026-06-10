from rag.retriever import retrieve_documents
from backend.llm import llm


def electrical_agent(query):

    docs = retrieve_documents(query)

    context = "\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
You are a senior electrical engineer.

Context:
{context}

Question:
{query}
"""

    response = llm.invoke(prompt)

    return {
        "agent": "Electrical Agent",
        "answer": response.content,
        "sources": [],
        "recommendation":
            "Check relay indications and electrical protection logs."
    }
from rag.retriever import retrieve_documents
from rag.citation_engine import build_citations

from backend.llm import llm


def hvac_agent(query):

    docs = retrieve_documents(query)

    citations = build_citations(docs)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
You are a senior HVAC engineer.

Answer only using the provided context.

Context:
{context}

Question:
{query}
"""

    response = llm.invoke(prompt)

    return {
        "agent": "HVAC Agent",
        "answer": response.content,
        "citations": citations,
        "recommendation":
            "Follow OEM maintenance procedures before escalation."
    }

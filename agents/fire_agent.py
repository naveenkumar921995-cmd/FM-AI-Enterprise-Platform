from rag.retriever import retrieve_documents
from rag.citation_engine import build_citations

from backend.llm import llm


def fire_agent(query):

    # Retrieve relevant documents
    docs = retrieve_documents(query)

    # Build citations
    citations = build_citations(docs)

    # Prepare context
    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    # Hallucination-safe prompt
    prompt = f"""
You are a Senior Fire and Life Safety Engineer.

Rules:
1. Answer ONLY from the provided context.
2. If the answer is not available in the context, respond:
   "Information not found in uploaded documents."
3. Do not make assumptions.
4. Provide troubleshooting steps when applicable.
5. Keep the response professional and concise.

Context:
{context}

Question:
{query}
"""

    # Generate response
    response = llm.invoke(prompt)

    return {
        "agent": "Fire Agent",
        "answer": response.content,
        "citations": citations,
        "recommendation":
            "Check fire alarm panel logs, detector health, loop communication and field device status before escalation."
    }

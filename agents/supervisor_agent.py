from backend.llm import llm


def route_query(query):

    prompt = f"""
Classify this Facility Management query.

Categories:

HVAC
Electrical
Fire
Vendor
Incident
SQL

Query:
{query}

Return only category name.
"""

    response = llm.invoke(prompt)

    return response.content.strip().lower()

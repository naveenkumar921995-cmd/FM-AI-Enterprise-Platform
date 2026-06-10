from backend.llm import llm


def route_query(query):

    prompt = f"""
Classify the following facility management query.

Possible categories:

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

    category = response.content.strip().lower()

    return category

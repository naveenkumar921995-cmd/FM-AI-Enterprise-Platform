from backend.llm import llm

from agents.hvac_agent import hvac_agent
from agents.electrical_agent import electrical_agent
from agents.fire_agent import fire_agent
from agents.sql_agent import sql_agent


def route_query(query):

    query_lower = query.lower()

    # SQL Agent Routing
    sql_keywords = [
        "asset",
        "assets",
        "work order",
        "work orders",
        "incident",
        "incidents",
        "vendor",
        "vendors",
        "show",
        "list",
        "count",
        "how many"
    ]

    for keyword in sql_keywords:

        if keyword in query_lower:
            return "sql"

    # FM Domain Classification

    prompt = f"""
Classify this Facility Management query.

Categories:
HVAC
Electrical
Fire

Query:
{query}

Return only category name.
"""

    response = llm.invoke(prompt)

    return response.content.strip().lower()


def supervisor_agent(query):

    category = route_query(query)

    if category == "sql":
        return sql_agent(query)

    elif "hvac" in category:
        return hvac_agent(query)

    elif "electrical" in category:
        return electrical_agent(query)

    elif "fire" in category:
        return fire_agent(query)

    else:

        return {
            "agent": "Supervisor Agent",
            "answer": "Unable to determine appropriate FM domain.",
            "recommendation":
                "Please specify HVAC, Electrical, Fire, Asset, Work Order, Vendor or Incident related query."
        }
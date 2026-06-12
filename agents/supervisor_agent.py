from backend.llm import llm

from agents.hvac_agent import hvac_agent
from agents.electrical_agent import electrical_agent
from agents.fire_agent import fire_agent


def route_query(query):

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

    if "hvac" in category:
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
                "Please specify HVAC, Electrical or Fire related query."
        }

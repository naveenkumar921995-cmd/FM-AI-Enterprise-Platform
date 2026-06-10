from typing import TypedDict

from langgraph.graph import (
    StateGraph,
    END
)

from agents.supervisor_agent import route_query

from agents.hvac_agent import hvac_agent
from agents.electrical_agent import electrical_agent
from agents.fire_agent import fire_agent
from agents.vendor_agent import vendor_agent
from agents.incident_agent import incident_agent
from agents.sql_agent import sql_agent


class FMState(TypedDict):

    query: str
    response: dict


def supervisor_node(state):

    query = state["query"]

    route = route_query(query)

    return {
        "query": query,
        "route": route
    }


def route_node(state):

    query = state["query"]

    route = state["route"]

    if route == "hvac":
        result = hvac_agent(query)

    elif route == "electrical":
        result = electrical_agent(query)

    elif route == "fire":
        result = fire_agent(query)

    elif route == "vendor":
        result = vendor_agent(query)

    elif route == "incident":
        result = incident_agent(query)

    elif route == "sql":
        result = sql_agent(query)

    else:

        result = {
            "answer":
                "No matching agent found."
        }

    return {
        "query": query,
        "response": result
    }


graph = StateGraph(dict)

graph.add_node(
    "supervisor",
    supervisor_node
)

graph.add_node(
    "route",
    route_node
)

graph.set_entry_point(
    "supervisor"
)

graph.add_edge(
    "supervisor",
    "route"
)

graph.add_edge(
    "route",
    END
)

app_graph = graph.compile()


def run_graph(query):

    result = app_graph.invoke(
        {"query": query}
    )

    return result["response"]
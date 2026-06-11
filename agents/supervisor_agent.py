from agents.hvac_agent import hvac_agent
from agents.electrical_agent import electrical_agent
from agents.fire_agent import fire_agent
from agents.vendor_agent import vendor_agent
from agents.incident_agent import incident_agent


def route_query(query):

    q = query.lower()

    if any(word in q for word in [
        "ahu",
        "chiller",
        "hvac",
        "cooling",
        "air conditioning"
    ]):
        return "hvac"

    elif any(word in q for word in [
        "electrical",
        "ups",
        "dg",
        "transformer",
        "power"
    ]):
        return "electrical"

    elif any(word in q for word in [
        "fire",
        "smoke",
        "alarm",
        "sprinkler"
    ]):
        return "fire"

    elif any(word in q for word in [
        "vendor",
        "contract",
        "amc"
    ]):
        return "vendor"

    elif any(word in q for word in [
        "incident",
        "breakdown",
        "fault"
    ]):
        return "incident"

    return "hvac"


def supervisor_agent(query):

    category = route_query(query)

    if category == "hvac":
        return hvac_agent(query)

    elif category == "electrical":
        return electrical_agent(query)

    elif category == "fire":
        return fire_agent(query)

    elif category == "vendor":
        return vendor_agent(query)

    elif category == "incident":
        return incident_agent(query)

    return {
        "agent": "Supervisor",
        "answer": "No suitable agent found."
    }

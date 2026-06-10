def route_query(query: str):

    query = query.lower()

    hvac_keywords = [
        "ahu",
        "fcu",
        "chiller",
        "vrf",
        "cooling tower",
        "compressor",
        "hvac"
    ]

    electrical_keywords = [
        "ups",
        "transformer",
        "dg",
        "vfd",
        "electrical",
        "lt panel",
        "ht panel"
    ]

    fire_keywords = [
        "fire",
        "sprinkler",
        "hydrant",
        "fire alarm",
        "detector"
    ]

    vendor_keywords = [
        "vendor",
        "amc",
        "warranty",
        "contract"
    ]

    incident_keywords = [
        "incident",
        "accident",
        "near miss",
        "leakage",
        "water leakage"
    ]

    sql_keywords = [
        "show",
        "list",
        "count",
        "how many",
        "report"
    ]

    for word in hvac_keywords:
        if word in query:
            return "hvac"

    for word in electrical_keywords:
        if word in query:
            return "electrical"

    for word in fire_keywords:
        if word in query:
            return "fire"

    for word in vendor_keywords:
        if word in query:
            return "vendor"

    for word in incident_keywords:
        if word in query:
            return "incident"

    for word in sql_keywords:
        if word in query:
            return "sql"

    return "general"
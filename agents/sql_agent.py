def sql_agent(query):

    query = query.lower()

    if "open work orders" in query:

        sql = """
        SELECT *
        FROM work_orders
        WHERE status='Open'
        """

    elif "hvac complaints" in query:

        sql = """
        SELECT *
        FROM complaints
        WHERE system='HVAC'
        """

    else:

        sql = "Query not recognised"

    return {
    "agent": "SQL Agent",
    "answer": "SQL query generated successfully.",
    "generated_sql": sql,
    "sources": [],
    "recommendation":
        "Review query results and validate records before reporting."
}
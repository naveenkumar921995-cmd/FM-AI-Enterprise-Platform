from sqlalchemy import text
from database.db import engine


def sql_agent(query):

    query = query.lower()

    if "open work order" in query:

        sql = """
        SELECT *
        FROM work_orders
        WHERE status='Open'
        """

    elif "closed work order" in query:

        sql = """
        SELECT *
        FROM work_orders
        WHERE status='Closed'
        """

    elif "critical incident" in query:

        sql = """
        SELECT *
        FROM incidents
        WHERE severity='Critical'
        """

    elif "vendor" in query:

        sql = """
        SELECT *
        FROM vendors
        """

    elif "asset" in query:

        sql = """
        SELECT *
        FROM assets
        """

    else:

        sql = """
        SELECT *
        FROM work_orders
        LIMIT 20
        """

    with engine.connect() as conn:

        result = conn.execute(
            text(sql)
        )

        rows = result.fetchall()

    return {
        "agent": "SQL Agent",
        "answer": f"Found {len(rows)} records",
        "rows": [
            dict(r._mapping)
            for r in rows
        ]
    }
from sqlalchemy import text
from database.db import engine


def sql_agent(query):

    q = query.lower()

    if "asset" in q:

        sql = "SELECT * FROM assets LIMIT 50"

    elif "incident" in q:

        sql = "SELECT * FROM incidents LIMIT 50"

    elif "vendor" in q:

        sql = "SELECT * FROM vendors LIMIT 50"

    elif "work order" in q:

        sql = "SELECT * FROM work_orders LIMIT 50"

    else:

        sql = "SELECT * FROM work_orders LIMIT 20"

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
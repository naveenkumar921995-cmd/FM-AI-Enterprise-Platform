from sqlalchemy import text
from database.db import engine


def sql_agent(query):

    sql = """
    SELECT *
    FROM work_orders
    """

    with engine.connect() as conn:

        result = conn.execute(
            text(sql)
        )

        rows = result.fetchall()

    return {
        "agent": "SQL Agent",
        "rows": [dict(r._mapping) for r in rows]
    }

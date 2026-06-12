import sqlite3
import pandas as pd

conn = sqlite3.connect("database/fm.db")

assets = pd.read_csv("data/assets.csv")
work_orders = pd.read_csv("data/work_orders.csv")
incidents = pd.read_csv("data/incidents.csv")
vendors = pd.read_csv("data/vendors.csv")

assets.to_sql(
    "assets",
    conn,
    if_exists="replace",
    index=False
)

work_orders.to_sql(
    "work_orders",
    conn,
    if_exists="replace",
    index=False
)

incidents.to_sql(
    "incidents",
    conn,
    if_exists="replace",
    index=False
)

vendors.to_sql(
    "vendors",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("Database Created Successfully")

import pandas as pd
import random

systems = [
    "HVAC",
    "Electrical",
    "Fire"
]

records = []

for i in range(1, 1001):

    records.append({
        "wo_id": f"WO-{i:05}",
        "system": random.choice(systems),
        "priority": random.choice(
            ["Low", "Medium", "High"]
        ),
        "status": random.choice(
            ["Open", "In Progress", "Closed"]
        ),
        "assigned_to": random.choice(
            ["Team A", "Team B", "Team C"]
        )
    })

df = pd.DataFrame(records)

df.to_csv(
    "data/work_orders.csv",
    index=False
)

print("1000 Work Orders Generated")

import pandas as pd
import random

systems = [
    "HVAC",
    "Electrical",
    "Fire"
]

records = []

for i in range(1, 301):

    records.append({
        "incident_id": f"INC-{i:04}",
        "system": random.choice(systems),
        "severity": random.choice(
            [
                "Low",
                "Medium",
                "High",
                "Critical"
            ]
        ),
        "status": random.choice(
            ["Open", "Closed"]
        )
    })

df = pd.DataFrame(records)

df.to_csv(
    "data/incidents.csv",
    index=False
)

print("300 Incidents Generated")

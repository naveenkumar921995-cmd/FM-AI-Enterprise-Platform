import pandas as pd
import random

systems = [
    "HVAC",
    "Electrical",
    "Fire",
    "Lift",
    "STP",
    "WTP"
]

locations = [
    "Tower A",
    "Tower B",
    "Basement",
    "Plant Room",
    "Roof",
    "Parking"
]

records = []

for i in range(1, 501):

    system = random.choice(systems)

    records.append({
        "asset_id": f"AST-{i:04}",
        "asset_name": f"{system} Asset {i}",
        "system": system,
        "location": random.choice(locations),
        "status": random.choice(
            ["Running", "Stopped", "Maintenance"]
        ),
        "health_score": random.randint(70, 100)
    })

df = pd.DataFrame(records)

df.to_csv(
    "data/assets.csv",
    index=False
)

print("500 Assets Generated")

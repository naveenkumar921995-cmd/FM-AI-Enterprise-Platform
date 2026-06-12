import pandas as pd

vendors = []

for i in range(1, 51):

    vendors.append({
        "vendor_id": f"VEN-{i:03}",
        "vendor_name": f"Vendor {i}",
        "service_type":
            [
                "HVAC",
                "Electrical",
                "Fire"
            ][i % 3],
        "contact":
            f"98765{i:05}"
    })

df = pd.DataFrame(vendors)

df.to_csv(
    "data/vendors.csv",
    index=False
)

print("50 Vendors Generated")

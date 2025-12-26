import requests

api_url = "http://mis.sunbeaminfo.com/api/CampusApi/GetBatchwisePlacement"

response = requests.get(api_url)
print("Status:", response.status_code)

data = response.json()

print("\n--- Internship / Batch (Placement) Information ---\n")

for row in data:
    print(
        row.get("BatchName", ""),
        "| K-DAC:", row.get("K-DAC", ""),
        "| DAC:", row.get("DAC", ""),
        "| WiMC/DMC:", row.get("WiMC-DMC", ""),
        "| DiVESD/DESD:", row.get("DiVESD-DESD", ""),
        "| DBDA:", row.get("DBDA", ""),
        "| DITISS:", row.get("DITISS", "")
    )

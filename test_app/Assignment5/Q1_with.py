import requests
from bs4 import BeautifulSoup

url = "https://www.sunbeaminfo.com/placements"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
print("Status:", response.status_code)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    print("\n--- Internship / Batch Information ---\n")

    # 1️⃣ Extract headings (Internship / Batch titles)
    headings = soup.find_all(["h3", "h4"])

    for h in headings:
        text = h.get_text(strip=True)
        if "Intern" in text or "Batch" in text or "Training" in text:
            print("▶", text)

    print("\n--- Batch Tables ---\n")

    # 2️⃣ Extract tables (batch schedules)
    tables = soup.find_all("table")

    for table in tables:
        rows = table.find_all("tr")
        for row in rows:
            cols = row.find_all(["td", "th"])
            data = [c.get_text(strip=True) for c in cols]
            if data:
                print(" | ".join(data))
        print("-" * 50)

else:
    print("Failed to fetch page")

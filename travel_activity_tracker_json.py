from tracker import travel_data
from datetime import datetime
import json

records = [
    travel_data("India", "discovering the beauty of India", "27-05-2025"),
    travel_data("Italy", "exploring the historic sites of Italy", "23-10-2023"),
    travel_data("Japan", "experiencing the culture of Japan", "10-02-2024")
]
print(records)
for x in records:
    date_obj = datetime.strptime(x["date"], "%d-%m-%Y")
    x["date"] = date_obj.strftime("%B %d, %Y")

json_data = json.dumps(records, indent=4)
print("JSON data: " ,json_data)

parsed_json = json.loads(json_data)
print("Parsed JSON data: ")
for x in parsed_json:
    print(x)
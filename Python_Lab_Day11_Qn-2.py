from tracker import travel_data
from datetime import datetime
import json

records = [
    travel_data("India", "Delhi", "discovering the beauty of India"),
    travel_data("Italy", "Rome", "exploring the historic sites of Italy"),
    travel_data("Japan", "Tokyo", "experiencing the culture of Japan")
]

for x in records:
    date_obj = datetime.strptime(x["date"], "%d-%m-%y")
    x["date"] = date_obj.strftime("%B %d, %Y")

json_data = json.dumps(x, indent=4)
print("JSON data: " ,json_data)

parsed_json = jso.loads(json_data)
print("Parsed JSON data: ")
for x in parsed_json:
    print(x)
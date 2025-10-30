from tracker import travel_data
from datetime import datetime
import json

records = [
    travel_data("India", "discovering the beauty of India", "10-02-25"),
    travel_data("Italy", "exploring the historic sites of Italy", "10-02-26"),
    travel_data("Japan", "experiencing the culture of Japan", "10-02-27")
]

for x in records:
    date_obj = datetime.strptime(x["date"], "%d-%m-%y")
    x["date"] = date_obj.strftime("%B %d, %Y")

json_data = json.dumps(x, indent=4)
print("JSON data: " ,json_data)

parsed_json = json.loads(json_data)
print("Parsed JSON data: ")
for x in parsed_json:
    print(x)
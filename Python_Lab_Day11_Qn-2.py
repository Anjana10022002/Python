from tracker import travel_data
import datetime
import json

records = [
    travel_data("India", "Delhi", "discovering the beauty of India"),
    travel_data("Italy", "Rome", "exploring the historic sites of Italy"),
    travel_data("Japan", "Tokyo", "experiencing the culture of Japan")
]

for x in records:
    date_obj = datetime.strptime(x["date"], "%d-%m-%y")
    x["date"] = date_obj.strftime("%B %d, %Y")


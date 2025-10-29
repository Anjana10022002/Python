from tripdata import trip_details
from datetime import datetime
import json

trips = [
    trip_details("India", "10-02-2025", "discovering the beauty of India"),
    trip_details("Italy", "15-03-2025", "exploring the historic sites of Italy"),
    trip_details("Japan", "20-04-2025", "experiencing the culture of Japan")
]

for x in trips:
    d = datetime.datetime.strptime(x["date"], "%d-%m-%y")
    x["date"] = d.strftime("%B %d %y")
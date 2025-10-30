import re
import sys

title = input("Enter the book title: ")
year = input("Enter the publication year: ")

pattern = '^[a-zA-Z ]+$'
result = re.search(pattern, title)
if result:
    print("Accepted!")
else:
    print("Oops!", sys.exc_info()[0], "occurred.")

pattern = '^.19|20'
result = re.search(pattern, year)
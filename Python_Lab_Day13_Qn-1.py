import os

item = input("Enter the name of new item: ")
if os.path.exists("items.txt"):
    with open("items.txt", "a") as f:
        f.write(item )




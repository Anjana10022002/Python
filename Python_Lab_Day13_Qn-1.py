import os

item = input("Enter the name of new item: ")
if os.path.exists("items.txt"):
    with open("items.txt", "a") as f:
        f.write(item )
else:
    with open("items.txt", "w") as f:
        f.write(item )

print("THe list is:") 
with open("item.txt", "r"):
    for x in items:
        print(x)  

        


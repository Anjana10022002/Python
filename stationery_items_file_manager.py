import os

item = input("Enter the name of new item: ")
if os.path.exists("items.txt"):
    with open("items.txt", "a") as f:
        f.write(item + "\n")
else:
    with open("items.txt", "w") as f:
        f.write(item + "\n" )

print("THe list is:") 
with open("items.txt", "r") as f:
    for x in f:
        print(x.strip())  

        


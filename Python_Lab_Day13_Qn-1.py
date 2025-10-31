import os
userName = input("Enter your name: ")
if os.path.exists("items.txt"):
    f = open("items.txt", "a")
    f.write("Condition for file exists.")
    f.close()
else:
    f = open("items.txt", "x")
    f = open("items.txt", "w")
    f.write("Condition for file not exist")
f = open("items.txt", "r")
print(f.read())
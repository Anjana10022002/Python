import os
count = int(input("Enter the number of students wanted to add: ") )
if os.path.exists("students.txt"): 
    with open("students.txt", "a") as f:
        existing_names = f.readlines()
        if existing_names:
            for x in existing_names:
                print(x.strip())
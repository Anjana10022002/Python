import os
count = int(input("Enter the number of students wanted to add: ") )
if os.path.exists("students.txt"): 
    with open("students.txt", "r") as f:
        for x in f:
            print(x.strip())
    
       
else:
    print("No item in existing file")

with open("student.txt", mode) as f:
    for i in range(count):
        


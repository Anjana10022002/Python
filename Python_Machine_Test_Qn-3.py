array = [{"id":1, "name":"Rajesh"},
         {"id":2, "name":"Rahul"}, 
         {"id":3, "name":"Sruthi"}]

num = int(input("Enter the ID number: "))

for x in array:
    if num == x["id"]:
        print(f"Student name is: {x["name"]}")
        break
else:
    print("Student ID not exist")
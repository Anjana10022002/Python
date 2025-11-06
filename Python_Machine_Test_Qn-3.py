array = [{"id":1, "name":"rajesh"},
         {"id":2, "name":"rahul"}, 
         {"id":3, "name":"sruthi"}]

num = int(input("Enter a ID number: "))
for x in array:
    if num == array.id:
        print(f"Student name is: {array["name"]}")
    else:
        print("Student ID not exist")
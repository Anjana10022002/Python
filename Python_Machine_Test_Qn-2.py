num = int(input("Enter the number: "))
print(f"The multiplication table of {num} is: ")
for i in range(1, 11):
    multiplication = i * num
    print(f"{i} * {num} = {multiplication}")
    
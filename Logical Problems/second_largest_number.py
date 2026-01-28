num = [10, 35, 40, 59, 12]
largest = num[0]
second_largest = -1

for n in num:
    if n > largest:
        second_largest = largest
        largest = n
    elif n != largest and n > second_largest:
        second_largest = n

print("Second largest:", second_largest)

# num = [10,30,40,23,56]
# largest = num[0]
# for n in num:
#     if n > largest:
#         largest = n

# print("Largest: ", largest)
import random
import math

invited_guests = input("Enter the list of names of invited guests (comma-separated): ")
list = invited_guests.split(",")

remove_duplication = []
for x in list:
    if x not in remove_duplication:
        remove_duplication.append(x)

print("After removing duplicate names:" + str(remove_duplication))

random = random.choice(remove_duplication)
print("Randomly chooosed guest: ", random)

def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]
s = remove_duplication[1]
print("The reversed string is: ", reverse(s))

count = len(remove_duplication)
print("Total number of unique names: ", count)
print("Rounded square root of total unique names: ", math.ceil(math.sqrt(count)))




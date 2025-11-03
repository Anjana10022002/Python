import random

invited_guests = input("Enter the list of names of invited guests (comma-separated): ")
list = invited_guests.split(",")

remove_duplication = []
for x in list:
    if x not in remove_duplication:
        remove_duplication.append(x)

print("After removing duplicate names:" + str(remove_duplication))

random = random.choice(remove_duplication)
print("Randomly chooosed guest: ", random)


import random

name = input("Enter names of customers (comma-separated) who have placed orders today: ")
list = name.split(",")

new_list = list(set(list))
print("Customers name after removing duplication: ", new_list)

shuffled_list = random.shuffle(new_list)
print("Shuffled final list of names: ", shuffled_list)

random_customer = random.randrange(new_list,2)
print("Randomly selected 2 customers: ", random_customer)

def reverse(s):
    s = s[::-1]
    return s
s = random_customer
print("The reversed string is: ", reverse(s))




initial_grocery = ["milk", "bread", "eggs"]

def add_item(item):
    initial_grocery.append(item)

def remove_last_Item():
    removeItem = initial_grocery.pop()

show_item = lambda item: print(f"Item: {item}")

def count_characters(x):
    if not x:
        return 0
    else:
        return len(x[0]) + count_characters(x[1:])
    
print("Initial grocery list: ")
for x in initial_grocery:
    show_item(x)

add_item("sugar")
print("After adding new item")
for x in initial_grocery:
    show_item(x)

remove_last_Item()
print("Gracery list after removing last item: ")
for x in initial_grocery:
    show_item(x)

total_characters = count_characters(initial_grocery)
print("Total number of characters:", total_characters)
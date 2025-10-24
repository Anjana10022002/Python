initial_grocery = ["milk", "bread", "eggs"]
def add_item(item):
    initial_grocery.append(item)
    print("Updated grocery list: ",initial_grocery)
def remove_last_Item():
    removeItem = initial_grocery.pop()
    print("Updated grocery list after removing last item: ", initial_grocery)
add_item("butter")
remove_last_Item()


inventory = []
def add_item(item):
    addItem = inventory.append(item)
    print(inventory)
add_item("Dog food")
add_item("Cat toy")
add_item("Bird cage")
add_item("Fish tank")
def count_items(items):
    if items == "" or items == []:
        return 0
    else:
        return 1 + count_items(items[1:])
print("The count of inventory list is: ",count_items(inventory))
show_item = lambda item: print(f"Item in Stock: {item}")
show_item("Dog food")
show_item("Cat toy")
show_item("Bird cage")
show_item("Fish tank")




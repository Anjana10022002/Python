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
print("The count of inventory lisy is: ",count_items(inventory))

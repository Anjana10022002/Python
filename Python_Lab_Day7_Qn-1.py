initial_grocery = ["milk", "bread", "eggs"]
def add_item(item):
    initial_grocery.append(item)
def remove_last_Item():
    removeItem = initial_grocery.pop()
show_item = lambda item: print(f"Item: {item}")
for i in initial_grocery:
    show_item(i)
def count_characters(x):
    if not x:
        return 0
    else:
        return len(item[0]) + count_characters(item[1:])

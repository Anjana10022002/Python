fruits = ["apple", "orange", "grape"]
vegetables = ["carrot", "cabbage", "spinach"]
beverages = ["water", "juice", "coffee"]
fruits.append("dragonfruit")
vegetables.insert(2, "broccoli")
beverages.pop()
inventory = fruits + vegetables + beverages
print("First two fruits:", fruits[:2])
print("First two vegetables:", vegetables[:-2])
name_lengths = [len(name) for name in fruits]
print("Length of each name in Fruits list:", name_lengths)
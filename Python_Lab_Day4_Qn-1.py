fruits = ["apple", "orange", "grape"]
vegetables = ["carrot", "cabbage", "spinach"]
beverages = ["water", "juice", "coffee"]
fruits.append("dragonfruit")
vegetables.insert(1, "broccoli")
beverages.pop()
inventory = fruits + vegetables + beverages
print("First two fruits:", fruits[:2])
print("Lastitem in vegetables:", vegetables[-1])
name_lengths = [len(name) for name in fruits]
print("Length of each name in Fruits list:", name_lengths)
if "water" in beverages:
    print("Yes, 'water' is in the beverage list")
else:
    print("No, 'water' is not in the beverage list")
first_element = (fruits[0], vegetables[0], beverages[0])
print("First elements of each section are: ", first_element)
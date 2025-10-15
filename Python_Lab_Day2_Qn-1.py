receiptHeader = """XYZ Store
Receipt"""
print(receiptHeader)
item1 = "Book Title: {a}\t - {b}".format(a = 'Python Basics', b = '₹450')
print(item1)
item2 = "Book Title: {a}\t - {b}".format(a = 'Data Science Intro', b = '₹600')
print(item2)
Total = 450 + 600
totalAmount = "Total amount:\t\t\t - {}".format(Total)
print(totalAmount)
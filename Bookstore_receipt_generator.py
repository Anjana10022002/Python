receiptHeader = """XYZ Store \n
Receipt \n"""
print(receiptHeader.upper())
item1 = "Book Title: {a}\t - {b}".format(a = 'Python Basics', b = '₹450')
print(item1.upper())
item2 = "Book Title: {a}\t - {b}".format(a = 'Data Science Intro', b = '₹600')
print(item2.upper())
Total = 450 + 600
totalAmount = "Total amount:\t\t\t - {}".format(Total)
print(totalAmount.upper())
Thankyou = "\n\nThank you for shopping with us! \n"
print(Thankyou.upper())

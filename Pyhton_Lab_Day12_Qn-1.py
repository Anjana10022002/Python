import re

try:
    title = input("Enter the book title: ")
    year = input("Enter the publication year: ")

    if re.fullmatch('^[a-zA-Z ]+$', title):
        print("Book title accepted!")
    else:
        raise ValueError("Book title must contain only alphabets and spaces. ")
    if re.fullmatch(r'(19|20)\d{2}', year):
        print("Publishing year accepted!")
    else:
        raise ValueError("Publication year must contain 4 digits and starting with 19 or 20.")
except ValueError as e:
    print("Error: ", e)

finally:
    print("Program sucessfully executed")
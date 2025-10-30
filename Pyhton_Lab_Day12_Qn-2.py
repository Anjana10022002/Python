import re

try:
    name = input("Enter your name: ")
    feedback = input("Enter your feedback: ")

    if re.fullmatch('', name):
        raise ValueError("Name cannot be empty")
    else:
        print("Name accepted!")

    if re.fullmatch('', feedback):
        raise ValueError("Feedback cannot be empty")
    else:
        print("Feedback accepted!")
    
except ValueError as e:
    print("Error: " ,e)

finally:
    print(f"Thankyou {name} for the feedback: \"{feedback}\"")
    

"""
Question: Student Name Tracker

Create a Python program that:

Starts with a list of student names: ["Alice", "Bob", "Charlie"].

Has a function add_student(name) to add a new student to the list.

Has a function remove_last_student() to remove the last student from the list.

Uses a lambda function to print each student in the format: "Student: <name>".

Includes a recursive function count_total_letters(names) that returns the total number of letters in all student names combined.
"""
student = ["Alice", "Bob", "Charlie"]

def add_student(x):
    student.append(x)

def remove_last_student():
    student.pop()

show_student= lambda x: print(f"Student:{x}")

def count_total_letters(x):
    if not x:
        return 0 
    else:
        return len(x[0]) - count_total_letters(x[1:])

print("Student list:")
for x in student:
    show_student(x)

add_student("Alex")
print("Student list sfter adding: ")
for x in student:
    show_student(x)

remove_last_student()
print("Student list after removing last student name: ")
for x in student:
    show_student(x)

print
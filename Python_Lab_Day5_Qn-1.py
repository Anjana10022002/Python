Python = {"Ajay", "Max", "John", "Sara"}
DataScience = {"John", "Mike", "Sara", "Linda"}
Python.add("Alana")
DataScience.pop()
bothCourse = Python.intersection(DataScience)
print("Students enrolled in both the courses: ", bothCourse)
onlyPython = Python - DataScience
print("Students enrolled only in Python: ", onlyPython)

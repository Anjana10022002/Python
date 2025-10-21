frontend = {"Alan", "Sarah", "Kate", "Tom"}
backend = {"John", "Alex", "Mike", "Max"}
backend.add("Ben")
frontend.remove("Sarah")
bothCourses = frontend.union(backend)
print("Students enrolled in both the courses: ", bothCourses)
onlyBackend = backend - frontend
print("Students enrolled only in backend: ",onlyBackend)
print("Total number of unique students: ", len(bothCourses))

course = {
    "Frontend" : len(frontend),
    "Backend" : len(backend)
    }
for courseName, student in course.items():
    print("The couse name and number of students in courses are:", courseName, student)
dictComprehension = {
    "Fullstack" : len(frontend) + len(backend)
}
print("Fullstack couses: ", dictComprehension)
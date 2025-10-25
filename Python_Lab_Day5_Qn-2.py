frontend = {"Alan", "Sarah", "Kate", "John"}
backend = {"John", "Alex", "Mike", "Max"}
backend.add("Ben")
frontend.remove("Sarah")
bothCourses = frontend.intersection(backend)
print("Students enrolled in both the courses: ", bothCourses)
onlyBackend = backend - frontend
print("Students enrolled only in backend: ",onlyBackend)
uniqueStudents = frontend.union(backend)
print("Total number of unique students: ", len(uniqueStudents))
course = {
    "Frontend": len(frontend),
    "Backend": len(backend)
}
for x, y in course.items():
    print("The course name and number of students in courses are:", x, y)
fullStack = {
    "Fullstack" : len(frontend) + len(backend)
}
print("Fullstack course: ", fullStack)


print
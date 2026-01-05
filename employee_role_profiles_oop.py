class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, employee_id):
        Person.__init__(self, name, age)
        self.employee_id = employee_id
    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Employee ID: {self.employee_id}")

class PartTime(Person):
    def __init__(self, name, age, working_hours):
        Person.__init__(self, name, age)
        self.working_hours = working_hours
    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Working Hours: {self.working_hours}")

class Consultant(Employee, PartTime):
    def __init__(self, name, age, employee_id, working_hours, project_name):
        Employee.__init__(self, name, age, employee_id)
        PartTime.__init__(self, name, age, working_hours)
        self.project_name = project_name
    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Employee ID: {self.employee_id}, "
              f"Working Hours: {self.working_hours}, Project: {self.project_name}")

person = Person("Alice", 30)
employee = Employee("Bob", 35, "E123")
part_time = PartTime("Charlie", 28, 20)
consultant = Consultant("David", 40, "C456", 25, "ProjectX")

person.show_details()
employee.show_details()
part_time.show_details()
consultant.show_details()

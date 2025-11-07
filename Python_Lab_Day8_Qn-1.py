class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show_details(self):
        print(f"Name: {self.name}\n Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id
    def __str__(self):
        return super().__str__() + f"\nEmployee Name: {self.name}\nAge : {self.age}\nEmployee ID: {self.employee_id}"
    
class PartTime(Person):
    def __init__(self, name, age, working_hours):
        super().__init__(name, age)
        self.working_hours = working_hours
    def __str__(self):
        return super().__str__() + f"\nEmployee Name: {self.name}\nAge : {self.age}\nWorking Hours: {self.working_hours}"
    
class Consultant(Employee, PartTime):
    def __init__(self, name, age, employee_id, working_hours, project_name):
        Employee.__init__(self, name, age, employee_id)
        PartTime.__init__(self, name, age, working_hours)
        self.project_name = project_name
    def __str__(self):
        return Employee.__str__(self) + f"\nName: {self.name}\nAge:{self.age}\nEmployee ID: {self.employee_id}\nWorking Hours: {self.working_hours}\nProject name: {self.project_name}"
    
person = Person("Alice", 30)
employee = Employee("Bob", 35, "E123", person.show_details)
partTime = PartTime("Charlie", 28, 20, person.show_details)
consultant = Consultant("David", 40, "C456", 25, "ProjectX", person.show_details)

person.show_details()
employee.show_details()
partTime.show_details()
consultant.show_details()
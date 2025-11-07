class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show_details(self, name, age):
        print(f"Name: {name}\n Age: {age}")
class Employee(Person):
    def __init__(self, name, age, employee_id, show_details):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.show_details = show_details
    def __str__(self):
        return super().__str__() + f"\nEmployee Name: {self.name}\nAge : {self.age}\nEmployee ID: {self.employee_id}"
class PartTime(Person):
    def __init__(self, name, age, working_hours, show_details):
        super().__init__(name, age)
        self.working_hours = working_hours
        self.show_details = show_details
    def __str__(self):
        return super().__str__() + f"\nEmployee Name: {self.name}\nAge : {self.age}\nWorking Hours: {self.working_hours}"

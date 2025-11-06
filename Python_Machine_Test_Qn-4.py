class Calculator:
    def addition(self, num1, num2):
        return num1 + num2
    def subtraction(self, num1, num2):
        return num1 - num2
    def multiplication(self, num1, num2):
        return num1 * num2
    def division(self, num1, num2):
        return num1 / num2
cal_obj = Calculator()
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Enter the operation(+, -, *, /): ")
if operation == "+":
    result = cal_obj.addition(num1, num2)
    print("Result is: ", result)
elif operation == "-":
    result = cal_obj.subtraction(num1, num2)
    print("Result is: ", result)
elif operation == "*":
    result = cal_obj.multiplication(num1, num2)
    print("Result is: ", result)
else:
    result = cal_obj.division(num1, num2)
    print("Result is: ", result)
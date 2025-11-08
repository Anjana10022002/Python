# Qn-1
# print("Hello World")

# Qn-2
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# sum = a + b
# print("The sum is: ", sum)

# Qn-3
# import math
# a = int(input("Enter the number: "))
# square = a ** 0.5
# # square = math.sqrt(a) 
# print("The square root of the number is: ", square)

# Qn-4
# a = int(input("Enter the first side:"))
# b = int(input("ENter the second number: "))
# c = int(input("Enter the third number: "))
# s = (a+b+c)/2
# area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
# print("The area of triangle is: " ,area)

# Qn-5
# import cmath
# a = int(input("Enter coefficient a: "))
# b = int(input("Enter coefficient b: "))
# c = int(input("Enter coefficient c: "))
# d = (b**2) - (4*a*c)
# solution1 = (-b + cmath.sqrt(d)) / (2*a)
# solution2 = (-b - cmath.sqrt(d)) / (2*a)
# print(f"THe solution of quadratic equation are {solution1} and {solution2}")

# Qn-6
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# print(f"The number before swapping are {a} and {b}")
# # a = a + b
# # b = a - b
# # a = a - b
# temp = a
# a = b
# b = temp
# print(f"The numbers after swapping are {a} and {b}")

# Qn-7
# import random
# # random_num = random.random()
# random_num = random.randint(10,100)
# print("The random number is: ", random_num)

# Qn-8
# km = float(input("Enter the value in kilometers: "))
# const = 0.621
# miles = km * const
# print(f"{km} km is equal to {miles} mile")

# Qn-9
# celsius = int(input("Enter the celsius vaalue: "))
# fahren = (celsius * 1.8) + 32
# print(f"Fahrenheit value of {celsius} degree celsius is {fahren}")

# qn-10
# a = int(input("Enter the number: "))
# if a > 0:
#     print(f"{a} is positive")
# elif a < 0:
#     print(f"{a} is negative")
# else:
#     print(f"{a} is zero")

# Qn-11
# num = int(input("Enter the number: "))
# if num % 2 == 0:
#     print(f"{num} is even")
# else:
#     print(f"{num} is odd")

# Qn-12
# year = int(input("Enter the year: "))
# if (year % 400 == 0) and (year % 100 ==0):
#     print(f"{year} is a leap year")
# elif(year % 4 == 0) and (year % 100 != 0):
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")

# Qn-13
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# c = int(input("Enter the third number: "))
# if (a > b) and (a > c):
#     print(f"{a} is the largest number")
# elif (b > a) and (b > c):
#     print(f"{b} is the largest number")
# else:
#     print(f"{c} is the largest number")

# Qn-14
# num = int(input("Enter the number: "))
# if num == 0 or num == 1:
#     print(f"{num} is not a prime number.")
# elif num > 1:
#     for i in range(2, num):
#         if(num % i) == 0:
#             print(f"{num} is a prime number.")
#             break
#         else:
#             print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")

# Qn-15
# upper = int(input("Enter the upper limit: "))
# lower = int(input("Enter the lower limit: "))
# for x in range (lower, upper + 1):
#     if x > 1:
#         for i in range(2, x):
#             if (x % i) == 0:
#                 break
#         else:
#             print(x)

# Qn-16 Python Program to Find the Factorial of a Number
# def factorial(x):
#     if x == 1 or x == 0:
#         return 1
#     else:
#         return (x * factorial(x - 1))
# num = int(input("Enter the number: "))
# result = factorial(num)
# print(f"The factorial of {num} is {result}")

# num = int(input("Enter the number: "))
# factorial = 1
# if num < 0:
#     print("Factorial doesn't exist for negative numbers")
# elif num == 0:
#     print("Factorial of 0 is 1")
# else:
#     for i in range (1, num + 1):
#         factorial = factorial * i
#     print(f"Th efactorial of {num} is {factorial}")

# Qn-17 Python Program to Display the multiplication Table
# num = int(input("Enter the number: "))
# print(f"Multipllication table of {num}:")
# for i in range(1, num+1):
#     multiplication = num * 1
#     print(f"{i} X {num} = {multiplication}")

# Qn-18 Python Program to Print the Fibonacci sequence
# terms = int(input("Enter the number of terms: "))
# n1 = 0
# n2 = 1
# count = 0
# if terms <= 0:
#     print("Enter a positive number")
# elif terms == 1:
#     print(f"Fibonacci sequence of {terms} terms is: {n1}")
# else:
#     print(f"Fibonacci sequence of {terms} terms is: ")
#     while count < terms:
#         print(n1)
#         seq = n1 + n2
#         n1 = n2
#         n2 = seq
#         count += 1

# Qn-19  Python Program to Check Armstrong Number
# num = int(input("Enter the number: "))
# order = len(str(num))
# sum = 0
# temp = num
# while temp > 0:
#     digit = temp % 10
#     sum = sum + digit ** order
#     temp = temp // 10
# if num == sum:
#     print("The number is Armstrong")
# else:
#     print("The number is not Armstrong")

# Qn-20  Python Program to Find Armstrong Number in an Interval
# lower = int(input("Enter the lower limit: "))
# upper = int(input("Enter the upper limit: "))
# for num in range(lower, upper + 1):
#     order = len(str(num))
#     sum = 0
#     temp = num
#     while temp > 0:
#         digit = temp % 10
#         sum += digit ** order
#         temp //= 10
#     if num == sum:
#         print(num)






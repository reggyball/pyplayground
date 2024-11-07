#  Write a program that gets an integer x, and prints the five (5) integers after it.

# x = int(input("Enter a number: "))

# for n in range (0, 5):
#     x = x+1 
#     print(x)

# ------------------------------------------------------------------------------------
# Create a program that computes for x^y by repeated multiplication. x and y positive integers and are inputs from the user.
# x = int(input("Enter a number: "))
# y = int(input("Enter a number: "))

# n = 0
# z = x
# while n < y-1:
#     z = z * x
#     n += 1
# print(z)

# ------------------------------------------------------------------------------------
# Create a program that computes for the square root of a number using the guess and check method.

# x = float(input("Enter a number: "))
# error = 0.01 
# high_threshold = x + error
# low_threshold = x - error
# g = x/2

# print(g)
# while g*g > high_threshold or g*g < low_threshold:
#     g = (g+x/g)/2
#     print(g)

# print(g)

# ------------------------------------------------------------------------------------
# Problem 8. Create a program that generates a random integer and makes the user guess that integer. Clues are given (higher or lower) to help the user guess the integer.
# import random

# random_int = random.randint(1, 100)
# print("R:", random_int)
# while (guess := int(input("Enter your guess: "))) !=  random_int:
#     if guess > random_int:
#         print("Lower!")
#     elif guess < random_int:
#         print("Higher!")
# print("Correct!")


# ------------------------------------------------------------------------------------
# Problem 8.1 with 10 guess Create a program that generates a random integer and makes the user guess that integer. Clues are given (higher or lower) to help the user guess the integer.
# import random

# random_int = random.randint(1, 100)
# print("R:", random_int)
# counter = 0
# while counter < 10 and (guess := int(input("Enter your guess: "))) != random_int:
#     if guess > random_int:
#         print("Lower!")
#     elif guess < random_int:
#         print("Higher!")
#     counter += 1
# if guess == random_int:
#     print("Correct!")
# else:
#     print("Sorry! you maxxed out your guesses :(")

# ------------------------------------------------------------------------------------
# Problem 9. Create a program that asks for a positive integer n and prints the following nxn patterns: (1)Filled up square and (2) Hollow Square

# n = int(input("Enter a number: "))
# print("1. Filled-up square")
# for i in range (0, n):
#     star = ""
#     for j in range (0, n):
#        star += "*"
#     print(star)

# n = int(input("Enter a number: "))
# for i in range(0, n):
#     for j in range (0, n):
#         print("X", end = "")
#     print()

# print()

# print("2. Hollow square")
# print("*" * n)
# for k in range (0, n-2):
#     print("*" + " " * (n-2) + "*")
# print("*" * n)

# n = int(input("Enter a number: "))
# for i in range(0, n):
#     for j in range(0, n):
#         if i == 0 or j == 0 or i == n-1 or j == n-1:
#             print("X", end = "")
#         else:
#             print(" ", end = "")
#     print()
    
# ------------------------------------------------------------------------------------
# Problem 9: Create a program that prints the largest integer among the three inputs of the user.
# n = int(input("Enter number: "))
# def largest (n):
#    for i in range(2):
#       m = int(input("Enter number: "))
#       if m > n:
#         n = m 
#    print(n)
# largest(n)

# ------------------------------------------------------------------------------------
# Problem 1: Create a program that computes the surface area of a cylinder, given its height (cm) and radius (cm).
#2πrh + 2πr².
# pi = 3.14159265359

# def surface_area (r, h):
#    sa = (2 * pi * r * h) + (2 * pi * r**2)
#    print("Circumferce:",sa, "cm")

# h = float(input("Enter height in cm: "))
# r = float(input("Enter radius in cm: "))

# surface_area(r, h)

# ------------------------------------------------------------------------------------
# Problem 1: Create a program that computes the surface area of a cylinder, given its height (cm) and radius (cm).
# Use the same functions to compute for the surface area of a cube and a sphere.
# pi = 3.14159265359
# def surface_area(shape, dimension1, dimension2=None):
#     if shape == "cylinder":
#         sa = (2 * pi * dimension1 * dimension2) + (2 * pi * dimension1**2)
#     elif shape == "cube":
#         sa = 6*(dimension1**2)
#     elif shape == "sphere":
#         sa = 4 * pi * (dimension1**2)
#     else:
#         sa = None
#     return sa


# shape = input("shape: ").lower()
# if shape == "cylinder":
#     dimension1 = int(input("Enter radius in cm: "))
#     dimension2 = int(input("Enter height in cm: "))
#     print("Surface area: ", surface_area(shape, dimension1, dimension2))
# elif shape == "cube":
#     dimension1 = int(input("Enter side in cm: "))
#     print("Surface area: ", surface_area(shape, dimension1))
# elif shape == "sphere":
#     dimension1 = int(input("Enter radius in cm: "))
#     print("Surface area: ", surface_area(shape, dimension1))

# ------------------------------------------------------------------------------------
# Problem 1: Create a program that computes the surface area of a cylinder, given its height (cm) and radius (cm).
# Use the same functions to compute for the surface area of a cube and a sphere.
# pi = 3.14

# def surface_area(shape, d1, d2=None):
#     if shape == cylinder:
#         area_circle  = pi*d1*d1
#         circumference = 2*pi*d1
#         area_rect = circumference * d2
#         sa = area_rect + (2*area_circle)
#     elif shape == cube:
#         sa = 6*(d1**2)
#     elif shape == sphere:
#         sa = 4*pi*(d1**2)
#--------------------------------------------------------------------------------------------
# Problem 10: Create a recursive function that computes for the factorial of a number n.

# def factorial(n):
#     #basecase
#     if n == 1 or n == 0:
#         return 1
#     #recursivecase
#     return n + factorial(n-1)

# n = int(input("Enter number: "))
# print(factorial(n))

#--------------------------------------------------------------------------------------------
# Problem 11: Create a recursive function that computes for the nth fibonacci number. Here are the first few fibonacci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34. 
# The next number is obtained by adding the two numbers before it.
# For example, 2 is obtained by adding 1 and 1, 3 is obtained by adding 2 and 1, and so on.

# def fibonacci(max, nth=0, curr=0, next=1):
#     if nth == max:
#         return curr
#     nth += 1
#     return fibonacci(max, nth, next, curr+next) 

# max = int(input("Enter n: "))
# print(fibonacci(max=max))

# def fib(n):
#     if n == 1 or n == 0:
#         return n
    
#     return fib(n-1) + fib(n-2)

# n = int(input("Enter n: "))
# print(fib(n))
#---------------------------------------------------------------------------------------
#PRACTICE PROBLEMS
#Create a program that determines the largest number among the four inputs of the user.
#determines the largest number among the four inputs of the user.

# prompts = ["first", "second", "third", "fourth",]
# numbers = [float(input("Enter " + prompt + " number: ")) for prompt in prompts]
# print("The largerst number is", max(numbers))


# create a list called prompts that contains a part of the string that will serve as the custom message in the input query. This also where the for loop inside the comprehension loops through.
# use a comprehension to create a list that will store the numbers from the user input.
# Since the comprehension uses the function 'input' to obtain the user input, it needs to be typecasted to float, as the return value of input is a string.
# use max function to determine the element with the highest value and print the return value


#CONDITIONALS
#Create a program that determines the largest number among the four inputs of the user.

prompts = ["first", "second", "third", "fourth"]
larger = float('-inf')
for i in range(4):
    num = float(input(f"Enter {prompts[i]} number: "))
    if num > larger:
        larger = num
print(larger)


# prompts = ["first", "second", "third", "fourth"]
# larger = float(input(f"Enter first number: "))
# for i in range(1, 4):
#     num = float(input(f"Enter {prompts[i]} number: "))
#     if num > larger:
#         larger = num
# print(larger)

# prompts = ["first", "second", "third", "fourth"]
# larger = None
# for i in range(4):
#     num = float(input(f"Enter {prompts[i]} number: "))
#     if larger == None:
#         larger = num
#     if num > larger:
#         larger = num
# print(larger)



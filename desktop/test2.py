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

# prompts = ["first", "second", "third", "fourth"]
# larger = float('-inf')
# for i in range(4):
#     num = float(input(f"Enter {prompts[i]} number: "))
#     if num > larger:
#         larger = num
# print(larger)


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

#---------------------------------------------------------------------------------------------
# Create a program that computes the BMI of a person and determines whether he is underweight, normal, or overweight.

# The Body Mass Index (BMI) is computed using the following formula:
# BMI = weight in kg / (height in m)^2
# BMI Categories:
# Underweight = <18.5
# Normal weight = 18.5–24.9
# Overweight = 25–29.9
# Obesity = BMI of 30 or greater

# Sample run of the program:
# Enter height (m): 1.52
# Enter weight (kg): 59
# Your BMI: 25.5 kg/m2 (Overweight)

#obtain user input
# height = float(input("Enter height (m): "))
# weight = float(input("Enter weight (kg): "))

# #compute for BMI
# BMI = weight/height**2
# BMI = round(BMI, 1)

# #categorize BMI
# if BMI >= 30:
#     category = "Obesity"
# elif BMI >= 25 and BMI <= 29.9:
#     category = "Overweight"
# elif BMI >= 18.5 and BMI <= 24.9:
#     category = "Normal weight"
# else:
#     category = "Underweight"

# #print output
# print(f"Your BMI: {BMI} kg/m2 ({category})")

#---------------------------------------------------------------------------------------------
# ITERATIVE
# Twin 'a'
# Continuously ask an input until the user enters two consecutive ‘a’.

# while True:
#     ax = input("Enter an input: ")
#     if ax == "a":
#         bx = input("Enter an input: ")
#         if ax == bx:
#           if bx == "a":
#              break    

# counter = 0
# while counter != 2:
#     ax = input("Enter an input: ")
#     if ax == "a":
#         counter += 1
#     else: 
#         counter = 0


#---------------------------------------------------------------------------------------------
#Write a program that prints the integer cube root of an integer x. If x is not a perfect cube, print a message saying so. 

# Example:	x = -27 -> cube root is -3
# 		x = 5 -> not a perfect cube

# while abs(a := int(input("Enter an integer: "))) != round(abs((a**(1/3))))**3:
#    print("not perfect cube")
# if a < 0:
#     cube_root = round(abs(-(a)**(1/3)))
#     cube_root = -cube_root
# else:
#     cube_root = round(a**(1/3))
# print(f"Cube root is {cube_root}")


# a = int(input("Enter an integer: "))
# counter2 = 0
# counter3 = 0
# counter5 = 0

# while a != 1:
#     if a % 2 == 0:
#         a = a / 2
#         counter2 += 1
#     if a % 3 == 0:
#         a = a /3
#         counter3 = +1
#     if a % 5 == 0:
#         a = a /5 
#         counter5 = +1
# print(counter2, counter3, counter5)

#----------------------------------------------------------------------------
#The Kingdom of Kapatid has banned the numbers 2 and 7. 
# Given a range of values n and m as user’s input, print the numbers from n to m (inclusive) that are not multiples of 2 and 7 
# and do not contain the values 2 and 7 such as 72, 17, 22, 42, and 77.

#obtain user input
# n = int(input("Enter n: "))
# m = int(input("Enter m: ")) 

# #create an empty list for eligible values 
# value = []

# #loop through numbers from n to m 
# for i in range(n, m+1):                           
#     if i % 2 == 0 or i % 7 == 0:                 #skips numbers divisible by 2 or 7
#         continue
#     if "7" in str(i) or "2" in str(i):           #skips numbers with digits 7 or 2
#         continue
#     else:                                        #adds in the list: numbers that satisfied given conditions
#         value += [i]
# print(value)                                    #prints the final list 

#----------------------------------------------------------------------------
#Merry Christmas!
# Input a positive integer n and draw a Christmas tree-shaped figure of chars, consisting of n stacked trapezoids, neatly centered on the screen.


#----------------------------------------------------------------------------
# Leap Year
# Most years have 365 days. However, the time required for the Earth to orbit the Sun is actually slightly more than that. 
# As a result, an extra day, February 29, is included in some years to correct for this difference. Such years are referred to as leap years. 
# The rules for determining whether or not a year is a leap year follow:

# Any year that is divisible by 400 is a leap year.
# Of the remaining years, any year that is divisible by 100 is not a leap year.
# Of the remaining years, any year that is divisible by 4 is a leap year.
# All other years are not leap years.
# Write a program prints the leap years from 1900 to 2018.

#----------------------------------------------------------------------------
# #FUNCTIONS AND RECURSIONS

# Pascal's Triangle is a recursive definition tool, useful for calculating coefficients in the expansion of the polynomial (x+a)^n. 
# Each number in the triangle is situated by coordinates relating to its row and column within that row. 
# The number in each position is defined as the sum of the number directly above it and the number to its upper left.
# Implement a recursive function that returns the value in the ith row and jth column of the Pascal's triangle. 

# # this function returns the value at the ith row and jth column of the Pascal's Triangle
# def pascal (row, col):
#     if row == 1 or col == 1 or col == row + 1:                    #base cases
#         return 1
#     if row == col or col == 2:                                   #base case - unnecessary but reduces stack
#         return row
# def pascal (row, col):
#     if row == 1 or col == 1 or col == row + 1:                    #base cases
#         return 1
#     if row == col or col == 2:                                   #base case - unnecessary but reduces stack
#         return row
   
#     return pascal(row-1, col) + pascal(row-1, col-1)            #recursive case
# print (pascal (5,3)) # the output is 10

#_________________________________________________________________________
#STRINGS
#_________________________________________________________________________
#Problem statement: Create a program that changes the character ‘a’ in the given string to a different character.

# import random
# import string

# x = input("Give me a string: ")
# y = input("Replace which letter? ")
# random_char = random.choice(string.ascii_lowercase)

# x = x.replace(y, random_char)
# print(x)
# #----------------------------------------
# x = input("Give me a string: ")
# y = input("Replace a with? ")

# x = x.replace("a", y)
# print(x)

#----------------------------------------
# def modify(x, y):
#     modified = ""

#     for i in x:
#         if i == "a":
#             modified += y
#         else:
#             modified += i
#     return modified

# x = input("Give me a string: ")
# y = input("Replace a with? ")
# print(modify(x, y))

#-----------------------------------------------------------------------------------------
#Palindrome
#Problem statement: Create a program that determines whether a string is a palindrome or not.

# x = input("Give me a word: ")
# x = x.lower().replace(" ", "")
# y = x[::-1]
# print(x)
# print(y)
# if x == y:
#     print("Palindrome siya")
# else:
#     print("Not a palindrome")

# def clean(x):
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     y = ""

#     for i in x:
#         if i in alphabet:
#             y += i
#     return y


# def ispalindrome(x):
#     y = clean(x)

#     if y == y[::-1]:
#         print("Palindrome")
#     else:
#         print("Not a palindrome")


# x = input("Give me a word: ")
# ispalindrome(x)



#-----------------------------------------------------------------------------------------
#Run-length encoding

# Problem statement: Create a function that performs a Run Length Encoding (RLE) data compression algorithm on a given bitmap image represented by a string of 1’s (black) and 0’s (white). 
# The function accepts a string then returns the compressed string using RLE.

# x = input("Enter a bitmap image: "  )


#-------------------------------------------------------------------------------------------
#LISTS
#Building a list of random integers
#Problem Statement: Create a program that builds a list of 10 random integers from 1 to 100. The integers in the list must be unique.
# import random

# list1 = []

# i = 0
# while i < 10:
#     random_int = random.randint(1, 101)
#     while random_int in list1:
#         random_int = random.randint(1, 101)
#     else:
#         list1.append(random_int)
#     i += 1

# print(list1)

#------------------------------------------------------------------------------------------- 
# Word-unit palindrome
# Problem Statement: Create a program that determines whether a string is a word-unit palindrome or not.

# string = input("Enter a string: ")
# string = string.lower()

# def clean(string):
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     newstr = ""
#     for i in string:
#         if i in alphabet:
#                 newstr += i
#     return newstr

                
# def ispalindrome(string):
#     words = string.split(" ")

#     for i in range(len(words)):
#         words[i] = clean(words[i])

#     if words == words[::-1]:
#          print("Palindrome")
#     else:
#          print("Not a palindrome")

# ispalindrome(string)

#------------------------------------------------------------------------------------
#NARCISSTIC NUMBER

# x = int(input("Enter an integer: "))

# for i in range(1, x+1):

#     #count no of digits of i
#     temp = i
#     nDigits = 0
#     while temp > 0:
#         temp = temp//10
#         nDigits += 1

#     #get the sum of the computed nth power of the digits 
#     sum = 0
#     temp = i
#     while temp > 0:
#         digit = temp%10
#         temp = temp//10

#         #compute for the nth power of the current digit
#         product = 1
#         for j in range(1, nDigits+1):
#             product *= digit
        
#         sum += product

#     if sum == i:
#         print(i, "is a narcissistic number")

#----------------------------------------------------------------------------------------------------------
# Write a program that determines if the integer input of the user is divisible by 2 only, divisible by 3 only, divisible by both 2 and 3, 
# and not divisible by 2 and 3.

# number = float(input("Number: "))
# if number % 3 == 0 and number % 2 == 0:
#     print("Divisible by both 2 and 3")
# elif number % 3 == 0:
#     print("Divisible by 3")
# elif number % 2 == 0:
#     print("Divisible by 2")
# else:
#     print("Not divisible by 2 or 3")
        
################################ DICTIONARIES #############################################

# months = {1: "Jan", 2: "Feb", 3: "March", 4: "April", 5: "May", 6: "Jun", 7: "Jul"}

# #ACCESS THE VALUE

# #using key
# print(months[1])

# #using .get()
# x = months.get(2)
# print(x)

# #using a default with .get()
# x = months.get(9)
# print(x)      #prints None
# x = months.get(9, "Sep")
# print(x)


# #ACCESS ALL KEYS/VALUES

# #returns dict objects
# print("-------------------DICT OBJECTS--------------")
# allK = months.keys()
# print(allK)
# allV = months.values()
# print(allV)

# #return as a pair, dict object
# pairs = months.items()
# print(pairs)


# #returns list
# print("---------------------LISTS------------------")
# print(list(allK))
# print(list(allV))
# print(list(pairs))

# #return individual strings
# print("---------------INDIVIDUAL STRINGS-----------")
# for key in allK:
#     print(key)
# print("\n")
      
# for val in allV:
#     print(val)
# print("\n")

# for pair in pairs:
#     print(pair)


# #ACCESSING ELEMENTS USING LOOP
# for k, v in months.items():
#     print(k,v)

# for k in months:
#     print("keys: ", k, "values: ", months[k])

#NESTED DICTIONARIES
# my_courses = {
#                 1: {"Code": "CMSC 202", "Title": "Principles of Programming"},
#                 2: {"Code": "CMSC 201", "Title": "Discrete Mathematics"}
#             }

# for course in my_courses:
#     print("course:", course)
#     for k, v in my_courses[course].items():
#         print(k, v)

#DICTIONARY COMPREHENSIONS

# dict_name = {key:value for key, value in zip(list1, list2)}

# names = ['Appa', 'Sunny', 'Theo']
# colors = ['white/black', 'Orange/white', 'Calico']
# cat_profile = {key:value for key, value in zip(names, colors)}
# print(cat_profile)

#------------------------------------------------------------------
#Problem: Create a program that stores the SMS keywords for a mobile service and the message that the service will send given the keyword.


# def addSMSkeywords(SMSKeywords):
#     keyword = input("\nEnter keyword: ")

#     if keyword in SMSKeywords.keys():
#         print("Keyword exists")
#     else: 
#         message = input("Enter the message: ")
#         SMSKeywords[keyword] = message

#     return SMSKeywords

# def printSMSKeywords(SMSKeywords):
#     print("\nSMS Keywords and Messages in the Dictionary")
#     for k, v in SMSKeywords.items():
#         print(f"{k} : {v}")

# def deleteSMSKeywords(SMSKeywords):
#     keyword = input("\nEnter keyword for deletion: ")

#     if keyword in SMSKeywords.keys():
#         del SMSKeywords[keyword]
#     else:
#         print("\nKeyword not in dictionary")
#     return SMSKeywords

# def searchSMSKeywords(SMSKeywords):
#     keyword = input("\nEnter keyword you want to search: ")

#     if keyword in SMSKeywords.keys():
#        print(keyword,"\t\t", SMSKeywords[keyword])
#     else:
#         print("\nKeyword not in dictionary")
    
# def menu ():
#     print("\n1. Add an SMS Keyword")
#     print("2. Print all SMS Keywords")
#     print("3. Delete an SMS Keyword")
#     print("4. Search an SMS Keyword")
#     print("0. Quit")
#     choice = int(input("Your choice: "))
#     return choice

# SMSKeywords = {}

# while True:
#     choice = menu()
#     if choice == 1:
#         SMSKeywords = addSMSkeywords(SMSKeywords)
#     elif choice == 2:
#         printSMSKeywords(SMSKeywords)
#     elif choice == 3:
#         SMSKeywords = deleteSMSKeywords(SMSKeywords)
#     elif choice == 4:
#         searchSMSKeywords(SMSKeywords)
#     elif choice == 0:
#         print("\nThanks! Bye!")
#         break
#     else:
#         print("Invalid choice:", choice)

#---------------------------------------------------------------------
# Practice Problem: Manage Product Information in a Store
# Create a program that stores product codes for a store and the details of each product (like price and description).
#  The user should be able to perform the following actions:
# 1. Add a Product
# 2. Print All Products
# 3. Delete a Product
# 4. Search for a Product
# 0. Quit

# def addProduct(products):
#     keyword = input("\nEnter product code: ")

#     if keyword in products.keys():
#         print("Product code already exists")
#     else:

#         description = (input("Enter product description: "))
#         price = (input("Enter product price: "))
#         products[keyword] = [description, price]

#     return products

# def printProduct(products):
#     print("\nProduct codes, descriptions and prices")

#     for code in products.keys():
#         print("Product code:", code)
#         print("Description:", products[code][0])
#         print("Price:", products[code][1])
#         print("\n")

# def delProduct(products):
#     keyword = input("\nEnter the product code for deletion: ")

#     if keyword in products.keys():
#         del products[keyword]
#         print("Successfully deleted", keyword)
#     else:
#         print("Product code not found")

#     return products

# def searchProducts(products):
#     keyword = input("\nEnter the product code: ")

#     if keyword in products.keys():
#         print("Product code: ", products[keyword])
#         print("Description: ", products[keyword][0])
#         print("Code:", products[keyword][1])
#     else:
#         print("Product code does not exist")

# def menu():
#     print("\n1. Add a product")
#     print("2. Print all products")
#     print("3. Delete a product")
#     print("4. Search for a product")
#     print("0. Quit")
#     select = int(input("Enter your choice: "))
#     return select

# products = {}

# while True:
#     select = menu()
#     if select == 1:
#         products = addProduct(products)
#     elif select == 2:
#         printProduct(products)
#     elif select == 3:
#         delProduct(products)
#     elif select == 4:
#         searchProducts(products)
#     elif select == 0:
#         print("Thanks, bye")
#         break
#     else:
#         print("Invalid Choice")

##############################################################
#FILE OPERATIONS
#Problem: Create a program that stores the SMS keywords for a mobile service and the message that the service will send given the keyword. Use files to store and retrieve data.
# 1. Add an SMS Keyword and message
# 2. Print all the Keywords and messages
# 3. Delete an SMS Keyword
# 4. Search for a message given a keyword


def loadData(filename):                                                 #copy data from file (kung meron) to a dictionary that the program will interact with the whole run
    SMSKeywords = {}                                                    #initial run -> initialize an empty dictionary

    fileHandle = open(filename, "r")
    for line in fileHandle:
        keyword, message = line.split(":") 
        SMSKeywords[keyword] = message [:-1]
    fileHandle.close()

    return SMSKeywords

def storeData(filename):
    fileHandle = open(filename, "w")
    for keyword, message in SMSKeywords.items():
        fileHandle.write(keyword + ":" + message + "\n")
    fileHandle.close()

def addSMSkeywords(SMSKeywords):
    keyword = input("\nEnter keyword: ")

    if keyword in SMSKeywords.keys():
        print("Keyword exists")
    else: 
        message = input("Enter the message: ")
        SMSKeywords[keyword] = message

    return SMSKeywords

def printSMSKeywords(SMSKeywords):
    print("\nSMS Keywords and Messages in the Dictionary")
    for k, v in SMSKeywords.items():
        print(f"{k} : {v}")

def deleteSMSKeywords(SMSKeywords):
    keyword = input("\nEnter keyword for deletion: ")

    if keyword in SMSKeywords.keys():
        del SMSKeywords[keyword]
    else:
        print("\nKeyword not in dictionary")
    return SMSKeywords

def searchSMSKeywords(SMSKeywords):
    keyword = input("\nEnter keyword you want to search: ")

    if keyword in SMSKeywords.keys():
       print(keyword,"\t\t", SMSKeywords[keyword])
    else:
        print("\nKeyword not in dictionary")
    
def menu ():
    print("\n1. Add an SMS Keyword")
    print("2. Print all SMS Keywords")
    print("3. Delete an SMS Keyword")
    print("4. Search an SMS Keyword")
    print("0. Quit")
    choice = int(input("Your choice: "))
    return choice
#---------------------------------------------------------------------------------------
SMSKeywords = loadData("SMSKeywords.txt")

while True:
    choice = menu()
    if choice == 1:
        SMSKeywords = addSMSkeywords(SMSKeywords)
    elif choice == 2:
        printSMSKeywords(SMSKeywords)
    elif choice == 3:
        SMSKeywords = deleteSMSKeywords(SMSKeywords)
    elif choice == 4:
        searchSMSKeywords(SMSKeywords)
    elif choice == 0:
        print("\nThanks! Bye!")
        break
    else:
        print("Invalid choice:", choice)

storeData(SMSKeywords, "SMSKeywords.txt")

#-----------------------------------------------

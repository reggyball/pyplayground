# numbers = [int(input("Enter a number: ")) for i in range(int(input("How many items to average: ")))]

# def average(numbers):
#     return sum(numbers) / len(numbers)

# print("The average of the scores are ", average(numbers))
 
   
#--------------------------------------------------------------
# numbers = []
# num = input("Enter a number: ")
# while num.isnumeric():
#     numbers.append(int(num))
#     num = input("Enter a number: ")

# def average(numbers):
#     return sum(numbers)/len(numbers)

# print("The average is ", average(numbers))

#--------------------------------------------------------------
#compute for Surface area of cylinder

# r = float(input("Enter the radius: "))
# h = float(input("Enter the height: "))

# pi = 3.14

# area_circ = pi*(r**2)
# circumference = 2*pi*r
# area_rect = circumference * h
# sa_cyl = area_rect + (2*area_circ)
# print(sa_cyl)

# num = (15.6 // 3.3 + (4.2 * 2.9))
# print(num)

# num2 = 15.6 //3.3
# print(num2)

# num = (10 * 2 - 3 * 2 + 4 > 10)
# print(num)

# Converts C to F

# C = float(input("Enter temperature in C: "))
# F = (C * 9/5) + 32
# print("Temperature in Fahrenheit: ", F)


# a = 45
# b = 98

# The output should be:

# a = 98
# b = 45

#Swaps a &b 
# a = 45
# b = 98

# a, b = (b, a)
# print("a =", a)
# print("b =",b)

# a = 45
# b = 98

# a = a+b
# print(a)
# b = a-b
# print(b)
# a = a-b
# print(a, b)

# -----------------------------------------------
#request user input for the number of terms and typecast as int
n = int(input("Enter a number: "))

#start value of pi at 3
k = 3
#for loop will iterate until n+1 (n+1 to include n). initializes counter to 1, checks condition (counter is less than n+1), goes to next line
for i in range (1, n+1):  
    print("{:<10} {:<10}".format(i, k))     #prints iteration count and current value of pi
    j = i*2                                 #denominator prep, set i * 2 so that denominator series will start at 2 onwards
    x = (j * (j+1) * (j+2)) * -(-1)**i      #denominator(x) is the product of coefficients, multiplied to -1 raised to i 
    k = k + 4/x
    
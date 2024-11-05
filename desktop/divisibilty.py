# Write a program that determines if the integer input of the user is divisible by 2 only, divisible by 3 only, divisible by both 2 and 3, 
# and not divisible by 2 and 3.

number = float(input("Number: "))
if number % 3 == 0 and number % 2 == 0:
    print("Divisible by both 2 and 3")
elif number % 3 == 0:
    print("Divisible by 3")
elif number % 2 == 0:
    print("Divisible by 2")
else:
    print("Not divisible by 2 or 3")
# while(True):  					 #while user input is not numeric will keep asking for age
# 	age = input("Enter age: ")   #asks user for input (age)
# 	if age.isnumeric():          #if age is valid, will exit while loop and print age in line 9
# 	    break
# 	else:                        #otherwise, will print error message and continue the while loop
# 		print("Input age in numeric form")

# print("Age:", age)

# while(True):  			   					   #while user input is not in the valid options, keep asking
#     sex = input("Enter sex (female/male): ")   #asks user for input
#     if sex in ["female", "male"]:              #if input sex is one of the valid options, exit loop
#         break
#     else:                       			   #otherwise, will print error message and continue the while loop
#         print("Please input only either female or male")

# print("Sex:", sex)

# -------------------------------------------------------------------------------------------------------------
# import re 

# mobile_pattern = r'^(?:\+639|09)\d{9}$' 
# while(True):  			   									#while user input is not in the valid options, keep asking
#     mobilenumber = input("Enter mobile number: ")   		#asks user for input
#     if re.match(mobile_pattern, mobilenumber) is not None:  #if input follows the pattern mobile_pattern
#         break
#     else:                       							 #otherwise, will print error message and continue the while loop
#         print("Please input a valid mobile number (+639xxxxxxxxx / 09xxxxxxxxx)")

# print("Mobile Number:", mobilenumber)

# 0000

# -------------------------------------------------------------------------------------------------------------
# def print10():
#     for i in range(1, 11):
#         print(i)

# z = print10
# print(z)
# -------------------------------------------------------------------------------------------------------------
# printStr = "test"
# def printTest():
#     print(printStr)

# def printocal(str):
#     print(str)


# printTest()

# -------------------------------------------------------------------------------------------------------------
# recursion
def foo (num1):
    if num1 <= 0:
        return 0
    return num1+foo(num1-1)

x = foo(int(input("n: ")))
print(x)
    
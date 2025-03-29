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

def fibonacci(max, nth=0, curr=0, next=1):
    if nth == max:
        return curr
    nth += 1
    return fibonacci(max, nth, next, curr+next) 

max = int(input("Enter n: "))
print(fibonacci(max=max))

# def fib(n):
#     if n == 1 or n == 0:
#         return n
    
#     return fib(n-1) + fib(n-2)

# n = int(input("Enter n: "))
# print(fib(n))
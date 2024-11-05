# Activity 5: Convert your program in Activity 4 that uses loops to compute the first n values in the Nilakantha series, 
# to a recursive function. 

# Here’s the skeleton of the program for this activity. 
# You will only supply the function body of the nilakantha function. 
# You are required to use recursion.

def nilakantha (n):
    # provide the code for this function
    # this function returns the nth value in the Nilakantha series
    if n == 1:
        return 3
    i = n-1
    j = i*2
    a = 4/(j * (j+1) * (j+2)) * -(-1)**i 
    return nilakantha(n-1) + a

# ask for an integer
n = int(input("Enter n: "))
print(f"Here are the first {n} values in the Nilakantha series: ")

# print the first n values in the Nilakantha series
for i in range (1, n+1):
    print (i, "\t", nilakantha(i))

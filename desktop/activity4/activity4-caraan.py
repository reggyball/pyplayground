#request user input for the number of terms/values and typecast as int
n = int(input("Enter n: "))

#start value of pi at 3 (ones place)
k = 3
print("Here are the first", n, "values in the Nilakantha series: ") 
#for loop(computes for decimals),
   # iterates (n) no of times. initializes counter to 1 and checks condition (counter(i) is less than n+1)
for i in range (1, n+1): 
    print("{:<10} {:<10}".format(i, k))     #prints padded iteration count(i) and current value of pi(k)
    j = i*2                                 #set coefficient (j) to i * 2 so that denominator series will start at i*2 onwards
    x = (j * (j+1) * (j+2)) * -(-1)**i      #(1)    
    k = k + 4/x                             #updates value of (k) which is k + computed decimal or 4/denominator
    

 # (1) denominator(x) is the product of coefficients, starting at j until j+2 multiplied by -(-1^i) 
    # (-1^i) purpose is to alternate the sign of x (based on whether i is odd or even), -(-1^i) starting at a positive value
    # different signs of x every iteration alternates the operation needed (addition and subtraction) to compute for the decimal values as dictated by the N.formula
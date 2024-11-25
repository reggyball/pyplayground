#  ###################################### Beginner Series #1 School Paperwork ###########################################
def paperwork(n,m):
    return n * m if n > 0 and m > 0 else 0                   #ternary conditional operator/short-hand if else

#testcases
print(paperwork(5,5))   #25
print(paperwork(1,2))   #2
print(paperwork(-5,5))  #0
print(paperwork(5,-5))  #0
print(paperwork(-5,-5)) #0
print(paperwork(5,0))   #0, 

#  ###################################### BOOLEAN TO STRING #############################################################
# def boolean_to_string(b):
#     return "True" if b == True else "False"                 #ternary conditional operator/short-hand if else

# #testcases
# print(boolean_to_string(True))#"True"
# print(boolean_to_string(False)) #"False"

# ###################################### SUM OF POSITIVE ###############################################################
# def positive_sum(arr):                                             
#     if not arr:                                                 #if the if statement is false it will go to else block
#            return 0                                             #if true(EMPTY) then will return 0
#     else:
#         return sum(number for number in arr if number > 0)          #generator expression to iterate over each number in arr and includes only those numbers that are greater than 0.
#                                                                     #The sum function then adds up these positive numbers and returns the result.
    
# #testcases    
# print(positive_sum([1,2,3,4,5])) #15
# print(positive_sum([1,-2,3,4,5])) #13
# print(positive_sum([-1,2,3,4,-5])) #9

# if not arr => when arr is not empty, arr = T -> if not (T) = F -> when false will return sum
# when arr is empty, arr = F -> if not (F) = T -> when true will return 0

# ###################################### TWO OLDEST AGES ###############################################################
# def two_oldest_ages(ages):
#     ages.sort()                                 #sort input list into ascending order
#     return ages[-2:]                            #slice the last 2 element of the list and return it

# #alternative solution
# # def two_oldest_ages(ages):
# #     return sorted(ages)[-2:]


# #Sample input
# (two_oldest_ages([1, 5, 87, 45, 8, 8]), [45, 87])
# (two_oldest_ages([6, 5, 83, 5, 3, 18]), [18, 83])
# (two_oldest_ages([10, 1]), [1, 10])

# ######################################## HELP THE BOOKSELLER ###########################################################
# def stock_list(stocklist, categories): 
#     if stocklist != [] and categories != []:               #if any of input contains values proceed
#         totals = {}                                        #create an empty dictionary
#         for letter in categories:                          #loop over each letter 
#             totals[letter] = 0                             #assign each letter as a key and assign 0 as a value
#             for word in stocklist:                         #loop over each word/phrase in stocklist
#                 if letter == word[0]:                      #if letter in category matches first letter of phrase:
#                     space = word.index(' ')                #find spaces in the phrase
#                     val = word[space+1:]                   #slice the number in the phrase
#                     totals[letter] += int(val)             #assign as value to the key, sum if same key                                                               
#         return " - ".join(f"({key} : {value})" for key, value in totals.items())
#     else:                                                   # if any input is empty, return an empty string
#         return ""


# #sample inputs
# b = []
# # c = []

# # b = ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"]
# c = ["A", "B", "C", "D", "E"]
# print(stock_list(b,c))

# #------------------------------------------------------------------------------------------------------
# #using concepts of truthy/falsy/comprehensions
# def stock_list(stocklist, categories):
#     if not stocklist or not categories:
#         return ""
#     return " - ".join(
#         "({} : {})".format
#          (category,sum(int(item.split()[1]) for item in stocklist if item[0] == category)) for category in categories)
# ########################################################################################################################


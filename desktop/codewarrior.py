###################################### TWO OLDEST AGES ###############################################################
def two_oldest_ages(ages):
    ages.sort()                                 #sort input list into ascending order
    return ages[-2:]                            #slice the last 2 element of the list and return it

#alternative solution
# def two_oldest_ages(ages):
#     return sorted(ages)[-2:]


#Sample input
(two_oldest_ages([1, 5, 87, 45, 8, 8]), [45, 87])
(two_oldest_ages([6, 5, 83, 5, 3, 18]), [18, 83])
(two_oldest_ages([10, 1]), [1, 10])

######################################## HELP THE BOOKSELLER ###########################################################
def stock_list(stocklist, categories): 
    if stocklist != [] and categories != []:               #if any of input contains values proceed
        totals = {}                                        #create an empty dictionary
        for letter in categories:                          #loop over each letter 
            totals[letter] = 0                             #assign each letter as a key and assign 0 as a value
            for word in stocklist:                         #loop over each word/phrase in stocklist
                if letter == word[0]:                      #if letter in category matches first letter of phrase:
                    space = word.index(' ')                #find spaces in the phrase
                    val = word[space+1:]                   #slice the number in the phrase
                    totals[letter] += int(val)             #assign as value to the key, sum if same key                                                               
        return " - ".join(f"({key} : {value})" for key, value in totals.items())
    else:                                                   # if any input is empty, return an empty string
        return ""


#sample inputs
b = []
# c = []

# b = ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B", "C", "D", "E"]
print(stock_list(b,c))

#------------------------------------------------------------------------------------------------------
#using concepts of truthy/falsy/comprehensions
def stock_list(stocklist, categories):
    if not stocklist or not categories:
        return ""
    return " - ".join(
        "({} : {})".format
         (category,sum(int(item.split()[1]) for item in stocklist if item[0] == category)) for category in categories)
########################################################################################################################
''' New Member '''
def open_or_senior(data):
  output = []

  for member in data:
      if member[0] >= 55 and member[1] > 7:
          output.append("Senior")
      else:
          output.append("Open")

  return output


def open_or_senior3(data):
  output = []
  for (age, handicap) in data:
    if age >= 55 and handicap > 7:
      output.append("Senior")
    else:
      output.append("Open")
  return output

print(open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)]))
print(open_or_senior3([(45, 12),(55,21),(19, -2),(104, 20)]))

def openOrSenior2(data):
  return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]

################################################################################################
''' String ends with '''
# def solution(text, ending):
#     length = len(ending)
#     if text[-length:] == ending:
#         return True
#     return False

# print(solution( "samurai", "ai"))
# print(solution( "ninja","ja"))
# print(solution( "sensei","i"))
# print(solution( "abc", "abc"))
# print(solution( "sumo", "omo"))

# def solution2(string, ending):
#     return string.endswith(ending)

# ##################################### VOWEL COUNT ###################################################################
# vowels = ['a', 'e', 'i', 'o', 'u']

# def get_count(sentence):
#   return sum(sentence.lower().count(vowel) for vowel in vowels)

# print(get_count("aeiou"))
# print(get_count("bcdfghjklmnpqrstvwxz y"))
# print(get_count(""))
# print(get_count("abracadabra"))
# print(get_count("Regina Ann"))

##################################### STRANGE MARKET ###################################################################
# def is_loch_ness_monster(string):
#     if any(phrase in string for phrase in keywords):
#         return True 
#     else:
#         return False

# # keywords = ["tree fiddy", "3.50", "three fifty"]

# # #alternative
# def is_loch_ness_monster(string):
#     return not not [keyword for keyword in keywords if keyword in string]

#testcases
# print(is_loch_ness_monster("Your girlscout cookies are ready to ship. Your total comes to tree fiddy"))
# print(is_loch_ness_monster("Howdy Pardner. Name's Pete Lexington. I reckon you're the kinda stiff who carries about tree fiddy?"))
# print(is_loch_ness_monster("I'm from Scottland. I moved here to be with my family sir. Please, $3.50 would go a long way to help me find them"))
# print(is_loch_ness_monster("Yo, I heard you were on the lookout for Nessie. Let me know if you need assistance."))
# print(is_loch_ness_monster("I will absolutely, positively, never give that darn Loch Ness Monster any of my three dollars and fifty cents"))
# print(is_loch_ness_monster("Did I ever tell you about my run with that paleolithic beast? He tried all sorts of ways to get at my three dolla and fitty cent? I told him 'this is MY 4 dolla!'. He just wouldn't listen."))
# print(is_loch_ness_monster("Hello, I come from the year 3150 to bring you good news!"))
# print(is_loch_ness_monster("By 'tree fiddy' I mean 'three fifty'"))
# print(is_loch_ness_monster("I will be at the office by 3:50 or maybe a bit earlier, but definitely not before 3, to discuss with 50 clients"))
# print(is_loch_ness_monster(""))

#TTTFFFFTFF

##################################### TRAFFIC JAM ###################################################################
# def traffic_jam(traffic, green_light_duration):
#     reversed = traffic[::-1]

#     return count

# print(traffic_jam([15, 2, 8, 7], 16))
# print(traffic_jam([12, 5, 8, 1], 16))
# print(traffic_jam([5, 5, 2, 4], 5))

   
##################################### REVERSED SEQUENCE ##############################################################
# def reverse_seq(n):
#     return list(range(1, n+1))[::-1]

# #alternative
# def reverse_seq(n):
#     return list(range(n, 0, -1))

# #testcase
# print(reverse_seq(5)) #[5,4,3,2,1]

# ###################################### Convert a string to an array #################################################
# def string_to_array(s):
#     return s.split(" ")                 #" " - replaces output ng empty string; if empty by default split removes all whitespace

# #testcases
# print(string_to_array("Robin Singh"))         #["Robin", "Singh"])
# print(string_to_array("CodeWars"))           #["CodeWars"])
# print(string_to_array("I love arrays they are my favorite")) #["I", "love", "arrays", "they", "are", "my", "favorite"])
# print(string_to_array("1   2 3"))                #["1", "2", "3"])
# print(string_to_array(""))                     # [""]

# ###################################### Beginner Series #1 School Paperwork ###########################################
# def paperwork(n,m):
#     return n * m if n > 0 and m > 0 else 0                   #ternary conditional operator/short-hand if else

# #testcases
# print(paperwork(5,5))   #25
# print(paperwork(1,2))   #2
# print(paperwork(-5,5))  #0
# print(paperwork(5,-5))  #0
# print(paperwork(-5,-5)) #0
# print(paperwork(5,0))   #0, 

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


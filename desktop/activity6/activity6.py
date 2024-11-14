# Activity 6: Create a program that converts a word into its Pig Latin equivalent. The goal of converting a word to Pig Latin is to conceal the words from those who do not know the rules.

# 1. If the string contains special characters, return the string as is.
# 2. Capitalize the first character of the newly-formed word.
# 3. If the original word contains both consonants and vowels but starts with a consonant, take the letters before the first vowel in the word and move them to the end of the word. Then append "ay" to it.
# 4. If the original word started with a vowel, add an "X" to the beginning of the newly-formed word. Then append "ay" to it.
# 5. If the word has only one letter, append "lyay" to it, regardless of whether it's a vowel or a consonant.
# 6. If the original word has no vowel, capitalize the first character and return the word.

# Input: wordlist.txt - a text file containing a the words that will be converted to Pig Latin
# Output: the program prints two lists: the list of original words and the list of converted words
########################################################
# The pigLatin function converts a string to Pig Latin given the rules. 
# The function should return the converted word
# MODIFY ONLY THIS PART OF THE PROGRAM
########################################################

def pigLatin (s):
#initialize consonant,vowels,empty strings and list. Consonants and vowels will serve as the basis for the conditions. Empty strings,lists as containers
    consonants = "bcdfghjklmnpqrstvwxyz"           
    vowels = "aeiou"
    pig_fin = ""
    temp_list = []
    detect_vowels = []

#condition no. 5 and no.1
#checks if word length is 1 and if word contains special characters 
    if len(s) != 1:
        for i in s:                                                                        #if current letter(i) is not in vowel or consonant, hence a special character
            if (i not in consonants) and (i not in vowels):                                 #return the original word 
                return s                                                                   
            else:                                                                          #otherwise, append current letter to temp_list 
                temp_list.append(i)
    else:                                                                                  #if word length is 1, then return capitalized letter +suffix 'ilyay'
        return s.upper() + "lyay"

           
#detects if the word(now casted as a 'list' in temp_list) has vowels
    for i in vowels:
        if i in temp_list:
            detect_vowels.append(temp_list.index(i))

#conditions no. 2,3,4,6
    detect_vowels.sort()                                                                    #sort to obtain first instance of vowel, first element = first instance of vowel except for 0
    if len(detect_vowels) == 0:                                                             #condition 6,2. if no vowels recorded on list (list is empty) hence, return original word with capitalized first letter
        return s.capitalize()
    elif 0 in detect_vowels:                                                                #condition 4. if 0 is recorded in list it means first letter is a vowel->  return word starting with X with suffix 'ay'
        pig_fin = "X" + s.lower() + "ay"
        return pig_fin
    elif len(detect_vowels) != len(s):                                                      #condition 3,2. if at this point the length of detect_vowels and the original word (s) is unequal, meaning the word is a mix of consonants and vowels.                                                                               
        first_vow = detect_vowels[0]                                                           #first element in detect_vowel is the index of first instance of vowel in the word(s) --> gives the location of the first vowel (enables slicing at the right index to meet condition 3)
        pig_fin = s[first_vow:] + s[:first_vow] + "ay"                                         #concatenation of the final word, slice of [first_vowel to end] + [start to first vowel-1] + suffix ay" 
        return pig_fin.capitalize()                                                            #capitalize the final concatenated word and return it
    
########################################################
# DO NOT MODIFY THIS PART OF THE PROGRAM
########################################################

# Read the file wordlist.txt
wordFile = open("wordlist.txt", "r")

# Save each line of the file in a list, exclude the new line character ('\n')
wordList = [line.replace("\n", "") for line in wordFile.readlines()]

# Convert each word to Pig Latin then append each converted word to a list
pigLatinWords = [pigLatin(word) for word in wordList]

# Print the original word and the converted words
print ("Pig-latin version of the words: ")
for i in range(0, len(wordList)):
    print (wordList[i] + " --> " + pigLatinWords[i])

########################################################
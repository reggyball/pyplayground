#Initialize container and alphabet lists 
key_list = []
stopwords_list = []
elphaba_list = "abcdefghijklmnopqrstuvwxyz"                                                   

#LOAD TEXT FILES CONTENT AND COPY TO LISTS

#copy stop words from text file to stop_words list   
with open ("stop_words.txt", "r", encoding="utf-8") as file:                                #Text file is opened at read mode with UTF-8 encoding to ensure program reads text files with any character                              
    for line in file:                                                                       #text file is read per line
        stop_word = line.strip()                                                            #each word per line is extracted as a 'stop_word' by removing any trailing spaces
        stopwords_list.append(stop_word)                                                    #each stop word is appended in the stopwords_list
                                                                                            #when finished processing, text file is automatically closed due to "with open" syntax

#content of article.txt is processed and appended to key_list
with open("article.txt", "r") as file:                                                      #Text file is opened at read mode, automatically closed after use
    for line in file:                                                                       #Processing will be per each line:
       for word in line.split():                                                               #To extract words per line, split at spaces
           word = word.lower().strip()                                                         #Each word will be in lowercase and removed of trailing spaces

#to remove special characters and punctuations in word
           term = ""                                                                           #declare an empty string "term"
           for letter in word:                                                                 #Each letter of the word will be assesed if in the alphabet list, 
                if letter in elphaba_list:                                                        #if yes each letter will be concatenated to 'term' string
                    term += letter                                                                      

#check if term is empty and in stop_words                                                                                                       
           if term and term not in stopwords_list:                                                #if term is not empty and not in stop_words list then it will be appended to the key_list
                key_list.append(term)                                                             #key_list will contain all the valid terms in the document (words less the punctuation and special chars, and not in stop words)
                

#term_freq(nt, nd) = no of times term appeared in doc/no of terms in doc

#ASSEMBLING THE DICTIONARY
term_freq = {}

nd = len(key_list)                                                                            #nd = no of terms in the document is the number of elements in the key_list

#processes each term in key_list and creates key:value pair for the dict
while len(key_list) > 0:                                                                      #while the key_list contains a term, continue to process                                                                                                                         
    term = key_list[0]                                                                         #each term will be called by calling the first element of the list
    nt = key_list.count(term)                                                                  #nt = since the list contains all valid terms in document, the no of instance of a term in the list is the nt
    tf = nt/nd                                                                                 #compute for term frequency
    term_freq[term] = {'count': nt, 'tf': tf}                                                  #assemble the dict, where each term and its counts are the key:val, respectively

    while term in key_list:                                                                     #remove processed words in the list to avoid duplicate processing of the term
        key_list.remove(term)

term_freq = dict(sorted(term_freq.items()))                                                     #sort the dictionary alphabetically

#copy created dictionary to term_freq text
with open("term_frequency.txt", "w") as file:                                                   #open text file in write mode/create if not yet available
    for keyword, value in term_freq.items():                                                    #for each key:val pair in dictionary,
        file.write(f"'{keyword}' : {value}\n")                                                      #copy to the text file given the format




        

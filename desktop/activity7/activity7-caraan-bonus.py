import math                                                                                                     
from pathlib import Path

#activity 7 as a function, calculates count, term frequency of each term in document
def termfreq(filename):
    key_list = []
    stopwords_list = []
    elphaba_list = "abcdefghijklmnopqrstuvwxyz"

    with open ("stop_words.txt", "r", encoding="utf-8") as file:
        for line in file:
            stop_word = line.strip()
            stopwords_list.append(stop_word)

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
         for word in line.split():
            word = word.lower().strip()

            term = ""
            for letter in word:
                    if letter in elphaba_list: 
                        term += letter

            if term and term not in stopwords_list:
                key_list.append(term)
                    
    term_freq = {}

    nd = len(key_list)

    while len(key_list) > 0:
        term = key_list[0]
        nt = key_list.count(term)
        tf = nt/nd
        term_freq[term] = {'count': nt, 'tf': tf}

        while term in key_list:
            key_list.remove(term)

    term_freq = dict(sorted(term_freq.items()))
    return term_freq


#To access directory of provided path
pathdir = input("Enter path directory (if unk, enter for default: current dir): ")
if '"' in pathdir:                                                                               # Remove double quotes from the provided directory path, if present
    pathdir = pathdir.replace('"', '')
if pathdir and pathdir[-1] != "/":                                                               # Ensure the path ends with a forward slash, if not already provided 
    pathdir += "/"

#Defaults pathdirectory as to current dir if no path was provided by the user
directory = Path(pathdir) if pathdir else Path.cwd()

#Obtain all filenames of text files inside the directory
file_list = [str(file).split("\\")[-1] for file in directory.glob("*.txt")]


tf_idf_dict = {}

#All filenames in file_list be extracted as key for the dictionary, values will be the counts returned by termfreq function
for filename in file_list: 
    tf_idf_dict[filename] = termfreq(pathdir+filename)                                              #argument used is (pathdir + filename) to provide direction on where to look for the filename

#Compute IDF for each term
#idf = log(total number of documents/number of documents with term t in it)

a = len(file_list)                                                                                  #a or the total number of documents

term_keys = []                                                                                  #To count the number of documents mentioning the term:
for key in tf_idf_dict.keys():                                                                      #For each document, all the terms (keys of the term-counts dict) are extracted and added to the term_keys list.
    term_keys += list(tf_idf_dict[key].keys())                                                      #Since term_keys collects terms from all documents, it contains duplicates whenever a term appears in multiple documents.
                                                                                                    #eg: The term appears in term_keys once for every document it is mentioned in.
                                                                                                    #hence, the no. of times the term appears in the term_keys is equivalent to the no. of documents term was mentioned. 

for key in tf_idf_dict.keys():                                                                          
    for term in tf_idf_dict[key].keys():                                                            #no. occurence of term in the list is equal to b
        b = term_keys.count(term)                                                                   #b or the number of documents with the term 
        idf = math.log(a/b)                                                                         #compute for idf; natural logarithim (log base e is used in formula calculation vs common log(logbase10)) is used in the formula
        tf_idf_dict[key][term]['idf'] = idf                                                         #update the term values to include the idf



with open("TF-IDF.txt", "w") as file:                                                               #open text file in write mode/create if not yet available
    for keyword, term_freq in tf_idf_dict.items():                                                  #write the contents of the dictionary in the text file given the following format
        file.write(f"'{keyword}':  \n" )                                                            #writes document name                                    
        for term, value in term_freq.items():                                                                                               
            file.write(f"\t'{term}' : {value}\n")                                                   #writes term and counts 
        


import math
from pathlib import Path

def termfreq(filename):
    key_list = []
    stopwords_list = []
    elphaba_list = "abcdefghijklmnopqrstuvwxyz"

    with open ("stop_words.txt", "r", encoding="utf-8") as file:
        for line in file:
            stop_word = line.strip()
            stopwords_list.append(stop_word)

    with open(filename, "r") as file:
        for line in file:
         for word in line.split():
            word = word.lower().strip()

            term = ""
            for letter in word:
                    if letter in elphaba_list: 
                        term += letter

            if term in stopwords_list:
                continue
            else:
                    key_list.append(term)

    nd = len(key_list)
    term_freq = {}
    print(nd)

    while len(key_list) > 0:
        term = key_list[0]
        nt = key_list.count(term)
        tf = nt/nd
        term_freq[term] = {'count': nt, 'tf': tf}

        while term in key_list:
            key_list.remove(term)

    term_freq = dict(sorted(term_freq.items()))
    return term_freq


#Access directory 
pathdir = "./bonusfiles/"
directory = Path(pathdir)

#Obtain all filenames of text files inside the directory
file_list = [str(file).split("\\")[-1] for file in directory.glob("*.txt")]

tf_idf_dict = {}

for filename in file_list: 
    tf_idf_dict[filename] = termfreq(pathdir+filename)

# print(tf_idf_dict)

#idf = log(total number of documents/number of documents with term t in it)
a= len(file_list)

term_keys = []
for key in tf_idf_dict.keys():
    term_keys += list(tf_idf_dict[key].keys())

for key in tf_idf_dict.keys():
    for term in tf_idf_dict[key].keys():
        b = term_keys.count(term)
        idf = math.log(a/b)
        tf_idf_dict[key][term]['idf'] = idf

print(tf_idf_dict)
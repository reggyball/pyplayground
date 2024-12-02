key_list = []
stopwords_list = []
elphaba_list = "abcdefghijklmnopqrstuvwxyz"

with open ("stop_words.txt", "r", encoding="utf-8") as file:
    for line in file:
        stop_word = line.strip()
        stopwords_list.append(stop_word)

with open("article.txt", "r") as file:
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

with open("term_frequency.txt", "w") as file:
    for keyword, value in term_freq.items():
        file.write(f"'{keyword}' : {value}\n")


        

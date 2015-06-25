__author__ = 'SantoshPappachan'

import csv

final = []
with open("MetaData/kw_standards.csv","rb") as s:
    rstandards = csv.reader(s)
    wordlist = list(rstandards)

with open("MetaData/final_keyword.csv","rb") as k:
    keywords = csv.reader(k)
    keywordlist = list(keywords)


for word in wordlist:
    current = word[5].split()
    exceptFile = open("MetaData/exceptions.txt","wb")
    isThere = False
    remove = False
    replace = False
    replacement = ""
    for keyword in current:
        for frekey in keywordlist:
            if keyword == frekey[0]:
                isThere = True
                if frekey[2] != "":
                    replace = True
                    replacement = frekey[2]
                elif frekey[3] == "y":
                    remove = True
        if isThere == False:
            exceptFile.write(keyword + "\n")

        if remove == True:
            current[current.index(keyword)] = ""
        elif replace == True:
            current[current.index(keyword)] = replacement

        isThere = False
        remove = False
        replace = False
    final.append(' '.join(current))




with open("MetaData/final_kw_standards.csv","wb") as s:
    wstandards = csv.writer(s)
    i = 1

    while i < len(final):
        wordlist[i][6] = final[i]
        wstandards.writerow(wordlist[i])

        i += 1


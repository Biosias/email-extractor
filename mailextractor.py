# Version 0.2
# Next update with xls format exporting

print("Welcome to @Extractor\n")
adress = input("Enter name of the file for extraction: ")
outpu = input("Enter name for the output file: ")
OutFile = open(outpu + ".txt", "w")
adress = open(adress, "r")
adressa = adress.read()
filterChoose = False
def remBor(adressa):
    remove = ['"', '=', '>', '<', '(', ')', '{', '}', '[', ']', '/', "%", '&', '!', '?', '|', ":", ",", ";",]
    remove2 = [" @", " @ ", "@ ", ]
    for a in remove:
        adressa = adressa.replace(a, " ")
    return adressa
def filterMenu():
    if input("Do you want to use additional filters? y/n: ") == "y":
        provFilter = input("Enter word which you want to flter: ")
        provFilter = provFilter.lower()
        return provFilter
    else:
        return 0
def extrMail(adressa, provFilter, filterChoose):
    adArray = adressa.split()
    adArrayb = []
    for word in adArray:
        if word == "@":
            word = word.replace(word, "")
        if word[:1] == "@":
            word = word.replace(word, "")
            for wordb in adArrayc:
        if "@" in word:
            if filterChoose == True:
                    if provFilter in word:
                        adArrayb.append(word)
            else:
                adArrayb.append(word)
    adArrayc = set(adArrayb)
            OutFile.write(wordb + "\n")
            print(wordb + "\n")
adressa = remBor(adressa)
provFilter = filterMenu()
if provFilter != 0:
    filterChoose = True
extrMail(adressa, provFilter, filterChoose)
print("Done!")

# Python 3.5
# Version 0.2
# Next update with xls format exporting

print("Welcome to @Extractor\n")
adress = input("Enter name of the file for extraction: ")
outpu = input("Enter name for the output file: ")
adress = open(adress, "r")
adressa = adress.read()
filterChoose = False


def remBor(adressa):
    remove = ['"', '=', '>', '<', '(', ')', '{', '}', '[', ']', '/', "%", '&', '!', '?', '|', ":", ",", ";",]
    remove2 = [" @", " @ ", "@ ", ]
    rozdelEma = ["<td>", "</td>" ]
    nahradaZav = ["(a)", "(@)", "(at)"]
    for a in nahradaZav:
        adressa = adressa.replace(a, "@")
    for b in rozdelEma:
        adressa = adressa.replace(b, "")
    for c in remove:
        adressa = adressa.replace(c, " ")
    return adressa

def filterMenu():
    if input("Do you want to use additional filters? y/n: ") == "y":
        provFilter = input("Enter which word you want to flter: ")
        provFilter = provFilter.lower()
        return provFilter
    else:
        return 0

def format():
    form = input("Choose ouput format(1-2)\nTXT 1\nCSV 2\n: ")
    if form == "1":
        return ".txt"
    else:
        return ".csv"

def extrMail(adressa, provFilter, filterChoose, format):
    adArray = adressa.split()
    adArrayb = []
    for word in adArray:
        if word == "@":
            word = word.replace(word, "")
        if word[:1] == "@":
            word = word.replace(word, "")
        if "@" in word:
            if "." in word:
                if filterChoose == True:
                    if provFilter in word:
                        adArrayb.append(word)
                else:
                    adArrayb.append(word)
    adArrayc = set(adArrayb)
    for wordb in adArrayc:
            OutFile.write(wordb + "\n")
            print(wordb + format)


format = format()
OutFile = open(outpu + format, "w")
if format == ".txt":
    format = "\n"
else:
    format = ",\n"
adressa = remBor(adressa)
provFilter = filterMenu()
if provFilter != 0:
    filterChoose = True
extrMail(adressa, provFilter, filterChoose, format)
print("Done!\n\nGithub: https://github.com/Biosias/email-extractor.git")

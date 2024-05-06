from string import ascii_lowercase

listOfLetters = list(ascii_lowercase)

for i in listOfLetters:
    for j in listOfLetters:
        if i != j:
            print(i + j)
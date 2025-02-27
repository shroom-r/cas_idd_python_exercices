import re

text = open('./swan.txt').read()

letterCount = {}

for letter in text:
    letter = letter.lower()
    # Check if letter is letter (ignore accents and other chars)
    matchLetter = re.search("[a-z]", letter)
    if matchLetter:
        try:
            letterCount[letter] += 1
        except KeyError:
            letterCount[letter] = 1

letterCount = dict(sorted(letterCount.items(), key=lambda item: item[1], reverse=True))

totalCount = sum(letterCount.values())
for letter, count in letterCount.items():
    print(letter + ": " + str(round(100*count/totalCount,2)) + "%" )
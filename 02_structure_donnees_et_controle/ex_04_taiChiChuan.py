words = [w.strip() for w in open('french_words.txt', encoding='utf-8')]

letters = input("Vos lettres : ").lower()

letterMustBeginWith = letters[0]
lettersMustContain = letters[1:]

wordsToPrint = []

for word in words:
    beginsWithLetter = word[0].lower() == letterMustBeginWith
    containsLetters = all(letterToCheck in word.lower() for letterToCheck in lettersMustContain)
    if (beginsWithLetter and containsLetters):
        wordsToPrint.append(word)

print(f"Mots qui commencent par {letterMustBeginWith} et qui contiennent {",".join(lettersMustContain)} (dans n'importe quel ordre) :")
for word in wordsToPrint:
    print(word)
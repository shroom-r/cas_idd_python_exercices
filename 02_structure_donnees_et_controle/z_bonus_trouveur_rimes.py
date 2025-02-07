words = [w.strip() for w in open('french_words.txt', encoding='utf-8')]

letters = input("Vos lettres : ").lower()

wordsToPrint = []

for word in words:
    rimeLength = len(letters)
    if (word[-rimeLength:] == letters):
        wordsToPrint.append(word)

print(f"Mots qui finissent par {letters} :")
for word in wordsToPrint:
    print(word)
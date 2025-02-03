import re
import unicodedata

words = [w.strip() for w in open('french_words.txt', encoding='utf-8')]


inputWord = input("Entrez un mot : ").lower()
while len(inputWord)>0:
    normalizedInput = inputWord
    # Replace accents from input with non accented chars
    normalizedInput = unicodedata.normalize('NFKD', normalizedInput)
    normalizedInput = ''.join([c for c in normalizedInput if not unicodedata.combining(c)])

    # Remove all non letter chars from input
    normalizedInput = re.sub(r'[^a-zA-ZÀ-ÖØ-öø-ÿ]','',normalizedInput)

    normalizedInput = "".join(sorted(normalizedInput))

    for word in words:
        normalizedWord = word
        # Replace accents from word with non accented chars
        normalizedWord = unicodedata.normalize('NFKD', normalizedWord)
        normalizedWord = ''.join([c for c in normalizedWord if not unicodedata.combining(c)])
        # Remove all non letter chars from input
        normalizedWord = re.sub(r'[^a-zA-ZÀ-ÖØ-öø-ÿ]','',normalizedWord)

        normalizedWord = "".join(sorted(normalizedWord))

        # Clean and normalize word
        if (normalizedWord == normalizedInput):
            print(word)
    
    inputWord = input("Entrez un mot : ").lower()
else:
    print("Au revoir")


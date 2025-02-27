import re
import unicodedata
from pathlib import Path

path = Path(__file__).parent.parent

words = [w.strip() for w in open(str(path) + '/02_structure_donnees_et_controle/french_words.txt', encoding='utf-8')]

anagrams={}

for word in words:
    normalizedWord = word
    # Replace accents from word with non accented chars
    normalizedWord = unicodedata.normalize('NFKD', normalizedWord)
    normalizedWord = ''.join([c for c in normalizedWord if not unicodedata.combining(c)])
    # Remove all non letter chars from input
    normalizedWord = re.sub(r'[^a-zA-ZÀ-ÖØ-öø-ÿ]','',normalizedWord)
    normalizedWord = "".join(sorted(normalizedWord))
    try:
        anagrams[normalizedWord].append(word)
    except KeyError:
        anagrams[normalizedWord] = [word]

inputWord = input("Entrez un mot : ").lower()
while len(inputWord)>0:
    normalizedInput = inputWord
    # Replace accents from input with non accented chars
    normalizedInput = unicodedata.normalize('NFKD', normalizedInput)
    normalizedInput = ''.join([c for c in normalizedInput if not unicodedata.combining(c)])

    # Remove all non letter chars from input
    normalizedInput = re.sub(r'[^a-zA-ZÀ-ÖØ-öø-ÿ]','',normalizedInput)

    normalizedInput = "".join(sorted(normalizedInput))

    # Clean and normalize word
    try:
        print(anagrams[normalizedInput])
    except KeyError:
        print("Aucun anagrame trouvé")
    
    inputWord = input("Entrez un mot : ").lower()
else:
    print("Au revoir")


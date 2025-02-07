words = [w.strip() for w in open('french_words.txt', encoding='utf-8')]

# Nombre de mots
wordsCount = len(words)

fourLetterWordsCount = 0
wordsBeginningWithZ = 0
wordsContainingZ = 0
wordsBeginningWithAAndFinishingWithS = 0
for word in words:
    # Nombre de mots de 4 lettres
    if (len(word)==4):
        fourLetterWordsCount += 1
    # Mots commençant par Z
    if (word[0].lower() == "z"):
        wordsBeginningWithZ += 1
    # Mots contenant la lettre Z
    if ("z" in word.lower()):
        wordsContainingZ += 1
    # Mots commençant par a et finissant par s
    if (word[0].lower() == "a" and word[-1].lower() == "s"):
        wordsBeginningWithAAndFinishingWithS += 1

print ( \
f"""La liste de mots contient :
\t- {wordsCount} mots
\t- {fourLetterWordsCount} mots de 4 lettres
\t- {wordsBeginningWithZ} mots commençant par Z
\t- {wordsContainingZ} mots contenant Z
\t- {wordsBeginningWithAAndFinishingWithS} mots commençant par A et finissant par S
""")
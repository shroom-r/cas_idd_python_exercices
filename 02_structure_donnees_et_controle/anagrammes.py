words = [w.strip() for w in open('french_words.txt', encoding='utf-8')]


inputWord = input("Entrez un mot : ").lower()
while len(inputWord)>0:
    sortedInput = sorted(inputWord)

    for word in words:
        if (sorted(word.lower()) == sortedInput):
            print(word)
    
    inputWord = input("Entrez un mot : ").lower()
else:
    print("Au revoir")


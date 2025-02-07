import random

words = [w.strip() for w in open('french_words.txt', encoding='utf-8')]
penduAscii = [
"""
=========
""",
"""
      +
      |
      |
      |
      |
      |
=========
""",
"""
  +---+
      |
      |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  0   |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  0   |
  |   |
      |
      |
=========
""",
"""
  +---+
  |   |
  0   |
 /|   |
      |
      |
=========
""",
"""
  +---+
  |   |
  0   |
 /|\\  |
      |
      |
=========
""",
"""
  +---+
  |   |
  0   |
 /|\\  |
 /    |
      |
=========
""",
"""
  +---+
  |   |
  0   |
 /|\\  |
 / \\  |
      |
=========
""",
]

print("Bienvenue au jeu du pendu !")
print(penduAscii[-1])

print("\nDevinez le mot")

randomIndex = random.randint(0,len(words)-1)
randomWord = words[randomIndex]

wordLength = len(randomWord)

print(randomWord)

tryCount = 0

partialString = " ".join("_"*wordLength)
guessArray = []
print(f"\n{penduAscii[tryCount]}")
while tryCount < len(penduAscii)-1:
    print("\n" + partialString)
    guess = input("Entrez une lettre: ")

    # Quit programm if input is 'quit'
    if guess.lower() == "quit":
        exit()

    # If guess has more than one letter, ask for only one
    if len(guess) > 1:
        print("Une seule lettre par tour")
        continue
    
    # If letter has already been guessed, continue loop
    if guess in guessArray:
        print("Vous avez déjà essayé cette lettre !")
        continue

    # append new guess to guess array
    guessArray.append(guess)

    # Check if guess is in randomWord
    # On yes, build new string with found letters
    # On no, increment try count and loop
    
    partialString = ""
    for letter in randomWord:
        if (letter in guessArray):
            partialString += letter
        else:
            partialString += "_"
    if guess not in randomWord:
        tryCount += 1
    
    partialString = " ".join(partialString)

    # Count "_" in partialString. If there is none, game is won
    if ("_" not in partialString):
        print(partialString)
        print("Bravo !")
        break

    print(f"\n{penduAscii[tryCount]}")
    # print("\n" + partialString)

else:
    # If loop ends 
    print("Perdu !")

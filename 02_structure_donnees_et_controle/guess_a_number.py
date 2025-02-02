import random

numToGuess = random.randint(1,10)

print("Devinez un nombre entre 1 et 10")

while True:
    guess = int(input("Votre proposition: "))
    if guess < numToGuess:
        print("Non, plus")
    elif guess > numToGuess:
        print("Non, moins")
    else:
        print("Bravo")
        break
import random

numToGuess = random.randint(1,10)

print("Devinez un nombre entre 1 et 10")

while True:
    try:
        guess = int(input("Votre proposition: "))
    except ValueError:
        print("La valeur entrée n'est pas un nombre. Réessayez.")
        continue
    if guess < numToGuess:
        print("Non, plus")
    elif guess > numToGuess:
        print("Non, moins")
    else:
        print("Bravo")
        break
import random

correctCount = 0

while correctCount <5:
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    reponse = int(input(f"{num1} x {num2} = "))
    if (reponse == num1*num2) :
        print("Bravo")
        correctCount+=1
    else:
        print("Non, ré-essayez")

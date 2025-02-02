import random

correctCount = 0

questions = []

for i in range(1,11):
    for j in range(1,11):
        questions.append([i,j])


while True:
    # print(questions)
    questionIndex = random.randint(0, len(questions)-1)
    # print("Index: " + str(questionIndex))
    questionArr = questions[questionIndex]
    tryCount = 0
    while True:
        num1 = questionArr[0]
        num2 = questionArr[1]
        reponse = int(input(f"{num1} x {num2} = "))
        if (reponse == num1*num2) :
            print("Bravo")
            if(tryCount==0):
                del questions[questionIndex]
            break
        else:
            print("Non, ré-essayez")
            tryCount+=1
    if len(questions) == 0:
        break

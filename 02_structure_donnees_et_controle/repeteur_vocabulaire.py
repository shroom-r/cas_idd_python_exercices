import random

print("Préparation du quizz")

questions = []

while True:
    question = input("Question (<entrer> pour terminer): ")
    if question == "":
        break
    answer = input("Réponse: ")

    questions.append({"question": question, "answer": answer})


print("\n==================================")

print("Début du quizz !")

remainingQuestions = questions[:]

while len(remainingQuestions) > 0:
    index = random.randint(0, len(remainingQuestions) -1)
    print(remainingQuestions)
    print(remainingQuestions[index]['question'])
    answer = input(">")

    if (answer == remainingQuestions[index]['answer']):
        print("Oui!")
        remainingQuestions.pop(index)
    else:
        print("Non!")
        continue
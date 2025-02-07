def mediane(*args):
    list = [*args]
    list.sort()
    listLength = len(list)
    if listLength % 2 == 0:
        # Even
        result = (list[int(listLength / 2)] + list[int(listLength / 2 - 1)]) / 2
    else:
        # Odd
        result = list[int((listLength - 1) / 2)]
    return result

listOfNumbers = []

print("Entrez un nombre par ligne, ligne vide pour terminer")
while n:=input():
    n = int(n)
    listOfNumbers.append(n)

medianeVal = mediane(*listOfNumbers)

print(f'Vous avez entré {len(listOfNumbers)} nombres; leur mediane est {medianeVal:.2f}')
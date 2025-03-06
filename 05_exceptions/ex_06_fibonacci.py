def is_fibonacci(n):
    
    try:
        # n = int(input("Entrer une valeur pour savoir si elle est dans la suite de fibonacci : "))
        n = int(n)
        if n < 0 :
            raise ValueError("")
    except ValueError:
        print("ValueError: This function only takes positive integers")
        return
    twoLast = [1,1]
    # print(twoLast[0])
    while twoLast[-1] <= n:
        # print(twoLast[1])
        nextNum = twoLast[0] + twoLast[1]
        twoLast[0] = twoLast[1]
        twoLast[1] = nextNum
    if twoLast[0] == n:
        print(f"{n} est dans la suite de Fibonacci")
    else:
        print(f"{n} n'est pas das la suite de Fibonacci")

while val:=input("Entrez une valeur (vide pour quitter) :"):
    if val == "":
        break
    try:
        is_fibonacci(val)
    except:
        continue
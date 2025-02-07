def fibonacci(n):
    twoLast = [1,1]
    print(twoLast[0])
    while twoLast[-1] <= n:
        print(twoLast[1])
        nextNum = twoLast[0] + twoLast[1]
        twoLast[0] = twoLast[1]
        twoLast[1] = nextNum

n = int(input("Nombre limite : "))
fibonacci(n)
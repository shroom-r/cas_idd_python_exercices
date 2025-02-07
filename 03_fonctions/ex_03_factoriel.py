def fact(n):
    temp = n
    while n > 1:
        temp = temp * (n-1)
        n -= 1
    return temp
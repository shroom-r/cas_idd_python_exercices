def fact(n):
    ''' Factorielle, version itérative '''
    result = 1

    for i in range(2, n + 1):
        result *= i

    return result

def fact2(n):
    ''' Factorielle, version récursive '''
    if n == 1:
        return 1
    
    return n * fact2(n-1)
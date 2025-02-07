from time import sleep

def countdown(n = 10):
    while n > 0:
        print(f'Il reste {n} secondes.')
        n -= 1
        sleep(1)
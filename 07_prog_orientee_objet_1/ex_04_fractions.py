from math import gcd

class Fraction:
    def __init__(self, num, denom = 1):
        # Simplify

        simplificationFactor = gcd(num,denom)
        self.num = int(num / simplificationFactor)
        self.denom = int(denom / simplificationFactor)

    def display(self):
        strNum = f'{self.num}'
        strDenom = f'/{self.denom}' if self.denom != 1 else ''
        print(strNum + strDenom)

    def neg(self):
        return Fraction(self.num * -1, self.denom)
    
    def add(self, fraction):
        num = int(self.num * fraction.denom + fraction.num * self.denom)
        denom = int(self.denom * fraction.denom)
        return Fraction(num, denom)

    def sub(self, fraction):
        num = int(self.num * fraction.denom - fraction.num * self.denom)
        denom = int(self.denom * fraction.denom)
        return Fraction(num, denom)

    def mul(self, fraction):
        num = int(self.num * fraction.num)
        denom = int(self.denom * fraction.denom)
        return Fraction(num, denom)
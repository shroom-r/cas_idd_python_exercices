'''
This module provides a class for generating fractions.
Example of use : 
>>> f = Fraction(2,3)
>>> f
2/3
>>> f = Fraction(4,6)
>>> f
2/3
>>> -f
-2/3
>>> g = Fraction(4)
>>> g
4
>>> print(f+g)
14/3
>>> print(f-g)
-10/3
>>> print(f*g)
8/3
'''

from math import gcd

class Fraction:
    def __init__(self, num, denom = 1):
        # Simplify

        simplificationFactor = gcd(num,denom)
        self.num = int(num / simplificationFactor)
        self.denom = int(denom / simplificationFactor)

    def __repr__(self):
        strNum = f'{self.num}'
        strDenom = f'/{self.denom}' if self.denom != 1 else ''
        return strNum + strDenom

    def __neg__(self):
        return Fraction(self.num * -1, self.denom)
    
    def __add__(self, fraction):
        num = int(self.num * fraction.denom + fraction.num * self.denom)
        denom = int(self.denom * fraction.denom)
        return Fraction(num, denom)

    def __sub__(self, fraction):
        num = int(self.num * fraction.denom - fraction.num * self.denom)
        denom = int(self.denom * fraction.denom)
        return Fraction(num, denom)

    def __mul__(self, fraction):
        num = int(self.num * fraction.num)
        denom = int(self.denom * fraction.denom)
        return Fraction(num, denom)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
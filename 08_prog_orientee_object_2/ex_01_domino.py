'''
This module provides a class for generating dominos and play with it.

Example of use:

>>> d1 = Domino(1,2)
>>> d1
[ 1 | 2 ]
>>> d2 = Domino(2,3)
>>> suite = d2 + d1 # doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
[...]
Exception: [ 2 | 3 ] and [ 1 | 2 ] don't match!
>>> suite = d1 + d2
>>> suite
[ 1 | 2 ] [ 2 | 3 ]
>>> suite + Domino(3,6)
[ 1 | 2 ] [ 2 | 3 ] [ 3 | 6 ]
>>> 

This module also provides an example of writing automated tests using
the `docstring` module!
'''

class Domino:
    def __init__(self,val1, val2):
        self.val1 = val1
        self.val2 = val2
        self.suite = [self]

    def __repr__(self):
        return " ".join(f'[ {domino.val1} | {domino.val2} ]' for domino in self.suite)

    def __add__(self, dominoToAppend):
        if dominoToAppend.val1 == self.suite[-1].val2:
            self.suite.append(dominoToAppend)
        else:
            raise Exception(f'{self} and {dominoToAppend} don\'t match !')
        return self
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
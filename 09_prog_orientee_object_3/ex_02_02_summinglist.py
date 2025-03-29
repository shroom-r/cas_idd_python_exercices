'''
>>> s = SummingList([1,2,3])
>>> print(s)
[1, 2, 3]
>>> s.append(4)
>>> print(s)
[1, 2, 3, 4]
>>> print(s.sum())
10
'''
class SummingList(list):    
    def sum(self):
        return sum(self)
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
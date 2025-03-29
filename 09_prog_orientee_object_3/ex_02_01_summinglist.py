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
class SummingList:
    def __init__(self, list):
        self.list = list

    def __str__(self):
        return str(self.list)
    
    def append(self, value):
        self.list.append(value)
    
    def sum(self):
        return sum(self.list)
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
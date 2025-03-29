'''
>>> hd = HistoryDict()
>>> hd['test'] = 1
>>> print(hd['test'])
1
>>> hd['test'] = 2
>>> print(hd['test'])
2
>>> hd.history('test')
[1, 2]
'''

class HistoryDict():
    def __init__(self):
        self.dict = {}
        self.histDict={}

    def history(self, key):
         return self.histDict[key]

    def __setitem__(self,key,value):
            self.dict[key] = value
            try:
                self.histDict[key].append(value)
            except KeyError:
                self.histDict[key] = [value]

    def __getitem__(self,key):
        return self.dict[key]
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
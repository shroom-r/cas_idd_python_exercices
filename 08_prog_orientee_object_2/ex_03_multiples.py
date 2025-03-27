class Multiples:
    def __init__(self, value, maxValue = None):
        self.increment = value
        self.currentValue = value
        self.maxValue = maxValue
    
    def __iter__(self):
        return self

    def __next__(self):
        returnValue = self.currentValue
        if self.maxValue == None or returnValue <= self.maxValue:
            self.currentValue += self.increment
            return returnValue
        else:
            raise StopIteration
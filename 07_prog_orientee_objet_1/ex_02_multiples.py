class Multiples:
    def __init__(self, value):
        self.increment = value
        self.value = value
    
    def next(self):
        print(self.value)
        self.value += self.increment
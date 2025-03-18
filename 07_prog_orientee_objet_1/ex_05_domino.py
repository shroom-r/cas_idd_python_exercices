class Domino:
    def __init__(self,val1, val2):
        self.val1 = val1
        self.val2 = val2
        self.suite = [self]

    def display(self):
        for domino in self.suite:
            print(f"[ {domino.val1} | {domino.val2} ]", end='')
        print("")

    def append(self, dominoToAppend):
        if dominoToAppend.val1 == self.suite[-1].val2:
            self.suite.append(dominoToAppend)
        else:
            raise Exception(f'{self} and {dominoToAppend} don\'t match !')
        return self
class Account:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def display(self):
        print(f'Le solde du compte de {self.owner} est de {self.balance} {self.currency}.')

    def deposit(self, value):
        self.balance += value

    def withdraw(self, value):
        if self.balance >= value:
            self.balance -= value
        else:
            raise Exception("Not enough money available.")
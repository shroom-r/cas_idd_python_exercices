from collections import deque

class Account:

    def __init__(self, owner, balance, currency):
        self.owner = owner
        self.balance = balance
        self.currency = currency
        self.history = deque([balance])

    def display(self):
        print(f'Le solde du compte de {self.owner} est de {self.balance} {self.currency}.')

    def deposit(self, amount):
        self.balance += amount
        self.history.appendleft(self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.history.appendleft(self.balance)
        else:
            raise NotEnoughMoneyException('Not enough money available.')
    
    def __getitem__(self, index):
        if (index <= len(self.history) -1):
            return self.history[index]
        else:
            raise IndexError("Not enough transactions")

class NotEnoughMoneyException(Exception):
    pass
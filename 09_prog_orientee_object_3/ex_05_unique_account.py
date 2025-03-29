from collections import deque

'''
>>> a = Account('Paul', 100, 'CHF')
>>> b = Account('Paul', 200, 'EUR') # doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
[...]
OwnerError: Paul alread owns an account!
>>> b = Account('Jean', 200, 'EUR')
>>> Account.from_owner('Paul').display()
Le solde du compte de Paul est de 100 CHF.
>>> Account.from_owner('Jean') == b
True
'''

class Account:

    accounts = {}

    def __init__(self, owner, balance, currency):
        if owner in self.accounts.keys():
            raise OwnerError(f"{owner} already owns an account!")
        self.owner = owner
        self.accounts[owner] = self
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
    
    @classmethod
    def from_owner(cls, owner):
        return cls.accounts[owner]

class NotEnoughMoneyException(Exception):
    pass

class OwnerError(Exception):
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()
'''
>>> jd = Person('John', 'Doe')
>>> hp = Wizard('Harry', 'Potter')
>>> tr = Muggle('Tom', 'Riddle')
>>> print(jd)
John Doe
>>> print(hp)
Harry Potter (has magical power)
>>> print(tr)
Tom Riddle (no magical power)
>>> isinstance(hp, Person)
True
>>> isinstance(hp, Wizard)
True
>>> isinstance(hp, Muggle)
False
>>> hp.make_magic()
Expecto patronum!!!
>>> tr.make_magic()
Sorry, I can't!
>>> jd.make_magic() # doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
[...]
AttributeError: 'Person' object has no attribute 'make_magic'
'''
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"{name} {surname}"
    
class Wizard(Person):
    def __repr__(self):
        return super().__repr__() + " (has magical power)"
    
    def make_magic(self):
        print("Expecto patronum!!!")
    
class Muggle(Person):
    def __repr__(self):
        return super().__repr__() + " (has no magical power)"
    
    def make_magic(self):
        print("Sorry, I can't")

if __name__ == "__name__":
    import doctest
    doctest.testmod()
""" Create a class called Bank with two attributes: name and address. Then, derive a
class called Branch that inherits the attributes from the Bank class and includes
an additional attribute called number. Both classes should only have a constructor.

Now it's your turn! Practice inheritance to improve your skills and ensure an
efficient implementation of the Object-Oriented Programming paradigm with Python. """
from bank import Bank


class Agency(Bank):
    def __init__(self, name, adress, number):
        super().__init__(name, adress)
        self._number = number


bank = Bank('Nubank', 'São Paulo')
agency = Agency('Nubank', 'São Paulo', 123456)

print(bank._name)
print(bank._adress)
print(agency._name)
print(agency._adress)
print(agency._number)

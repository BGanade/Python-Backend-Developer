""" Create a class called Bank with two attributes: name and address. Then, derive a
class called Branch that inherits the attributes from the Bank class and includes
an additional attribute called number. Both classes should only have a constructor.

Now it's your turn! Practice inheritance to improve your skills and ensure an
efficient implementation of the Object-Oriented Programming paradigm with Python. """


class Bank:
    def __init__(self, name, adress):
        self._name = name
        self._adress = adress

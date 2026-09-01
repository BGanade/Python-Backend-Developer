""" Now it's your turn! Create a new class called Person with attributes such as name,
age, and profession. Add a special __str__ method to print a string representation of
the person.

Also implement an instance method called birthday that increases the person's age by
one year.

Finally, add a property called greeting that returns a personalized greeting message
based on the person's profession. """


class Person():

    def __init__(self, name, age, profession):
        self.name = name.title()
        self.age = age
        self.profesion = profession

    def __str__(self):
        return f'name: {self.name}, age: {self.age} years, profession: {self.profesion}'

    @property
    def greeting(self):
        if self.profesion:
            return f'Hello, I am {self.name}, work with {self.profesion}'

    def birthday(self):
        self.age += 1


ganade = Person('Bruno Ganade', 29, 'senior laboratory technician')
print(ganade)
print(ganade.greeting)
ganade.birthday()
print(ganade)

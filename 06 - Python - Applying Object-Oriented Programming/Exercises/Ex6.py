""" 1. Create a class called Book with a constructor that accepts the parameters title,
author, and publication_year. Initialize an attribute called available as True by 
default.

2. In the Book class, add a special __str__ method that returns a formatted message
with the book's title, author, and publication year. Create two instances of the Book
class and print these instances.

3. Add an instance method called borrow to the Book class that sets the available
attribute to False. Create an instance of the class, call the borrow method, and print
whether the book is available or not.

4. Add a static method called check_availability to the Book class that receives a year
as a parameter and returns a list of available books published in that year.

5. Create a file called library.py and import the Book class into this file.

6. In the library.py file, borrow the book by calling the borrow method and print
whether the book is available or not after the loan.

7. In the library.py file, use the static method check_availability to obtain the list
of available books published in a specific year.

8. Create a file called main.py, import the Book class, and in the main.py file,
instantiate two objects of the Book class and display the formatted message using
the __str__ method. """

# 1


class Book:

    books = []

    def __init__(self, title, author, publication_year):
        self._title = title
        self._author = author
        self._publication_year = publication_year
        self._available = True
        Book.books.append(self)

    # 2
    def __str__(self):
        return (
            f'Title: {self._title}, Author: {self._author}, '
            f'Publication year: {self._publication_year}, '
            f'Available: {self._available}.'
        )

    # 3
    def borrow(self):
        self._available = False

    # 4
    @staticmethod
    def check_availability(year):
        return [
            book for book in Book.books
            if book._publication_year == year and book._available
        ]

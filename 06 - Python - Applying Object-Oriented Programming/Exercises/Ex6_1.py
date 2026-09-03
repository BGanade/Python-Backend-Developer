# 5
from Ex6 import Book

book1 = Book('Harry Potter and the Philosopher Stone', 'J.K. Rowling', 1997)
book2 = Book('The Hobbit', 'J.R.R. Tolkien', 1937)
book3 = Book('Harry Potter and the Chamber of Secrets', 'J.K. Rowling', 1998)
book4 = Book('The Lord of the Rings', 'J.R.R. Tolkien', 1954)
book5 = Book('1984', 'George Orwell', 1949)
book6 = Book('Animal Farm', 'George Orwell', 1945)
book7 = Book('The Little Prince', 'Antoine de Saint-Exupery', 1943)
book8 = Book('The Alchemist', 'Paulo Coelho', 1988)
book9 = Book('The Da Vinci Code', 'Dan Brown', 2003)
book10 = Book('Twilight', 'Stephenie Meyer', 2005)
book11 = Book('The Hunger Games', 'Suzanne Collins', 2008)
book12 = Book('Into Thin Air', 'Jon Krakauer', 1997)
book13 = Book('Memoirs of a Geisha', 'Arthur Golden', 1997)
book14 = Book('Harry Potter and the Prisoner of Azkaban', 'J.K. Rowling', 1999)
book15 = Book('Harry Potter and the Goblet of Fire', 'J.K. Rowling', 2000)
book16 = Book('Angels and Demons', 'Dan Brown', 2000)
book17 = Book('The Fault in Our Stars', 'John Green', 2012)
book18 = Book('Gone Girl', 'Gillian Flynn', 2012)
book19 = Book('The Shining', 'Stephen King', 1977)
book20 = Book('The Silmarillion', 'J.R.R. Tolkien', 1977)

available_books = Book.check_availability(1997)

for book in available_books:
    print(book)

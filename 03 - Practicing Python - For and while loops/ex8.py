""" Ana is implementing a book filtering system for Buscante. The feature should 
iterate through a list of books and display the name of each book that is available in 
stock. However, if a book is out of stock, it should be skipped during the iteration.

books = [

    {"name": "1984", "stock": 5},

    {"name": "Dom Casmurro", "stock": 0},

    {"name": "The Little Prince", "stock": 3},

    {"name": "The Hobbit", "stock": 0},

    {"name": "Pride and Prejudice", "stock": 2}

]

Create a program that helps Ana display only the books that are in stock, using the 
format: "Available book: <book name>". """

books = [

    {"name": "1984", "stock": 5},

    {"name": "Dom Casmurro", "stock": 0},

    {"name": "The Little Prince", "stock": 3},

    {"name": "The Hobbit", "stock": 0},

    {"name": "Pride and Prejudice", "stock": 2}

]

for book in books:
    if book['stock'] > 0:
        print(f"Available book: {book['name']}")

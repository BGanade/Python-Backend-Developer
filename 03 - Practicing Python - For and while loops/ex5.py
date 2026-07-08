""" Joseph is developing a feature for the Buscante system to stop searching as soon as 
a specific book is found. The list of books already registered in the system is as 
follows:

books = ["1984", "Dom Casmurro", "The Little Prince", "The Hobbit", 
"Pride and Prejudice"]

Help Joseph create a program that iterates through the list and displays the message 
"Book found: <book name>" as soon as the book "The Hobbit" is found. After finding the 
book, the program should immediately stop searching without checking the remaining 
books. """

books = [
    "1984",
    "Dom Casmurro",
    "The Little Prince",
    "The Hobbit",
    "Pride and Prejudice"
]

for book in books:
    if book == "The Hobbit":
        print(f"Book found: {book}")
        break

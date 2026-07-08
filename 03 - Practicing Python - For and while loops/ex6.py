""" You are developing an inventory management system for Buscante. One of the 
requirements is to check the number of copies of a book in stock and continue selling 
until the inventory is depleted. Whenever a sale is made, the system should notify the 
user and update the remaining quantity available.

Create a program that simulates the sale of a book with an initial stock of 5 copies. 
The program should display the message "Sale completed! Remaining stock: <quantity>" 
after each sale and, once the stock reaches zero, display the message 
"Out of stock". """

books = [
    {
        "title": "1984",
        "author": "George Orwell",
        "stock": 5
    },
    {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "stock": 3
    }
]

book_title = input("Enter the book title: ")

for book in books:
    if book["title"].lower() == book_title.lower():

        while book["stock"] > 0:
            sell = input("Sell a copy? (y/n): ").lower()

            if sell != "y":
                break

            book["stock"] -= 1
            print(f'Sale completed! Remaining stock: {book["stock"]}')

        if book["stock"] == 0:
            print("Out of stock")

        break
else:
    print("Book not found.")
""" Clara is managing her store's inventory and received two separate lists: one 
containing the product names and another containing their respective prices. To make 
the data easier to organize, she needs to combine the lists so that each product is 
associated with its price.

Create a program that combines the lists and displays the result in the format:

product: price

Example input:

Enter the products separated by commas: apple, banana, pear
Enter the prices separated by commas: 2.5, 1.2, 3.0

Expected output:

apple: 2.5
banana: 1.2
pear: 3.0 """

products = input('Enter the products separated by commas: ').split(",")
prices = input('Enter the prices separated by commas: ').split(",")

for product, price in zip(products, prices):
    print(f'{product.strip()}: {price.strip()}')
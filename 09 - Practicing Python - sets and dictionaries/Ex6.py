""" Ana is responsible for inventory management at a stationery store. She needs a
program that allows products to be registered as structured data. The system should
ask for the name and quantity of three products and, at the end, display the registered
information in a dictionary, where each product will be a key and the corresponding
quantity will be the value.

Input Example:

Enter the product name: Pen
Enter the quantity: 50
Enter the product name: Notebook
Enter the quantity: 30
Enter the product name: Eraser
Enter the quantity: 20

Expected Output:
Product dictionary: {'Pen': 50, 'Notebook': 30, 'Eraser': 20} """

products = {}

for _ in range(3):
    product_name = input("Enter the product name: ")
    product_quantity = int(input("Enter the quantity: "))

    products[product_name] = product_quantity

print(f"Product dictionary: {products}")

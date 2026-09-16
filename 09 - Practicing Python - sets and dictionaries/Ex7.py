""" Ana realized that, after the initial registration of the products, she needs to
update the quantity of a specific item in the inventory. Your task is to create a
program that asks for the product name and the new quantity, updating this
information in the inventory dictionary.

Input Example:

inventory = {
    "College notebook": 50,
    "Blue pen": 120,
    "White eraser": 30
}

Product name to update: Blue pen
New quantity: 150

Expected Output:
{
    "College notebook": 50,
    "Blue pen": 150,
    "White eraser": 30
} """

inventory = {
    "College notebook": 50,
    "Blue pen": 120,
    "White eraser": 30
}

while True:
    product_name_update = input("Product name to update: ")

    if product_name_update in inventory:
        product_new_quantity = int(input("New quantity: "))
        inventory[product_name_update] = product_new_quantity
        print("product sucessefully updated")
        print(inventory)
        break
    else:
        print("Product not found")

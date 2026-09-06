""" Armano works with the management of two merchandise inventories that are
represented as tuples. Now, he needs to create a unified report with the products
from both inventories combined.

To help him, how would you create a program that reads the inventory information
and generates a report with all the products combined?

Input Example:

Inventory 1 products (separated by commas): Rice, Beans, Pasta
Inventory 2 products (separated by commas): Oil, Salt, Sugar

Expected Output:

Combined inventory:
('Rice', 'Beans', 'Pasta', 'Oil', 'Salt', 'Sugar') """

inventory_1 = tuple(
    input("Inventory 1 products (separated by commas): ").split(", "))
inventory_2 = tuple(
    input("Inventory 2 products (separated by commas): ").split(", "))
combined_inventory = inventory_1 + inventory_2
print(f'Combined Inventory: {combined_inventory}')

""" Paulo is creating a list of orders for the snack bar. He already has all the
orders, but he noticed that the last one was added by mistake and needs to be removed.

Given this situation, help Paulo by creating a program that automates this operation,
allowing him to list the orders and automatically remove the last item.

Input Example:

Orders placed (separated by commas): Sandwich, Juice, Dessert

Expected Output:

Final orders: ['Sandwich', 'Juice'] """

orders = input('Enter the orders placed (separated by commas): ').split(", ")
print(f'Mistaken order: {orders}')
orders.pop()
print(f'Correct order: {orders}')

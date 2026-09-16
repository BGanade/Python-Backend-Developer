""" Nathalia is a manager at an online store and needs a system that receives sales
records organized by product category. Each category contains a list of dictionaries
representing individual sales, with information about the product, quantity sold,
and unit price. Your task is to create a program that displays the total sales
for each category.

Input Example:

sales = {
    "Electronics": [
        {"product": "Smartphone", "quantity": 5, "unit_price": 2000},
        {"product": "Tablet", "quantity": 3, "unit_price": 1500}
    ],

    "Home Appliances": [
        {"product": "Refrigerator", "quantity": 2, "unit_price": 3000},
        {"product": "Microwave", "quantity": 4, "unit_price": 800}
    ],

    "Books": [
        {"product": "Book A", "quantity": 10, "unit_price": 50},
        {"product": "Book B", "quantity": 5, "unit_price": 100}
    ]

}

Expected Output:

Total sales by category:
- Electronics: R$ 14500.00
- Home Appliances: R$ 9200.00
- Books: R$ 1000.00 """

sales = {
    "Electronics": [
        {"product": "Smartphone", "quantity": 5, "unit_price": 2000},
        {"product": "Tablet", "quantity": 3, "unit_price": 1500}
    ],
    "Home Appliances": [
        {"product": "Refrigerator", "quantity": 2, "unit_price": 3000},
        {"product": "Microwave", "quantity": 4, "unit_price": 800}
    ],
    "Books": [
        {"product": "Book A", "quantity": 10, "unit_price": 50},
        {"product": "Book B", "quantity": 5, "unit_price": 100}
    ]
}

for category, products in sales.items():
    total = 0
    for product in products:
        total += product["quantity"] * product["unit_price"]

    print(f"- {category}: R${total:.2f}")

""" Roberto is organizing his pantry and wants to check whether certain items ar 
already stored before adding them to his shopping list.

Help Roberto create a program that asks for the desired item and checks whether it
is in the list of available items in the pantry. If the item is not in the list,
the program should inform him that it needs to be purchased.

Input Example:

Type the item you want to check: sugar

Expected Output:

The item sugar needs to be purchased. """

pantry_items = [
    'rice', 'beans', 'pasta', 'tomato sauce', 'flour', 'salt', 'olive oil',
    'cooking oil', 'vinegar', 'coffee', 'milk', 'butter', 'cheese', 'ham',
    'eggs', 'bread', 'garlic', 'onion', 'potatoes', 'tomatoes', 'carrots',
    'lettuce', 'broccoli', 'chicken', 'ground beef', 'fish', 'sausage',
    'corn', 'peas', 'tuna', 'mayonnaise', 'ketchup', 'mustard', 'oregano',
    'black pepper', 'paprika', 'cinnamon', 'chocolate powder', 'oatmeal',
    'granola', 'cookies', 'baking powder', 'heavy cream', 'condensed milk'
]

verify_item = input("Enter an item to check: ").lower()

if verify_item in pantry_items:
    print(f"You still have {verify_item}.")
else:
    print(f"The item {verify_item} needs to be purchased.")

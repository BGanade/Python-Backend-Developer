class Restaurant:
    name = ''
    category = ''
    active = False

restaurant_praca = Restaurant()
restaurant_praca.name = 'Praca'
restaurant_praca.category = 'Gourmet'
restaurant_pizza = Restaurant()

restaurants = [restaurant_praca, restaurant_pizza]

print(restaurant_praca)
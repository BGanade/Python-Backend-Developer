class Restaurant:
    restaurants = []
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._active = False
        Restaurant.restaurants.append(self)

    def __str__(self):
        return f'{self.name} | {self.category}'

    def list_restaurants():
        print(f'{'Restaurant Name'.ljust(25)} |'
              f'{'Category'.ljust(25)} |' 
              f'{'Status'}')
        for restaurant in Restaurant.restaurants:
            print(
                f'{restaurant.name.ljust(25)} |'
                f'{restaurant.category.ljust(25)} |'
                f'{restaurant.active}'
            )

    @property
    def active(self):
        return 'active' if self._active else 'inactive'

restaurant_praca = Restaurant('Praça', 'Gourmet')
restaurant_pizza = Restaurant('Pizza Express', 'Italiano')

Restaurant.list_restaurants()

class Restaurant:
    restaurants = []

    def __init__(self, name, category):
        self._name = name.title()
        self.category = category.upper()
        self._active = False
        Restaurant.restaurants.append(self)

    def __str__(self):
        return f'{self._name} | {self.category}'

    @classmethod
    def list_restaurants(cls):
        print(f'{'Restaurant Name'.ljust(25)} |'
              f'{'Category'.ljust(25)} |'
              f'{'Status'}')
        for restaurant in cls.restaurants:
            print(
                f'{restaurant._name.ljust(25)} |'
                f'{restaurant.category.ljust(25)} |'
                f'{restaurant.active}'
            )

    @property
    def active(self):
        return 'active' if self._active else 'inactive'

    def Alternate_status(self):
        self._active = not self._active


restaurant_praca = Restaurant('praça', 'Gourmet')
restaurant_praca.Alternate_status()
restaurant_pizza = Restaurant('pizza express', 'Italiano')

Restaurant.list_restaurants()

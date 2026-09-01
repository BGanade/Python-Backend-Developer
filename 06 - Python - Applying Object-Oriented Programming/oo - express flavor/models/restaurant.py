from models.review import Review


class Restaurant:
    restaurants = []

    def __init__(self, name, category):
        self._name = name.title()
        self.category = category.upper()
        self._active = False
        self._review = []
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

    def recive_review(self, costumer, rating):
        review = Review(costumer, rating)
        self._review.append(review)

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
        print(
            f'{"Restaurant Name".ljust(25)} | '
            f'{"Category".ljust(25)} | '
            f'{"Review".ljust(25)} | '
            f'{"Status"}'
        )

        for restaurant in cls.restaurants:
            print(
                f'{restaurant._name.ljust(25)} | '
                f'{restaurant.category.ljust(25)} | '
                f'{str(restaurant.average_reviews).ljust(25)} | '
                f'{restaurant.active}'
            )

    @property
    def active(self):
        return 'active' if self._active else 'inactive'

    def alternate_status(self):
        self._active = not self._active

    def receive_review(self, customer, rating):
        review = Review(customer, rating)
        self._review.append(review)

    @property
    def average_reviews(self):
        if not self._review:
            return 0
        sum_ratings = sum(review._rating for review in self._review)
        quantity_of_ratings = len(self._review)
        average = round(sum_ratings / quantity_of_ratings, 1)

        return average

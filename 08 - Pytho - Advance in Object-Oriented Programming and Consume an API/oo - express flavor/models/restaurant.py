from models.review import Review


class Restaurant:
    """Represent a restaurant in the application.

    ```
    Stores information about a restaurant, including its name,
    category, activation status, and customer reviews.
    """

    restaurants = []

    def __init__(self, name, category):
        """Initialize a new restaurant.

        Args:
            name: The name of the restaurant.
            category: The category of the restaurant.
        """
        self._name = name.title()
        self.category = category.upper()
        self._active = False
        self._reviews = []

        Restaurant.restaurants.append(self)

    def __str__(self):
        """Return a formatted string representation of the restaurant.

        Returns:
            A string containing the restaurant's name and category.
        """
        return f'{self._name} | {self.category}'

    @classmethod
    def list_restaurants(cls):
        """Display all registered restaurants.

        Prints a formatted list containing each restaurant's name,
        category, average review, and activation status.
        """
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
        """Return the current activation status of the restaurant.

        Returns:
            A string indicating whether the restaurant is active
            or inactive.
        """
        return 'active' if self._active else 'inactive'

    def alternate_status(self):
        """Toggle the restaurant's activation status.

        Changes the current status from active to inactive or from
        inactive to active.
        """
        self._active = not self._active

    def receive_review(self, customer, rating):
        """Add a customer review to the restaurant.

        Creates and stores a review when the provided rating is
        between 1 and 5.

        Args:
            customer: The customer who submitted the review.
            rating: The rating given to the restaurant.
        """
        if 0 < rating <= 5:
            review = Review(customer, rating)
            self._reviews.append(review)

    @property
    def average_reviews(self):
        """Calculate the average rating of the restaurant.

        Returns:
            The average rating rounded to one decimal place, or
            a hyphen if the restaurant has no reviews.
        """
        if not self._reviews:
            return '-'

        sum_ratings = sum(review._rating for review in self._reviews)
        quantity_of_ratings = len(self._reviews)
        average = round(sum_ratings / quantity_of_ratings, 1)

        return average

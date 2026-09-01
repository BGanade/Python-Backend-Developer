# 1) Implement a class called Car with basic attributes such as model, color, and year.
#    Create an instance of this class and assign values to its attributes.

class Car:
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year

# Creating a car instance and assigning values to its attributes
my_car = Car(model='Beetle', color='Blue', year=1970)


# 2) Create a class called Restaurant with the attributes name, category, active, and 
# create 2 additional attributes.
#    Instantiate a restaurant and assign values to its attributes.

class Restaurant:
    def __init__(self, name, category, capacity, rating, active=False):
        self.name = name
        self.category = category
        self.capacity = capacity
        self.rating = rating
        self.active = active

# Creating a restaurant instance and assigning values to its attributes
example_restaurant = Restaurant(
    name='Good Food',
    category='Gourmet',
    capacity=50,
    rating=4.5,
    active=True
)


# 3) Modify the Restaurant class by adding a constructor that accepts name and category 
# as parameters and initializes active as False by default. Create an instance using 
# the constructor.

class Restaurant:
    def __init__(self, name, category, capacity=0, rating=0.0, active=False):
        self.name = name
        self.category = category
        self.capacity = capacity
        self.rating = rating
        self.active = active

# Creating a restaurant instance using the new constructor
new_restaurant = Restaurant(name='Santa Marmita', category='Fast Food')


# 4) Add a special __str__ method to the Restaurant class so that when an instance is 
# printed, a formatted message with the name and category is displayed. Display this 
# message for a restaurant instance.

class Restaurant:
    def __init__(self, name, category, capacity=0, rating=0.0, active=False):
        self.name = name
        self.category = category
        self.capacity = capacity
        self.rating = rating
        self.active = active

    def __str__(self):
        return f'{self.name} | {self.category}'

# Displaying a formatted restaurant instance
formatted_restaurant = Restaurant(name='Good Taste', category='Traditional')
print(formatted_restaurant)


# 5) Create a class called Customer and think of 4 attributes.
#    Then, instantiate 3 objects of this class and assign values to their attributes 
# through a constructor.

class Customer:
    def __init__(self, name, age, email, phone):
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone

# Creating three Customer objects and assigning values to their attributes through the constructor
customer1 = Customer(name='Alice', age=25, email='alice@gmail.com', phone='123-456-7890')
customer2 = Customer(name='Bob', age=30, email='bob@gmail.com', phone='987-654-3210')
customer3 = Customer(name='Charlie', age=22, email='charlie@gmail.com', phone='555-123-4567')
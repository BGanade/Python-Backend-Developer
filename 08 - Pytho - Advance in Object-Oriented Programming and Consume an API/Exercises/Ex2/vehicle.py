""" 1. Create a Parent Class (Vehicle): Implement a class called Vehicle with a
constructor that accepts two parameters, brand and model. The class should have
a protected attribute _is_on initialized to False by default.

2. Build the Special __str__ Method: Add a special __str__ method to the Vehicle
class that returns a formatted message with the vehicle's brand, model, and
on/off status.

3. Create a Child Class (Car): Now, create a class called Car that inherits from
the Vehicle class. In the Car class constructor, include a new attribute called
doors that indicates the number of doors the car has.

4. Implement the Special __str__ Method in the Child Class: Add a special __str__
method to the Car class that extends the parent class's (Vehicle) method and
includes information about the number of doors the car has.

5. Create a Child Class (Motorcycle): Similarly, create a class called Motorcycle
that also inherits from Vehicle. Add a new attribute called type to the
constructor, indicating whether the motorcycle is sport or casual.

6. Implement the Special __str__ Method in the Child Class (Motorcycle): Add a
special __str__ method to the Motorcycle class that extends the parent class's
(Vehicle) method and includes information about the motorcycle's type.

7. Create a Main File (main.py): Create a file called main.py in the same directory
as your classes.

8. Import and Instantiate Objects: In the main.py file, import the Car and
Motorcycle classes. Then, create three instances of Car and Motorcycle with
different brands, models, numbers of doors, and types.

9. Display the Information: For each instance, print the information to the
console using the __str__ method. """

#1
class Vehicle:
    def __init__(self, brand, model) -> None:
        self._brand = brand
        self._model = model
        self._is_on = False

    #2
    def __str__(self) -> str:
        return f'Brand: {self._brand}, Model: {self._model}, Status: {self._is_on}'

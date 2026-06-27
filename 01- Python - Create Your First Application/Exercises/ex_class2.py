""" 1 - Ask the user to enter a number, and then use an `if-else` structure to determine whether the number is even or odd.

2 - Ask the user for their age and, based on that, use an `if-elif-else` structure to classify the age into categories according to the following conditions:

Child: 0 to 12 years old;
Teenager: 13 to 18 years old;
Adult: over 18 years old.
3 - Ask for a username and password, and use an `if-else` structure to verify if the provided username and password match the expected values ​​you have defined.

4 - Ask the user for the (x, y) coordinates of a point and use an `if-elif-else` structure to determine which quadrant of the Cartesian plane the point lies in, according to the following conditions:

First Quadrant: both x and y values ​​must be greater than zero;
Second Quadrant: the x value is less than zero and the y value is greater than zero;
Third Quadrant: both x and y values ​​must be less than zero;
Fourth Quadrant: the x value is greater than zero and the y value is less than zero;
Otherwise: the point is located on an axis or at the origin. """

#1----------------------------------------------------------------------------------------------------
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"The number {number} is even.\n")
else:
    print(f"The number {number} is odd.\n")

#2----------------------------------------------------------------------------------------------------
age = int(input("Enter your age: "))
if age >= 0 and age <= 12:
    print("You are a child.\n")
elif age <= 18:
    print("You are a teenager.\n")
else:
    print("You are an adult.\n")  

#3----------------------------------------------------------------------------------------------------
username = input("Enter your username: ")
password = input("Enter your password: ")
expected_username = "admin"
expected_password = "password123"

if username == expected_username and password == expected_password:
    print("Access granted.\n")
else:
    print("Access denied. Invalid username or password.\n")

#4----------------------------------------------------------------------------------------------------
x = float(input("Enter the x-coordinate of the point: "))
y = float(input("Enter the y-coordinate of the point: "))
if x > 0 and y > 0:
    print("The point is in the First Quadrant.\n")
elif x < 0 and y > 0:
    print("The point is in the Second Quadrant.\n")
elif x < 0 and y < 0:
    print("The point is in the Third Quadrant.\n")
elif x > 0 and y < 0:
    print("The point is in the Fourth Quadrant.\n")
else:
    print("The point is located on an axis or at the origin.\n")


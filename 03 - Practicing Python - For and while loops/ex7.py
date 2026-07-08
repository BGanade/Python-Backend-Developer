""" Aline is implementing a feature that displays personalized messages to customers 
during a special promotion for her new bookstore. The system should display a custom 
countdown message for each number from 10 to 1, and at the end display the message: 
"Take advantage of the promotion now!"

Create a program that uses a for loop to display the following messages:

For even numbers, display: "Only <number> seconds left - Don't miss this opportunity!".
For odd numbers, display: "The countdown continues: <number> seconds remaining.".
At the end of the countdown, display the message: "Take advantage of the promotion 
now!". """

for number in range(10, 0, -1):
    if number % 2 == 0:
        print(f"Only {number} seconds left - Don't miss this opportunity!")
    else:
        unit = "second" if number == 1 else "seconds"
        print(f"The countdown continues: {number} {unit} remaining.")
print("Take advantage of the promotion now!")
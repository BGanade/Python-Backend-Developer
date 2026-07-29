""" Carlos is creating a simple calculator but wants to make sure the program does not 
crash if the user enters invalid values. To achieve this, he needs to handle possible 
errors.

Create a calculator that allows the user to choose between addition, subtraction, 
multiplication, and division. In addition to organizing the code into functions, use 
try-except blocks to handle the following errors:

If the user enters a character instead of a number, raise a ValueError.
If the user attempts to divide by zero, raise a ZeroDivisionError.

Example input:
Enter the first number: 5
Choose an operation (+, -, *, /): +
Enter the second number: 7

Expected output:
Result: 12

If the user selects an operation that is not listed:
Invalid option

If the user enters a character instead of a number:
Error: Invalid input. Please enter numbers only.

If the user attempts to divide by zero:
Error: Division by zero is not allowed. """

operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y
}


def calculator():
    first_number = get_number("Enter the first number: ")
    operation = get_operation()
    second_number = get_number("Enter the second number: ")

    try:
        result = calculate(first_number, operation, second_number)
        print(f"Result: {result}")

    except ZeroDivisionError as error:
        print(f"Error: {error}")


def get_number(message):
    while True:
        try:
            number = int(input(message))
            return number

        except ValueError:
            print("Error: Invalid input. Please enter numbers only.")


def get_operation():
    while True:
        user_option = input("Enter an operation (+, -, *, /): ")

        if user_option not in operations:
            print("Invalid option.")
        else:
            return user_option


def calculate(first_number, operation, second_number):
    if operation == "/" and second_number == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")

    return operations[operation](first_number, second_number)


calculator()
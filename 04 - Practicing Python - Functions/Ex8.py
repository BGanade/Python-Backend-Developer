""" Joana is participating in a recruitment process for a software developer position 
and has received a technical challenge to create a calculator that can add, subtract, 
multiply, and divide two numbers.

Your task is to create a program using lambda functions that reads two numbers and a 
mathematical operator chosen by the user (+, -, * or /), then displays the corresponding
 result.

Example input:
Enter the first number: 10
Enter the second number: 5
Choose an operation (+, -, *, /): +

Expected output:
The result is: 15 """

first_number = int(input('Enter the first number: '))
second_number = int(input('Enter the second number: '))
operator = input('chose an operation (+, -, *, /): ')

operations = {
    "+": lambda x,y: x + y,
    "-": lambda x,y: x - y,
    "*": lambda x,y: x * y,
    "/": lambda x,y: x / y
}

if operator in operations:
    try:
        result = operations[operator](first_number, second_number)
        print(result)
    except ZeroDivisionError:
        print("Cannot divide by zero")
else:
    print("Invalid operation")

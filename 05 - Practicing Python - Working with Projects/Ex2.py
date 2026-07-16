""" Carlos works at a notary office and needs to validate whether a CPF provided by a 
client has the correct format before proceeding with the service. The CPF must contain 
exactly 11 numeric digits. If the input contains letters or any other character that is 
not a digit, the program should display an error message.

Create a program that asks the user for a CPF number and checks whether it has exactly 
11 digits and contains only numbers.

Example input:
Enter your CPF: 12345678901

Expected output:
Valid CPF.

If the CPF is invalid:
Enter your CPF: 1234abc567
Error: The CPF must contain only numbers.

If the CPF has a number of digits other than 11:
Enter your CPF: 1234567
Error: The CPF must contain exactly 11 digits. """

while True:
    cpf = input("Enter your CPF: ")

    if not cpf.isdigit():
        print("The CPF must contain only numbers.")
    elif len(cpf) != 11:
        print("The CPF must contain exactly 11 digits.")
    else:
        print("Valid CPF.")
        break
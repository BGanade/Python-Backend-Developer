""" Lucas is developing a game and needs a feature that checks whether a number is even 
or odd. This check will be used to determine different actions within the game. Write a 
program that takes an integer as input and displays a message stating whether it is even
 or odd. """

number = int(input('Enter an integer: '))

if number % 2 == 0:
    print(f'The number {number} is even!')
else:
    print(f'The number {number} is odd!')

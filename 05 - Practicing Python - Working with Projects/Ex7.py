""" Maria is creating a game to help her students practice logic and quick thinking. 
She wants a program in which the computer randomly selects a number between 1 and 100, 
and the player has to guess it.

In addition to providing a fun gameplay experience, Maria wants the program to handle 
invalid input by preventing the user from entering invalid values, such as letters or 
numbers outside the allowed range.

Your task is to create a program that generates a random number between 1 and 100 and 
allows the user to keep guessing until they find the correct number. The program should 
inform the user whether the guess is higher or lower than the correct number. If the 
user enters an invalid value or a number outside the allowed range, a ValueError 
exception should be raised.

Example input:
Guess the number (1-100): 50

Expected output:
Congratulations! You guessed the number 37.

If the guess is too low:
Too low! Try again: 17

If the guess is too high:
Too high! Try again: 75

If an exception occurs:
Invalid input: Number out of range! Enter a number between 1 and 100.
Invalid input: invalid literal for int() with base 10: 'abc12' """

import random


def game():
    random_number = generate_random_number()
    attempts = 0

    while True:
        guessed_number = get_guessed_number()
        attempts += 1

        result = check_numbers(random_number, guessed_number)

        if result:
            attempt_word = "attempt" if attempts == 1 else "attempts"
            print(
                f"Congratulations! You guessed the number {random_number} "
                f"in {attempts} {attempt_word}."
            )
            break


def check_numbers(rand_number, guess_number):
    if guess_number > rand_number:
        print("Too high! Try a lower number.")
        return False

    elif guess_number < rand_number:
        print("Too low! Try a higher number.")
        return False

    else:
        return True


def get_guessed_number():
    while True:
        try:
            guessed_number = int(input("Guess the number (1-100): "))

            if not 1 <= guessed_number <= 100:
                raise ValueError(
                    "Number out of range! Enter a number between 1 and 100."
                )

            return guessed_number

        except ValueError as error:
            print(f"Invalid input: {error}")


def generate_random_number():
    return random.randint(1, 100)


game()
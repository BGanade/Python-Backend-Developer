""" Lucas wants to create a Rock, Paper, Scissors game to play against the computer. 
He needs a program that allows the user to choose an option and then displays the result
 of the match.

Create a program that lets the user choose between rock, paper, or scissors. The 
computer will randomly choose one of the three options. The program should display the 
winner of the match. Remember that:

Rock beats Scissors (Rock crushes Scissors);
Scissors beat Paper (Scissors cut Paper);
Paper beats Rock (Paper covers Rock);
If both players choose the same option, the game ends in a tie.

Example input:
Choose: rock, paper, or scissors? paper

Expected output:
Computer chose: rock
You won!

If the computer wins:
Computer chose: scissors
You lost!

If the computer chooses the same option as the user:
Computer chose: paper
It's a tie! """

import random

OPTIONS = ["rock", "paper", "scissors"]

WINS = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}


def comparison_of_results(user_choice):
    cpu_choice = random.choice(OPTIONS)

    print(f"\nThe computer chose: {cpu_choice}")

    if user_choice == cpu_choice:
        print("It's a tie!")
    elif WINS[user_choice] == cpu_choice:
        print("You won!")
    else:
        print("You lost!")


def start_game():
    while True:

        user_choice = input("\nChoose: rock, paper or scissors: ").lower()

        if user_choice not in OPTIONS:
            print("Invalid choice! Try again.")
            continue

        comparison_of_results(user_choice)

        user_end_choice = input("\nPress Enter to play again or type 1 to quit: ")

        if user_end_choice == "1":
            print("Game ended!")
            break


start_game()
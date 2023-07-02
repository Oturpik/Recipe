# Certainly! Here's an example of Python code for a rock-paper-scissors game:

# python
import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == "rock" and computer_choice == "scissors")
        or (player_choice == "paper" and computer_choice == "rock")
        or (player_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    choices = ["rock", "paper", "scissors"]

    print("Welcome to Rock-Paper-Scissors!")
    print("Available choices: rock, paper, scissors")

    while True:
        player_choice = input("Enter your choice: ").lower()
        if player_choice not in choices:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = random.choice(choices)

        print(f"\nYou chose {player_choice}.")
        print(f"The computer chose {computer_choice}.\n")

        result = determine_winner(player_choice, computer_choice)
        print(result)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("\nThank you for playing Rock-Paper-Scissors!")

play_game()


#In this code, the game is played in a `play_game` function. The function takes player input, generates a random choice for the computer, determines the winner, and asks the player if they want to play again. The `determine_winner` function compares the player's and computer's choices to determine the winner based on the rules of rock-paper-scissors. The game continues until the player chooses not to play again.

#You can run this code and play the game by entering "rock", "paper", or "scissors" as your choice. Enjoy!
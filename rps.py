import random


WELCOME_MESSAGE = "Hi. Welcome to my Rock-Paper-Scissors game!"


WIN_MESSAGE = "You won my guy"
LOSE_MESSAGE = "Oh, the computer won. It's ok. (No its not)"
TIE_MESSAGE = "Its a tie game! Try again to win...or lose"

def random_choice(options=["rock", "paper", "scissors"]):
    return random.choice(options)

def determine_winner(choice1, choice2):

    winners = {
        "rock":{
            "rock": None,
            "paper": "paper",
            "scissors": "rock",
        },
        "paper":{
            "rock": "paper",
            "paper": None,
            "scissors": "scissors",
        },
        "scissors":{
            "rock": "rock",
            "paper": "scissors",
            "scissors": None,
        },
    }


    winner = winners[choice1][choice2]

    return winner

if __name__ == "__main__":


    options = ["rock", "paper", "scissors"]

    user_choice = input("Choose rock, paper or scissors: ")

    if user_choice in options:
        print("You chose:", user_choice)
    else:
        print("Kinda expecting rock, paper, or scissors...nothing else so try again")
        exit()

    computer_choice = random_choice(options)
    print("The computer chose:", computer_choice)


    winning_choice = determine_winner(user_choice, computer_choice)

    if winning_choice:
        if winning_choice == user_choice:
            print(WIN_MESSAGE)
        elif winning_choice == computer_choice:
            print(LOSE_MESSAGE)
    else:
        print(TIE_MESSAGE)

    print("Play again! or something")
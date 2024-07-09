import random

user_score = 0
computer_score = 0

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def display_result(user_choice, computer_choice, winner):
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if winner == "tie":
        print("It is a TIE !")
    elif winner == "user":
        print("You WIN !")
    else:
        print("You LOSE !")

def play_game():
    global user_score, computer_score
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid Choice, Please Choose Again...")
        return
    computer_choice = get_computer_choice()
    winner = determine_winner(user_choice, computer_choice)
    display_result(user_choice, computer_choice, winner)
    if winner == "user":
        user_score += 1
    elif winner == "computer":
        computer_score += 1
    print(f"Scores: You - {user_score}, Computer - {computer_score}")

def main():
    while True:
        play_game()
        play_again = input("Do You want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            break
    print("Thanks For Playing...")

main()

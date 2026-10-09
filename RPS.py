import random
while True:
    user_action = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print("It's a tie!")
    elif user_action == "rock":
        if computer_action == "paper":
            print("Computer wins. You lose.")
        else:
            print("Computer loses. You win!")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Computer loses. You win!")
        else:
            print("Computer wins. You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Computer loses. You win!")
        else:
            print("Computer wins. You lose.")
    Answer = input("Do you want to play again? Y/N")
    if Answer == "N":
        print("Bye")
        break
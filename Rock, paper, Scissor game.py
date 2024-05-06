import random

def get_choices():
    option = ["rock", "paper", "scissor"]
    player_choice = input("Enter a choice (rock, paper, scissor): ")
    computer_choice = random.choice(option)

    choices = {"player": player_choice, "computer": computer_choice}

    return choices

def check_result(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "Tie!"
    elif player == "rock":
        if computer == "scissor":
            return "won"
        else:
            return "lost"
    elif player == "paper":
        if computer == "rock":
            return "won"
        else:
            return "lost"
    elif player == "scissor":
        if computer == "paper":
            return "won"
        else:
            return "lost"

choices = get_choices()

result = check_result(choices["player"], choices["computer"])
print(result)
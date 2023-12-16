import random

def get_choices():
    options = ["rock", "paper", "scissors"]
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def get_result(choices):
    player = choices["player"]
    computer = choices["computer"]
    
    print(f"Player Choice: {player}, Computer Choice: {computer}")
    if player == computer:
        return "Result: Tie"
    elif player ==  "rock":
        if computer == "paper":
            return "paper covers rock! Result: Computer Won!"
        else: 
            return "rock smashes scissors! Result: You Won!"
    elif player == "paper":
        if computer == "scissors":
            return "scissors cut paper! Result: Computer Won!"
        else: 
            return "paper covers rock! Result: You Won!"
    else:
        if computer == "rock":
            return "rock smashes scissors! Result: Computer Won!"
        else: 
            return "scissors cut paper! Result: You Won!"
    

choices = get_choices()
result = get_result(choices)
print(result)


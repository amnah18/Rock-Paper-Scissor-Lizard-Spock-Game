import random

# Define the choices and rules
choices = ["rock", "paper", "scissor", "lizard", "spock"]
rules = {
    "rock": ["scissor", "lizard"],
    "paper": ["rock", "spock"],
    "scissor": ["paper", "lizard"],
    "lizard": ["paper", "spock"],
    "spock": ["rock", "scissor"]
}

# Game logic
print("Rock Paper Scissor Lizard Spock Game")
your_choice = input("Enter your choice: ").lower()

if your_choice not in choices:
    print("Invalid input! Please choose from rock, paper, scissor, lizard, or spock.")
else:
    computer = random.choice(choices)
    print(f"You chose {your_choice} and Computer chose {computer}")

    if your_choice == computer:
        print("It's a tie!")
    elif computer in rules[your_choice]:
        print(f"{your_choice.capitalize()} beats {computer}! You win!")
    else:
        print(f"{computer.capitalize()} beats {your_choice}! You lose!")

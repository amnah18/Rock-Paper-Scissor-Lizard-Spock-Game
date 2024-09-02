#Rock Paper Scissor Lizard Spock game 
import random
print("Rock Paper Scissor Lizard Spock Game")
your_choice= input("Enter your choice:")
choices=["Rock", "Paper", "Scissor"]
choices.append("Lizard")
choices.append("Spock")
computer = random.choice(choices) 
print(f"You choose {your_choice} and Computer choose {computer}")

if your_choice==computer:
    print("It's a tie!")
else:
    if your_choice == "Rock" and computer == "Scissor":
        print("Rock smashes Scissor! You win!")
    elif your_choice == "Paper" and computer == "Scissor":
        print("Scissor cuts Paper! You Lose!")
    elif your_choice == "Scissor" and computer == "Paper":
        print("Scissor cuts Paper! You Win!")
    elif your_choice == "Rock" and computer == "Paper":
        print("Paper covers Rock! You Lose!")
    elif your_choice == "Paper" and computer == "Rock":
        print("Paper covers Rock! You win!")
    elif your_choice == "Scissor" and computer == "Rock":
        print("Rock smashes Scissor! You Lose!")
    elif your_choice == "Rock" and computer == "Lizard":
        print("Rock Crushes Lizard! You Win")
    elif your_choice == "Lizard" and computer == "Rock":
         print("Rock Crushes Lizard! You Lose")
    elif your_choice == "Rock" and computer == "Spock":
        print("Spock vaporizes Rock! You Lose")
    elif your_choice == "Spock" and computer == "Rock":
        print("Spock vaporizes Rock! You Win")
    elif your_choice == "Paper" and computer == "Lizard":
        print("Lizard eats Paper! You Lose")
    elif your_choice == "Lizard" and computer == "Paper":
        print("Lizard eats Paper! You Win")
    elif your_choice == "Paper" and computer == "Spock":
        print("Paper disproves Spock! You Win")
    elif your_choice == "Spock" and computer == "Paper":
        print("Paper disproves Spock! You Lose")
    elif your_choice == "Scissor" and computer == "Lizard":
        print("Scissor decapitates Lizard! You Win")
    elif your_choice == "Lizard" and computer == "Scissor":
        print("Scissor decapitates Lizard! You Lose")
    elif your_choice == "Scissor" and computer == "Spock":
        print("Spock smashes Scissor! You Lose")
    elif your_choice == "Spock" and computer == "Scissor":
        print("Spock smashes Scissor! You Win")
    else:
        print("Invalid input")
print(choices)
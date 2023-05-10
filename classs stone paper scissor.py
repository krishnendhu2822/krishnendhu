import random
options = ["stone", "paper", "scissors"]
num_rounds = int(input("How many rounds do you want to play? "))
user_score = 0
computer_score = 0
class game:
    def checker(num_rounds):
        global computer_score, user_score
        for round_num in range(num_rounds):
            print("Round", round_num + 1)
            user_choice = input("Choose stone, paper, or scissors: ")
            computer_choice = random.choice(options)
            print("Computer chose", computer_choice)
            if user_choice == computer_choice:
                print("It's a tie!")
            elif user_choice == "stone" and computer_choice == "paper":
                print("Computer wins this round!")
                computer_score += 1
            elif user_choice == "stone" and computer_choice == "scissors":
                print("You win this round!")
                user_score += 1
            elif user_choice == "paper" and computer_choice == "stone":
                print("You win this round!")
                user_score += 1
            elif user_choice == "paper" and computer_choice == "scissors":
                print("Computer wins this round!")
                computer_score += 1
            elif user_choice == "scissors" and computer_choice == "stone":
                print("Computer wins this round!")
                computer_score += 1
            elif user_choice == "scissors" and computer_choice == "paper":
                print("You win this round!")
                user_score += 1
game.checker(num_rounds)
print("Final scores:")
print("You:", user_score)
print("Computer:", computer_score)
if user_score > computer_score:
    print("You win!")
elif computer_score > user_score:
    print("Computer wins!")
else:
    print("It's a tie!")

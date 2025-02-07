
from random import randint

# Create A List Of Play Options
t = ["Rock", "Paper", "Scissors"]

# Assign A Random Play To The Computer
computer = t[randint(0,2)]

# Set Player To False
player = False

while player == False:
    player = input("Rock, Paper, Scissors?\n")
    if player == computer:
        print("Tie.\n")
    elif player == "Rock":
        if computer == "Paper":
            print("You Lose.", computer, "Covers", player, "\n")
        else:
            print("You Win.", player, "Covers", computer, "\n")
    elif player == "Paper":
        if computer == "Scissors":
            print("You Lose.", computer, "Cuts", player, "\n")
        else:
            print("You Win.", player, "Covers", computer, "\n")
    elif player == "Scissors":
        if computer == "Rock":
            print("You Lose.", computer, "Smashes", player, "\n")
        else:
            print("You Win.", player, "Cuts", computer, "\n")
    else:
        print("Invalid play. Check your spelling.\n")

    player = False
    computer = t[randint(0,2)]


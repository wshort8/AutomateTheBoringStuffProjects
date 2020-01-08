# updated 1/7/2020

import random
import sys
wins = 0
losses = 0
ties = 0

print("\nROCK PAPER SCISSORS")

while True:
    print("%s Wins, %s Losses, %s Ties \n" %(wins, losses, ties))
    while True:
        print("Welcome to the game. Please select (r)ock, (p)aper, (s)cissors or (q)uit. \n")
        playerMove = input("Enter your selection: ")
        if playerMove == 'q':
            sys.exit()
        elif playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break
        print("Please make a selection from these options: r, p, s or q ")
    if playerMove == 'r':
        print("ROCK vs....")
    elif playerMove == 'p':
        print("PAPER vs....")
    elif playerMove == 's':
        print("SCISSORS vs....")

#translate computer randInt into a 'letter' choice
    computerMove = random.randint(1,3)
    if computerMove == 1:
        computerMove = 'r'
        print("ROCK")
    elif computerMove == 2:
        computerMove = 'p'
        print ("PAPER")
    elif computerMove == 3:
        computerMove = 's'
        print ("SCISSORS")

#check translated computer against
    if playerMove == computerMove:
        print("It's a TIE! \n")
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print("You WIN! \n")
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print("You LOSE. \n")
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print("You LOSE. \n")
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 'r':
        print("You WIN! \n")
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'r':
        print("You LOSE. \n")
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'p':
        print("You WIN! \n")
        wins = wins + 1
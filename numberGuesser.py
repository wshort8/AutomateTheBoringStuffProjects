import random

# main loop of guessing game
def guessResult():
    secretNumber = random.randint(1, 20)
    guessNumber = 0
    while True:
        guessNumber += 1
        guess = int(input("\nI'm thinking of a number between 1 and 20. What is your guess? \nTYPE A NUMBER: "))
        if guess == secretNumber:
            print("Congratulations, your guess of " + str(guess) + " is correct. \n You got the correct answer in " + str(guessNumber) + " guesses \n")
            guessNumber = 0
            retry = str(input("Would you like to play again? yes/no \n"))
            if retry == str('yes'):
                guessResult()
            else:
                print("Goodbye")
                break
        elif 0 < guess < secretNumber:
            print("Your guess is too low, try again \n")
        elif 21 > guess > secretNumber:
            print("Your Guess is too high, try again \n")
        else:
            print("Invalid choice, please select and integer between 1-20 \n")


guessResult()


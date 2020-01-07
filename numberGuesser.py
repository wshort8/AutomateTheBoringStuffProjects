import random


secretNumber = random.randint(1,20)
guessNumber = 0

def guessResult(guessNumber):
    while True:
        guessNumber += 1
        guess = int(input("I'm thinking of a number between 1 and 20. What is your guess?"))
        if guess == secretNumber:
            print("Congratulations, your guess of " + str(guess) + " is correct. \n You got the correct answer in " + str(guessNumber) + " guesses \n")
            break
        elif guess < secretNumber:
            print("Your guess is too low, try again")
            guessResult(guessNumber)
        elif guess > secretNumber:
            print("Your Guess is too high, try again")
            guessResult(guessNumber)

guessResult(guessNumber)


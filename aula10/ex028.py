# Create a program that makes the PC think in an integer
# between 0 e 5 and ask for the user figure out which
# number was chosen by the computer. The program should write
# in the screen if the user won or lost

import random

number = random.randrange(0, 5)

userNumber = int(input("Please enter a number between 1 and 5: "))

if number == userNumber:
    print("You did it, guessed the right number!")
else:
    print("You lose, better luck next time!")

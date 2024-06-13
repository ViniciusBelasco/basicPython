# Create a program that reads a real number from input and shows in
# the screen its integer portion on the screen.

import math

number = float(input("Please insert a real number: "))

print(
    "The integer number from {:.3f} is {}".format(number, math.floor(number))
)

# Create a program that read a real number from input and show in
# the screen its int portion

import math

number = float(input("Please insert a real number: "))

print(
    "The integer number from {:.3f} is {}".format(number, math.floor(number))
)

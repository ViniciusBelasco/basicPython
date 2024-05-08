# Create a program that reads the oposite lenght cathetus
# and the adjacent of a right triangle. Calculate and show
# the hipotenuse's lenght

import math

higth = float(input("Lenght of oposite side: "))
widgth = float(input("Leght of adjacent leg: "))

hipotenuse = math.sqrt(math.pow(higth, 2) + math.pow(widgth, 2))

print("The hipotenuse will measure: {:.2f}".format(hipotenuse))

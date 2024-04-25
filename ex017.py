# Create a program that reads the oposite lenght cathetus
# and the adjacent of a right triangle. Calculate and show
# the hipotenuse's lenght

import math

higth = float(input("Please enter the triangle's higth: "))
widgth = float(input("Please enter the triangle's widgth: "))

hipotenuse = math.sqrt(math.pow(higth, 2) + math.pow(widgth, 2))

print(hipotenuse)

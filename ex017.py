# Create a program that reads the oposite lenght cathetus
# and the adjacent of a right triangle. Calculate and show
# the hipotenuse's lenght

import math

option = int(
    input(
        "please enter how you want to calculate the hipotenuse\n"
        "basic math = 1 or math module 2: "
    )
)

higth = float(input("Lenght of oposite side: "))
width = float(input("Leght of adjacent leg: "))

if option == 1:
    hipotenuse = math.sqrt(math.pow(higth, 2) + math.pow(width, 2))

elif option == 2:
    hipotenuse = math.hypot(higth, width)

else:
    hipotenuse = (higth**2 + width**2) ** (1 / 2)


print("The hipotenuse will measure: {:.2f}".format(hipotenuse))

# Create a program that reads an angle and show in the screen
# it's value os sine, cossine , tangent.

import math

angle = float(input("Insert and angle: "))

sine = math.sin(math.radians(angle))
cossine = math.cos(math.radians(angle))
tangent = math.tan(math.radians(angle))

print(
    "The angle {:.2f} have a sine of {:.2f} a cossine of {:.2f} "
    "and a tangent of {:.2f}".format(angle, sine, cossine, tangent)
)

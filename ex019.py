# A teacher want to draw one of your four studants to erease the
# board. Do a program to help him, inputing his studants names and
# printing the name of the chosen studant.

import random

number = int(input("How many studants will be in draw? "))
studants = []

for i in range(number):
    studants.append(str(input("Insert a studant name ")))
    pass

draw_studant = random.randint(0, len(studants)-1)

print("The selected studant is {}".format(studants[draw_studant]))

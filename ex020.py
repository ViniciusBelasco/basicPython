# A teacher want to draw the order of studants apresentation.
# Do a program to help him, inputing his studants names and
# printing the name of the sorted order.

import random

number = int(input("How many studants will be in draw? "))
studants = []

for i in range(number):
    studants.append(input("Insert a studant name "))
    pass

random.shuffle(studants)

for i in range(number):
    print("{} a apresentar é {}!".format(i+1, studants[i]))
    pass

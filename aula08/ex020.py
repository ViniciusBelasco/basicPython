# A teacher wants to draw the order of studant's presentations.
# Create a program to help him inputing the studant's names and
# printing the names in the sorted order.

import random

number = int(input("How many studants will be in draw? "))
studants = []

for i in range(number):
    studants.append(input("Insert a studant name "))
    pass

random.shuffle(studants)

print("The order for presentation is: {}!".format(studants))

# Do a program that reads a number of 0 to 9999 and show
# in the screen each one of the digits separetaly.
# EX: Digite um número : 1834
#   unit: 4
#   dozens: 3
#   hundreds: 8
#   thousands: 1

fullNumber = input("Type a number: ")
splitedNumber = []

for x in range(len(fullNumber)):

    splitedNumber.append(fullNumber[x])
    pass

splitedNumber.reverse()

for x in range(len(splitedNumber)):

    unit = ''
    if x == 0:
        unit = 'unit'
    elif x == 1:
        unit = 'dozens'
        pass
    elif x == 2:
        unit = 'hundreds'
        pass
    else:
        unit = 'thousands'
        pass

    print("{} {}".format(unit, splitedNumber[x]))
    pass

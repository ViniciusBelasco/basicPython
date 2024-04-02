def multiplicationtable(number):

    for x in range(1, 11):
        print("{} X {} is: {}".format(number, x, number * x))
    return


number = int(input("Which multiplication table do you want to see? "))

multiplicationtable(number)

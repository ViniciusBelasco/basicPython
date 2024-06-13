def double(number):

    return number * 2


def triple(number):

    return number * 3


def squareRootOf(number):

    return number ** (1 / 2)


number = int(input("Write a number: "))

print("The number is {}".format(number))
print("It's double is {}".format(double(number)))
print("It's triple is {}".format(triple(number)))
print("It's square root is {:.3f}".format(squareRootOf(number)))

def decimeter(number):

    return number * 10


def centimeters(number):

    return number * 1000


def milimeters(number):

    return number * 10000


def kilometers(number):

    return number / 1000


def hectometer(number):

    return number / 100


def decameter(number):

    return number / 10


meters = float(input("Meters for convertion: "))

print("The distance of {}m matches to:")
print(
    "{}Km \n {}Hm \n {}Dam \n {}Dm \n {}cm \n {}Mm".format(
        kilometers(meters),
        hectometer(meters),
        decameter(meters),
        decimeter(meters),
        centimeters(meters),
        milimeters(meters)
    )
)

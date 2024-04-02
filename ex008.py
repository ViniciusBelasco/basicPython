def centimeters(number):

    return number * 100


def milimeters(number):

    return number * 1000


meters = float(input("Meters for convertion: "))

print("{} Meters in centimeters is {} cm".format(meters, centimeters(meters)))
print("{} meters in milimeters is {} mm".format(meters, milimeters(meters)))

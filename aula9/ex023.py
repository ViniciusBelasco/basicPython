# Create a program that reads a number from 0 to 9999 and shows each of its
# digits separately on the screen.
# EX: Enter a number: 1834
#   unit: 4
#   Tens: 3
#   Hundreds: 8
#   Thousands: 1

# Solução do professor guanabara
# n = int(input('informe um número: '))
# u = num // 1 % 10
# d = num // 10 % 10
# c = num // 100 % 10
# m = num // 1000 % 10
#
# print('Analisando o número {}'.format(num))
# print('Unidade {}'.format(u))
# print('Dezena {}'.format(d))
# print('Centena {}'.format(c))
# print('Milhar {}'.format(m))
#

fullNumber = input("Type a number: ")
splitedNumber = []

for x in range(len(fullNumber)):

    splitedNumber.append(fullNumber[x])
    pass

splitedNumber.reverse()

for x in range(len(splitedNumber)):

    unit = ""
    if x == 0:
        unit = "unit"
    elif x == 1:
        unit = "dozens"
        pass
    elif x == 2:
        unit = "hundreds"
        pass
    else:
        unit = "thousands"
        pass

    print("{} {}".format(unit, splitedNumber[x]))
    pass

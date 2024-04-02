def predecessor(number):

    return number - 1


def sucessor(number):

    return number + 1


n1 = int(input("Write a number: "))

print(
    "The number is {}, the predecessor is {}, and de sucessor is {}!".format(
        n1, predecessor(n1), sucessor(n1)
    )
)

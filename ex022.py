# Create a program that input the full name of a person and show:
# 1 - The name with all upper letters
# 2 - The name with all lower letters
# 3 - How many letters the string have (with no spaces)
# 4 - How many letters the first name has

fullName = str(input("Please enter your name: "))

print(
    "The full name in uppercase is {}. \n"
    "In lowercase is {}. \n"
    "It's lenght is {} \n"
    "And the first name lenght is {}".format(
        fullName.upper(),
        fullName.lower(),
        len(fullName) - fullName.count(' '),
        len(fullName.split()[0])
    )
)

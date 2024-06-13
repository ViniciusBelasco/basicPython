# Create a program that input the full name of a person and shows:
# 1 - The name with all uppercase letters
# 2 - The name with all lowercase letters
# 3 - How many letters the name has (excluding spaces)
# 4 - How many letters the first name has

fullName = str(input("Please enter your name: ")).strip()

print(
    "The full name in uppercase is {}. \n"
    "In lowercase is {}. \n"
    "It's length is {} \n"
    "And the first name length is {}".format(
        fullName.upper(),
        fullName.lower(),
        len(fullName) - fullName.count(' '),
        len(fullName.split()[0])  # Outra passibilidade é
                                  # usar o fullName.find(' ')
    )
)

# Create a program that reads the full name of a person and then shows
# the first and last name separately.

name = str(input("Enter yout entire name: "))

splitedName = name.split()

print(len(splitedName))

print(
    "Your first name is {} and your last name is {}".format(
        splitedName[0], splitedName[len(splitedName)-1]
    )
)

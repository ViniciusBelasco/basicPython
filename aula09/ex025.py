# Create a program that reads the name of a person and
# tells if they have "SILVA" in their name

personName = input("Please enter your name: ")

if personName.upper().find("SILVA") >= 0:
    findMessage = "have SILVA"
else:
    findMessage = "don't have SILVA"

print("Your name {}".format(findMessage))

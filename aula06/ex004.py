userInput = input("Type anything and I will tell you a lote about it! ")

print("This is the type of your input: {}".format(type(userInput)))

print("Is this alpha numeric? {} ".format(userInput.isalnum()))
print("Is this alphabetic? {}".format(userInput.isalpha()))
print("Is this ASCII? {}".format(userInput.isascii()))
print("Is this a digit? {}".format(userInput.isdigit()))
print("Is this lower case? {}".format(userInput.islower()))
print("Is this upper case? {}".format(userInput.isupper()))
print("Is this a space? {}".format(userInput.isspace()))
print("Is this a titlle? {}".format(userInput.istitle()))
print("Is this a decimal number? {}".format(userInput.isdecimal()))
print("Is this numeric? {}".format(userInput.isnumeric()))
print("Is this printable? {}".format(userInput.isprintable()))

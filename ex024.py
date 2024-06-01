# Create a program that reads the name of a city, and sai if it begins
# or not with the name SANTO

cityName = input("Enter your city name: ")
startOrNot = ""

if cityName[0:5].upper() == "SANTO":
    startOrNot = "start with"
else:
    startOrNot = "don't start with"

print("Your city {} SANTO".format(startOrNot))

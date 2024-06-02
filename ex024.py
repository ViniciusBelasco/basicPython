# Create a program that reads the name of a city and says if it begins
# with 'SANTO' or not

cityName = input("Enter your city name: ")
startOrNot = ""

if cityName[0:5].upper() == "SANTO":
    startOrNot = "start with"
else:
    startOrNot = "don't start with"

print("Your city {} SANTO".format(startOrNot))

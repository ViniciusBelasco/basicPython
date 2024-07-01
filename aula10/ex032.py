# Create a program that reads a year and show if it is a leap year

year = str(input("Which year do you wanna check? ")).strip().upper()

if (int(year[2:4]) % 4) == 0:
    print("It is a leap year")
else:
    print("It isn't a leap year")

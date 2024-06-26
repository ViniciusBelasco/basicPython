# Create a program that reads the speed of a car.
# If he exceeds 80Km/h, show a message saying he has been fined
# The fine will cost R$ 7,00 for each KM above the limit

speed = float(input("Registred speed: "))
tax = 7.00

if speed > 80.0:
    fine = (speed - 80.0) * tax
    print("You have been fined in R${:.2f}!".format(fine))

# Create a program that reads the distance of a trip in km.
# Calculate the ticket price, charging R$ 0.50 per Km for trips
# up to 200 kilometers and R$ 0.45 for longer trips

tripDistance = float(input("What's the distance of your trip? "))
distanceCharge = 0.50

if tripDistance >= 200:
    distanceCharge = 0.45

print("For this trip you will pay {:.2f}".format(tripDistance*distanceCharge))

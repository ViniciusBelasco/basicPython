# Write a program that convert an input temperature in
# celcius to fahrenheit

celcius = float(input("Insert the temperature in Celcius degrees: "))
fahrenheit = (celcius - 32) * (5 / 9)

print(
    "The temperature of {:.1f} in Celcius degrees matches"
    " to {}F degrees!".format(celcius, fahrenheit)
)

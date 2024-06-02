# Create a program which asks how much kilometers a rented car
# has been driven and how many days it was rented. Calculate how much
# money the rent costs, knowing that the daily cost of the car cost is
# 60 real and 0.15 real for each kilometers driven.

km_driven = float(input("How many kilometers have you drive? "))
days_rent = int(input("How many days have you rent it? "))

day_cost = 60
km_cost = 0.15

full_price = float((km_driven * km_cost) + (days_rent * day_cost))

print(
    "Using the car for {} kilometers for {} days, you have"
    " to pay {:.2f}R$".format(km_driven, days_rent, full_price)
)

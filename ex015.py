# write a program which asks how much Km a rented car
# has been driven and how many days it was rent. Calculate how much money
# the rent cost, knowing that the car cost is 60 real for a dai and 0.15
# real for km driven.

km_driven = float(input("How many kilometers have you drive? "))
days_rent = int(input("How many days have you rent it? "))

day_cost = 60
km_cost = 0.15

full_price = float((km_driven * km_cost) + (days_rent * day_cost))

print(
    "Using the car for {} kilometers for {} days, you have"
    " to pay {:.2f}R$".format(km_driven, days_rent, full_price)
)

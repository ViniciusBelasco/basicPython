# Do an Algorithm thar read the employ's salary and
# show the new salary, with 15% of increase.

salary = float(input("Actual wage: "))

increase = salary * 0.15

print(
    "Your actual wage is {:.2f},"
    "and your wage with a rise of 15% "
    "will be {:.2f}!".format(salary, salary + increase)
)

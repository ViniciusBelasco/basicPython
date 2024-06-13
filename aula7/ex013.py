# Create an Algorithm that reads the employee's salary and
# shows their new salary with a 15% increase.

salary = float(input("Actual wage: "))

increase = salary * 0.15

print(
    "Your actual wage is {:.2f},"
    "and your wage with a rise of 15% "
    "will be {:.2f}!".format(salary, salary + increase)
)

# Create an algorithm that reads the price of a product
# and shows its new price with a 5% discount.

price = float(input("Product price: "))
discount = price * 0.05

print("The product price with discount is {}".format(price-discount))

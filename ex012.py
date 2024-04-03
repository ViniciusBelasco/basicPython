# Do an algorithm that read the price of a product
# and show it's new price, whith 5% discount

price = float(input("Product price: "))
discount = price * 0.05

print("The product price with discount is {}".format(price-discount))

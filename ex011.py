# Do a program that input hight and width of a wall and calculate
# it's area and how much paint will be needed to paint it. Knowing each
# liter of paint can be used in 2m square of wall

hight = float(input("What is the wall hight: "))
width = float(input("What is the wall width: "))

area = hight * width
amount_paint = area/2

print("This amount of dye can paint {} square meters!".format(amount_paint))

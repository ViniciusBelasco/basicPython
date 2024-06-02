# Create a program that inputs height and width of a wall and calculates
# its area and how much paint will be needed to paint it. Knowing each
# liter of paint can cover 2 square meters of wall.

hight = float(input("What is the wall hight: "))
width = float(input("What is the wall width: "))

area = hight * width
amount_paint = area/2

print("This amount of dye can paint {} square meters!".format(amount_paint))

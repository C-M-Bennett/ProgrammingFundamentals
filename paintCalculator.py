# algorithm for calculating the number of tins of paint needed for painting a wall with 2 coats of paint
# M = meters
# MSq = meters square
# 1 tin covers 10m^2
import math

wallHeightM = 5
wallWidthM = 2.5
#calculate area of the wall
wallAreaMSq = wallHeightM*wallWidthM
print("The wall is {} meters squared".format(wallAreaMSq))
#multiply by 2 for 2 coats and then divide by paint coverage
totalPaintAreaMSq = wallAreaMSq*2
totalNeeded = totalPaintAreaMSq/10
#round total up to nearest whole number
tinsNeeded = math.ceil(totalNeeded)
print(tinsNeeded, "tins of paint are needed for 2 coats on this wall")
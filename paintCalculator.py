# algorithm for calculating the number of tins of paint needed for painting a wall with 2 coats of paint
# M = meters
# MSq = meters square
# 1 tin covers 10m^2
import math

wallHeightM = int(input("Enter the height of the wall in meters:"))
wallWidthM = int(input("Enter the width of the wall in meters:"))
#calculate area of the wall
wallAreaMSq = wallHeightM*wallWidthM
print("Your measurements mean the wall is {} meters squared".format(wallAreaMSq))
#multiply by 2 for 2 coats and then divide by paint coverage
totalPaintAreaMSq = wallAreaMSq*2
totalNeeded = totalPaintAreaMSq/10
#round total up to nearest whole number
tinsNeeded = math.ceil(totalNeeded)
print(tinsNeeded, "tin(s) of paint are needed for 2 coats on this wall")
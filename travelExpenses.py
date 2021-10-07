# User inputs
firstName = ("Bob")
surname = ("Smith")
jobTitle = ("Lecturer")
startMileage = (20000)
endMileage = (20050)

hotelCostDay1 = (100)
foodCostDay1 = (20)
transportCostDay1 = (10)

hotelCostDay2 = (100)
foodCostDay2 = (50)
transportCostDay2 = (20)

hotelCostDay3 = (100)
foodCostDay3 = (25)
transportCostDay3 = (10)

# Calculations
# calculate fuel using constant for price per mile
FUELPRICE = 0.43 
mileageUsed = endMileage-startMileage
fuelTotal = mileageUsed * FUELPRICE

# create function for calculating total for a day
def total (item1, item2, item3):
    ans = item1 + item2 + item3
    return ans

# use "total" function to get 3 day totals for hotel, food and transport
hotelTotal = total (hotelCostDay1, hotelCostDay2, hotelCostDay3)
foodTotal = total (foodCostDay1, foodCostDay2, foodCostDay3)
transportTotal = total (transportCostDay1, transportCostDay2, transportCostDay3)

# test calculations
# print(hotelTotal)
# print(foodTotal)
# print(transportTotal)



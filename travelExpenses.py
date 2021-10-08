# User inputs
firstName = input("Please enter the first name:")
surname = input("Please enter the surname:")
jobTitle = input("Please enter the job title:")
startMileage = int(input("Please enter the pre trip mileage:"))
endMileage = int(input("Please enter the post trip mileage:"))

hotelCostDay1 = int(input("Please enter the hotel cost for day 1:"))
foodCostDay1 = int(input("Please enter the food cost for day 1:"))
transportCostDay1 = int(input("Please enter the transport cost for day 1:"))

hotelCostDay2 = int(input("Please enter the hotel cost for day 2:"))
foodCostDay2 = int(input("Please enter the food cost for day 2:"))
transportCostDay2 = int(input("Please enter the transport cost for day 2:"))

hotelCostDay3 = int(input("Please enter the hotel cost for day 3:"))
foodCostDay3 = int(input("Please enter the food cost for day 3:"))
transportCostDay3 = int(input("Please enter the transport cost for day 3:"))

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

# calculate overal total for trip
overallTotal = fuelTotal + hotelTotal + foodTotal + transportTotal

# test calculations
# print(hotelTotal)
# print(foodTotal)
# print(transportTotal)

# Display the total to be reimbursed as well as itemised
print("\nThe following details have been entered:\n")
print("Name: " + surname + ", " + firstName)
print("Job: " + jobTitle)
print("Overall reimbursement due" , overallTotal)
print("\nFuel cost reimbursement:" ,fuelTotal)
print("Hotel costs reimbursement:" , hotelTotal)
print("Food costs reimbursement:" , foodTotal)
print("Transport costs reimbursement:" , transportTotal)

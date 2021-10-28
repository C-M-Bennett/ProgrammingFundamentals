#define variables to store input, sum and total inputs
sumNumber = 0
totalEntries = 0
number = 0

#error message if first number is 0
while (number == 0):
    number = int(input("Please enter a number that is not zero: "))
#updates with last none zero number entered
sumNumber += number
totalEntries += 1

#enter a number
while (number != 0):
    number = int(input("Enter another number (0 to exit): "))
    if number != 0:
        sumNumber += number 
        totalEntries += 1
 #could alternatively have the following
 #sumNumber += number 
 #totalEntries += (number !=0)
 #uses Python's interpretation of true and false as 1 and 0

#calculate average (dont include 0)
average = sumNumber / totalEntries
print("The sum is:" , sumNumber)
print("The total numbers is:" , totalEntries)
print("The average is:", average)
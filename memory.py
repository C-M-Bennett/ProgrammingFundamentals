# A program to simulate memory with two different management techniques
# NOTE - each page to save is represented by a positive integer
# NOTE - memory capacity is 8 pages

memory = []
numberList = []
frequency = {}
userInput = ""
menuOption = ""


# firstOut = remove first index in memory
def firstOut():
    for integer in numberList:
        # check if integer already in memory and print hit if so
        if integer in memory:
            print("Hit")

        # check if memory list is full
        elif len(memory) == 8:
            print("Miss")
            # access value in index 0 (first in) and remove
            del memory[0]
            memory.append(integer)

        # if integer not in memory then print miss and add to memory
        elif integer not in memory:
            print("Miss")
            memory.append(integer)


# lowestFreq = remove integer with lowest freq or if equal, lower number.
def lowestFreq():
    for integer in numberList:
        # check if already in memory, print hit if so and incremement freq
        if integer in memory:
            print("Hit")
            frequency[integer] += 1

        # check if memory list is full
        elif len(memory) == 8:
            # create a temp copy of freq dict to keep global freq continuous
            tempFrequency = {}
            for i in memory:
                tempFrequency[i] = frequency[i]

            # make dict into a list of tuples to enable sorting
            freqList = []
            for item in tempFrequency.items():
                freqList.append(list(item))

            # sort the list by frequency and then page
            sortFreqList = sorted(freqList, key=lambda x: (x[1], x[0]))

            # make list into dict to get lowest value and remove from memory
            sortFreqDict = {item[0]: item[1:] for item in sortFreqList}
            lowestValue = min(sortFreqDict, key=sortFreqDict.get)
            memory.remove(lowestValue)
            memory.append(integer)
            print("Miss")

            # add to global frequency dict
            if integer not in frequency:
                frequency[integer] = 1
            elif integer in frequency:
                frequency[integer] += 1

        # if not in memory then miss printed, added to memory and freq set to 1
        elif integer not in memory:
            print("Miss")
            memory.append(integer)
            if integer not in frequency:
                frequency[integer] = 1
            elif integer in frequency:
                frequency[integer] += 1


# create a menu for user options
def menu():
    menuOption = str.upper(input("Please press 1 for firstOut, or press 2 for lowestFreq, or press Q to quit the program: "))
    # check input is an accepted option
    while (menuOption != "1" and menuOption != "2" and menuOption != "Q"):
        print("I'm sorry, that wasn't an option.")
        menuOption = str.upper(input("Please try again and enter 1 for firstOut, 2 for lowestFreq, or Q to quit: "))

    if menuOption == "1":
        firstOut()
    if menuOption == "2":
        lowestFreq()
    if menuOption == "Q":
        print("You have chosen to quit the program. Goodbye")
        exit()
    print("The memory contains the following: ", memory)

    # empty dictionaries ready for next set of inputs
    memory.clear()
    numberList.clear()
    frequency.clear()


# ask for input until Q is inputted to quit
while menuOption != "Q":
    while userInput != "0":
        try:
            userInput = int(input("Please enter an integer you would like to save to the memory (enter 0 to stop): "))
            if userInput != 0:
                numberList.append(userInput)
            if userInput == 0:
                menu()
        except ValueError:
            print("Sorry, that isn't an integer.")

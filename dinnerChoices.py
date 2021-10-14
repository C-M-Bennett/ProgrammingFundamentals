wantsMain = False
wantsDessert = False
guestNumber = 1
totalMain = 0
totalDessert = 0

#def guestChoice (guest1, guest2, guest3):


while (guestNumber < 4):

    #welcome guest and get name
    print("Guest number", guestNumber)
    guestName = input("Please type your name:")
    print("Welcome "+ guestName +"!")

    #ask guest if they want "main", "dessert", "both", or "none"
    main = str.lower(input("Would you like a main course? Please type 'Yes' if you do and 'No' if you do not: "))
    dessert = str.lower(input("Would you like a dessert course? Please type 'Yes' if you do and 'No' if you do not: "))

    if(main == "yes"):
        wantsMain = True
        
    if(dessert == "yes"):
        wantsDessert = True
        

    if (wantsMain == True and wantsDessert == True):
        print(guestName, "wants both main and dessert")
        totalMain = totalMain + 1
        totalDessert = totalDessert + 1

    elif (wantsMain == False and wantsDessert == False):
        print(guestName, "doesnt want any food")

    elif (wantsMain == True and wantsDessert == False):
        print(guestName, "only wants a main course")
        totalMain = totalMain + 1

    elif (wantsMain == False and wantsDessert == True):
        print(guestName, "only wants a dessert")
        totalDessert = totalDessert + 1

    else:
        print("Sorry, I dont think that's an option")

    
    guestNumber = guestNumber + 1
    wantsMain = False
    wantsDessert = False
    #print(guestNumber)



#take guest choice and output total mains
#output total desserts
print("total number of main courses needed =", totalMain)
print("total number of desserts needed =", totalDessert)


#def order():
    #return guestName, wantsMain, wantsDessert

#print(wantsMain)
#print(order)

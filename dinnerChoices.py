wantsMain = False
wantsDessert = False
guestNumber = 1
totalMain = 0
totalDessert = 0

guestList = []
guestChoiceMain = []
guestChoiceDessert = []

def guestOrder():
    #ask guest if they want "main", "dessert", "both", or "none"
    main = str.lower(input("Would you like a main course? Please type 'Yes' if you do and 'No' if you do not: "))
    dessert = str.lower(input("Would you like a dessert course? Please type 'Yes' if you do and 'No' if you do not: "))

    #add main
    if(main == "yes"):
        wantsMain = True
        guestChoiceMain.append("a main course")
        global totalMain 
        totalMain = totalMain + 1

    elif(main == "no"):
        wantsMain = False
        guestChoiceMain.append("no main course")

    else:
        print("Sorry, I dont think that's an option")
    
    #add dessert    
    if(dessert == "yes"):
        wantsDessert = True
        guestChoiceDessert.append("a dessert")
        global totalDessert 
        totalDessert = totalDessert + 1

    elif(dessert == "no"):
        wantsDessert = False
        guestChoiceDessert.append("no dessert")

    else:
        print("Sorry, I dont think that's an option")   
    return

while (guestNumber < 4):

    #welcome guest and get nameChoice
    print("Guest number", guestNumber)
    nameChoice = input("Please type your name:")
    print("Welcome "+ nameChoice +"!")
    #call guestOrder function to ask questions and update totals
    guestOrder()
    guestList.append(nameChoice)
    guestNumber = guestNumber + 1
    
  
#take guest choice and output total mains
#output total desserts
print("\ntotal number of main courses needed =", totalMain)
print("total number of desserts needed =", totalDessert)
#output each guest's request

# for guests in guestList:
#     print(guests)
# for mains in guestChoiceMain:
#     print(mains)
# for desserts in guestChoiceDessert:
#     print(desserts)   

for x in range (3):
    print(guestList[x], "would like", guestChoiceMain[x], "and", guestChoiceDessert[x] + ".")
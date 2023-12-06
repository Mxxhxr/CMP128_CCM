#Python Final Project: Shopping List App
#Maahir Vohra
#12/20/21
#Shopping List App that lets users edit the shopping list.

#Dictionary with names, items, budgets, and status.
shoppers = { "Spiderman":{"Game":0,"Book":0,"Kindle":0,"budget":100,"status":"incomplete"},
             "Steve":{"Tie":0,"Scarf":0,"Amazon Echo":0,"budget":100,"status":"incomplete"},
             "Kevin":{"Mario Kart":0,"budget":65,"status":"incomplete"},
             "Jane":{"Gift Card":0,"Gloves":0,"budget":50,"status":"incomplete"},
             "Chris":{"Chocolates":0,"Galaxy Tab":0,"budget":100,"status":"incomplete"} }


#Creating the display menu function
#Pretty straightforward menu. Just a bunch of print functions.
def displayMenu():
    print("Menu")
    print("-----------------")
    print("Update Shopping List")
    print("Complete Shopping List")
    print("Display Shopping List")
    print("Exit Application")
    print("-----------------")
    print("Please Make your Selection:")


#Creating the exit application function, Also pretty simple, It  prints out
#a thank you message so that you can end the program.
def exitApplication():
    print("Thank you.")
    return False


#Creating the get choice function
#It basically look at the users answer to the input then looks at the first letter
#It then matches that letter with one of the if/elif statements and then does the
#Function that it says below it.
def getChoice():
    choice = input("What would you like to do? ")
    letter = choice.split(" ")
    if letter[0] == "U":
        printPeople()
        updateShoppingList(printItems())
    elif letter[0] == "C":
        printPeople()
        completeShoppingList()
    elif letter[0] == "D":
        displayShoppingList()
    elif letter[0] == "E":
        return exitApplication()
    else:
        print("Invalid Selection, please try again")
        getChoice()
    return True


#Display shopping list function that just shows all the shopping list information including the
#budget and if you are under/over the budget.
def displayShoppingList():
    for key in shoppers:
        total = 0
        print()
        print(key + ": ", end =" ")
        print(shoppers.get(key))
        for key2 in shoppers.get(key):
            if(key2!="budget" and key2!="status"):
                total+=shoppers.get(key).get(key2)
        print("Total Spent: ",total)
        budget = shoppers.get(key).get("budget")
        print("Budget Amount: ",budget)
        print("Under/Over Budget: ",budget-total)
        print()

    
#Small function that goes into the getChoice function to help make it work. Output's the shoppers names.
def printPeople():
    print("\nPeople:")
    for shopper in shoppers:
        print(shopper)


#Complete shopping list function that first asks who you want to update then it changes the status
#to that persons shopping list to "Complete"
def completeShoppingList():
    choice = input("\nWho are you updating? ")
    if choice in shoppers:
        shoppers.get(choice)["status"] = "complete"
        print("\n" + choice + "'s status is now complete\n")
    else:
        print("\nTry Again")
        completeShoppingList()


#Update shopping list function that asks who you want to update and then what item you are updating
#and the cost of the item you chose to update. When you type "D" for the getChoice function all the
#things you updated will show there.
def updateShoppingList(shopper):
    choice = input("\nWhat item are you updating? ")
    choice2 = input("What is the cost? ")
    dict = shoppers.get(shopper)
    if choice in dict:
        dict[choice] = int(choice2)
        print("Successfully updated ",choice)
    else:
        print("Try Again")
        updateShoppingList(shopper)


#Print items function that goes into the getChoice function to make it work.Inputs who you are updating
def printItems():
    choice = input("\nWho are you updating? ")
    if choice in shoppers:
        dict = shoppers.get(choice)
        print("\nItems:")
        for key in dict:
            if(key!="budget" and key!="status" ):
                print(key)
        return choice
    else:
        print("\nTry Again")
        return printItems()


#main program needed to run the code.
def main():
    cont = True
    while(cont):
        displayMenu()
        cont = getChoice()

if __name__ == "__main__":
    main()
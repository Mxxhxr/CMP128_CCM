#Maahir Vohra
#9/27/2021
#Program that calculate the total amount of a meal purchased.

#Ask the user to enter the charge for the food
Charge = float(input("Please enter the charge for the food. "))

#Calculate tip and tax.
Tip = 0.18 * Charge
Tax = 0.07 * Charge
Total = Charge + Tip + Tax

#Display message
print("Your tip is $",Tip,)
print("Your sales tax is $",Tax,)
print("Your total is $",Total,)

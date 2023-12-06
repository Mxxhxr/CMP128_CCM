#Maahir Vohra
#9/27/2021
#Program that calculates and displays taxes, total, and total with taxes.


#Ask for purchase amount.
PurchaseAmnt = float(input("Please enter the purchase amount. "))

#Calculate tax, tax total, and tale total.
StateSalesTax = .05 * PurchaseAmnt
CountySalesTax = 0.025 * PurchaseAmnt
TotalSalesTax = StateSalesTax + CountySalesTax
SaleTotal = PurchaseAmnt + TotalSalesTax

#Display message
print("The amount of purchase is $",PurchaseAmnt,)
print("The state sales tax is $",StateSalesTax,)
print("The county sales tax is $",CountySalesTax,)
print("The total sales tax is $",TotalSalesTax,)
print("The total of the sale is $",SaleTotal,)

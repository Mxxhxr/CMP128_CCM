#Maahir Vohra
#10/6/2021
#Program that calculates price of a speeding ticket.

#Ask speed limit and clocked speed.

SpeedLimit = int(input("What is the speed limit? "))
ClockedSpeed = int(input("What is the clocked speed? "))

#Calculate the fines

fine = 50 + (ClockedSpeed - SpeedLimit) * 5
FineOver90 = (50 + (ClockedSpeed - SpeedLimit) * 5) + 200

#Check to see if there will be a fine, and print the appropiate fine if there is one.

#Prints out fine for ticket under 90mph, over 90mph, and no fine.
if ClockedSpeed > SpeedLimit and ClockedSpeed < 90:
    print("Your fine will cost",fine," dollars.")
elif ClockedSpeed > SpeedLimit and ClockedSpeed >= 90:
    print("Your fine will cost",FineOver90,"dollars.")
else:
    ClockedSpeed <= SpeedLimit
    print("The speed was legal.")
   
    

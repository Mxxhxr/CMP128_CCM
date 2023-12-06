#Maahir Vohra
#10/25/21
#Takes the sum of two numbers and prints it. It then asks the user if they want to do it again.

while True:
    Digit1 = int(input("Enter your first number: "))
    Digit2 = int(input("Enter your second number: "))
    digitSum = Digit1 + Digit2
    print("The sum of your numbers is",digitSum)
    continueLoop = input("To continue adding numbers, enter the letter 'Y': ").upper()
    
    if continueLoop == "Y":
        continue

    else:
        break

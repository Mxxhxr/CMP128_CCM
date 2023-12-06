#total = 0
#anotherNumber = "yes"
#while anotherNumber == "yes":
#    number = int(input("Enter a number: "))
#    total = total + number
#    anotherNumber = input("Do you have another number? yes or no. ")    
#print("Your total is:",total)


total = 0
anotherNumber = "yes"
count = 1
while anotherNumber == "yes":
    number = int(input("Enter a number: "))
    total = total + number
    anotherNumber = input("Do you have another number? yes or no. ")
    if anotherNumber == "yes":
        count = count + 1

print("Your total is:",total)
print("Your average is:",total / count)

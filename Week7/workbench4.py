#Maahir Vohra
#10/25/2021
#Asks user to enter number 10 ten times and keeps a running total.
sum = 0
for counter in range(10):
    Number = input("Enter a number: ")
    sum += int(Number)
    
print(sum)

#Maahir Vohra
#10/6/2021
#Program that calculates eligibility for Senate and US Representative.

#Ask age and how long they have been a citizen

age = int(input("What is your age? "))
YearsOfCitizenship = int(input("How long have you been a US citizen? "))

#See if they are eligible for senate

if age >= 20 and YearsOfCitizenship >= 9:
    print("You are eligible for Senate.")

else:
    print("Sorry, you are not eligible for Senate.")
    
#See if they are eligible for representative

if age >= 25 and YearsOfCitizenship >= 7:
    print("You are eligible for US Representative.")

else:
    print("You are not eligible for US Representative.")

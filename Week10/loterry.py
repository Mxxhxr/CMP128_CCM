#Maahir Vohra
#11/17/21
#Prints out lottery numbers

#Set up
import random
lottery_numbers = []

#Appends random numbers to the lottery number list
for number in range(7):
	random_number = random.randint(0, 9)
	lottery_numbers.append(random_number)

#Prints out the lottery numbers
print("Your lottery numbers are: ", end = "")
for number in lottery_numbers:
	print(number, end = "")

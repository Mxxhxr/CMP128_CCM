number_list = []
user_number = input("Enter  20 numbers (add a space after each number): ").split()

#For loop
for number in user_number:
	number_list.append(int(number))

#Finds min max etc.
lowest_number = min(number_list)
highest_number = max(number_list)
total = sum(number_list)
average = total / 20

#Prints the answers
print(f"\nThe lowest number is {lowest_number}.")
print(f"The highest number is {highest_number}.")
print(f"The total is {total}.")
print(f"The average is {average}.")

#I found this way to string it together a few weeks ago^

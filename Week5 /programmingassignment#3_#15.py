#Maahir Vohra
#10/13/2021
#Program that asks the user to enter the number of seconds and prints out the number of minutes, hours, or days.

seconds = int(input("Please enter the number of seconds. "))

if seconds < 60:
    print(seconds, "seconds")
    
elif seconds >= 60 and seconds <= 3600:
    print(seconds // 60, "minutes and" ,seconds % 60, "seconds")

elif seconds >= 3600 and seconds <= 86400:
    print(seconds // 3600, "hours and", seconds % 3600 // 60, "minutes", "and", seconds % 60, "seconds")

else:
    seconds >= 86400 
    print(seconds // 86400, "days and", seconds % 86400 // 3600 , "hours", seconds % 86400 % 3600 // 60, "minutes and" , seconds % 60, "seconds")

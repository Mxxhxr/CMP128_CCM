#Maahir Vohra
#10/6/2021
#Program that calculates total wages for the week.

#Ask for number of hours worked and the hourly rate.

HoursWorked = float(input("How many hours did you work this week? "))
HourlyRate = float(input("How much is your hourly pay rate? "))

#Calculate wage and wage with overtime.

wage = HoursWorked * HourlyRate
WageWithOvertime = (HourlyRate * 40) + (HoursWorked - 40) * 1.5 * HourlyRate

#Check to see if they worked 40 hours or more and print their wage.

if HoursWorked > 40:
    print("Your weekly wage is",WageWithOvertime," with overtime!")
else:
    print("Your weekly wage is",wage,"!")

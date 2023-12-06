#Maahir Vohra
#10/24/21
#Program that computes the distance traveled and prints it out in string format
speed = int(input("What is the speed of the vehicle in MPH? "))
time = int(input("How many hours has it traveled? "))

print("\n%-10s %10s" %("Hour", "Distance Traveled"))
for i in range(1,speed + 1):
    print("%-10d %11d miles" %(i, i * speed))

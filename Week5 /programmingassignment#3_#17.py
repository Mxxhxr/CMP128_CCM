#Maahir Vohra
#10/13/2021
#Program that goes through the steps for troubleshooting a bad Wi-Fi connection

print("Hello, try rebooting the computer and trying to connect.")
answer = input("Did that fix the problem? ")
if answer == "no":
    print("Reboot the router and try to connect.")
    answer = input("Did that fix the problem? ")
    if answer == "no":
        print("Make sure the cables between the router and modem are plugged in firmly.")
        answer = input("Did that fix the problem? ")
        if answer == "no":
            print("Move the router to a new location and try to connect.")
            answer = input("Did that fix the problem? ")
            if answer == "no":
                print("Get a new router.")

print("Thank you.")



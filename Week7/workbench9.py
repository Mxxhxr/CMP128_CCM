#Maahir Vohra
#10/25/21
#Program that prompts the user to enter a number 1 - 100 and validates the input.

number = int(input("Please enter a number in the range 1 throught 100. "))

if number <= 1 and number >= 100:
    print("That is not within the given range! ")
else:
    print("Good")


#Is it glitching? Not sure why it wont work. I flipped the "<=" and ">=" around and I got the opposite of what I was supposed to get.
#What doesn't make sense is when I flip it back to normal, it doesn't work properly. Im not sure why.

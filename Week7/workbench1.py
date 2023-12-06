#Maahir Vohra
#10/25/21
#While loop that lets user enter a number and mulitplies it by 10 if its < 100.

while True:
    Digit = float(input("Enter a number: "))
    product = Digit * 10

    if product < 100:
        print(product)
        continue

    else:
        print(product, " is not less than 100!")
        break

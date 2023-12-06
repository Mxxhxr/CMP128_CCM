#Maahir Vohra
#10/27/21
#Dice roller

import random

count = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

for i in range(10):
    roll = random.randint(1, 6)
    print(f"You rolled a {roll}!")

    if roll == 1:
        count[1] += 1
    elif roll == 2:
        count[2] += 1
    elif roll == 3:
        count[3] += 1
    elif roll == 4:
        count[4] += 1
    elif roll == 5:
        count[5] += 1
    elif roll == 6:
        count[6] += 1

print(" ")

for i in range(1, 7):
    print(f"You rolled {count[i]} {i}s!")

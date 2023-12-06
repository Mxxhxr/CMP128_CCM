counter = 0
eventTotal = 0
anotherDiver = "Y"
while anotherDiver == "Y":
    counter += 1
    highest = 0
    lowest = 10
    total = 0
    for judge in range(1,6):
        score = float(input("Enter the score given by the judge#"+str(judge)+":"))
        while score < 0 or score > 10:
            print("Invalid score, please re enter. (Valid range: 0-10)")
            score = float(input("Enter the score given by the judge#"+str(judge)+":"))
        print("Judge " + str(judge) + " score is " + str(score))
        if score > highest:
            highest = score
        if score < lowest:
            lowest = score
        total = total + score
    print("Highest: ",highest)
    print("Lowest: ",lowest)
    difficulty = float(input("Enter the degree of difficulty "))
    while difficulty <1 or difficulty >1.67:
        print("Invalid difficulty, please re enter. (Valid range: 1.00-1.67)")
        difficulty = float(input("Enter the degree of difficulty "))
    print("Degree of difficulty is " +str(difficulty))


    adjustedTotal = ((total - highest - lowest) / 3) * difficulty
    print(adjustedTotal)
    eventTotal = eventTotal + adjustedTotal
    anotherDiver = input("Is there another diver? Please enter Y/N: ")
print("Number of diver " + str(counter))
averageScore = eventTotal / counter
print("Average score: ",averageScore)

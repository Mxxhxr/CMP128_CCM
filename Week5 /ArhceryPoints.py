#Maahir Vohra
#10/13/2021
#Making an archery target that "shoots" an arrow and prints out the points
#I remade the target so it would be easier for me to "shoot" the arrows at the target as well as calculate the score
import turtle, random, math


#Background Color
turtle.bgcolor("tan")

#Draw Target 

#Outer Black Circle
turtle.penup()
turtle.color("black")
turtle.fillcolor("black")
turtle.goto(0, -142)
turtle.begin_fill()
turtle.circle(142)
turtle.end_fill()
turtle.pendown()

#White Circle
turtle.penup()
turtle.color("white")
turtle.fillcolor("white")
turtle.goto(0, -140)
turtle.begin_fill()
turtle.circle(140)
turtle.end_fill()
turtle.pendown()

#Inner Black Circle
turtle.penup()
turtle.color("black")
turtle.fillcolor("black")
turtle.goto(0, -110)
turtle.begin_fill()
turtle.circle(110)
turtle.end_fill()
turtle.pendown()

#Blue Circle
turtle.penup()
turtle.color("blue")
turtle.fillcolor("blue")
turtle.goto(0, -80)
turtle.begin_fill()
turtle.circle(80)
turtle.end_fill()
turtle.pendown()

#Red Circle
turtle.penup()
turtle.color("red")
turtle.fillcolor("red")
turtle.goto(0, -50)
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()
turtle.pendown()

#Yellow Circle
turtle.penup()
turtle.color("yellow")
turtle.fillcolor("yellow")
turtle.goto(0, -20)
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()
turtle.pendown()


#Shooting Arrow
turtle.penup()
arrowX = random.randint(-140, 140)
arrowY = random.randint(-140, 140)
turtle.goto(arrowX, arrowY)
turtle.dot()
turtle.pendown()

#Calculate score 
score = 0

arrowHit = math.hypot(arrowX, arrowY)



if 0 <= arrowHit < 20:
  score += 5

if 21 <= arrowHit < 50:
  score += 4

if 51 <= arrowHit < 80:
  score += 3

if 81 <= arrowHit < 110:
  score += 2

if 111 <= arrowHit < 140:
  score += 1

print(score)

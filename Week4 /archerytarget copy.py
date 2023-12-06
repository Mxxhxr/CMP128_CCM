#Maahir Vohra
#9/27/2021
#Making an archery target

#Changing the background color
import turtle
turtle.bgcolor("tan")

#Making the black outline of the circle
turtle.color("black")
turtle.penup()
turtle.left(90)
turtle.forward(1)
turtle.right(90)
turtle.pendown()
turtle.circle(101)
turtle.penup()
turtle.left(90)
turtle.forward(1)
turtle.right(90)
turtle.pendown()

#Making the white circle
turtle.color("white")
turtle.begin_fill()
turtle.circle(100)
turtle.penup()
turtle.left(90)
turtle.forward(20)
turtle.right(90)
turtle.end_fill()

#Making the black circle
turtle.pendown()
turtle.color("black")
turtle.begin_fill()
turtle.circle(80)
turtle.end_fill()
turtle.penup()
turtle.left(90)
turtle.forward(20)
turtle.right(90)

#Making the blue circle
turtle.pendown()
turtle.color("blue")
turtle.begin_fill()
turtle.circle(60)
turtle.end_fill()
turtle.penup()
turtle.left(90)
turtle.forward(20)
turtle.right(90)

#Making the red circle
turtle.pendown()
turtle.color("red")
turtle.begin_fill()
turtle.circle(40)
turtle.end_fill()
turtle.penup()
turtle.left(90)
turtle.forward(20)
turtle.right(90)

#Making the yellow circle
turtle.pendown()
turtle.color("yellow")
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()

turtle.penup()
from random import randrange

pointX = randrange(0, 101)
pointY = randrange(0, 101)

turtle.goto(pointX, pointY)
turtle.dot()
turtle.pendown()
#Shooting the arrow
turtle.penup()
x = turtle.setx(0)
y = turtle.sety(0)
turtle.pendown()

#points
if pointX <= 100 and pointX >=0 and pointY <=100 and pointY >=0:
    print("1 point")
    
print(turtle.xcor(), turtle.ycor())



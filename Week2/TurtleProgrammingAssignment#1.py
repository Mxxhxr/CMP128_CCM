#Maahir Vohra
#9/27/2021
#Turtle Programming Assignment that makes three shapes.(triangle,octagon,square)

#Triangle
import turtle
turtle.color("orange")
turtle.begin_fill()
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.end_fill()

#Picking up the pen
turtle.penup()
turtle.forward(20)
turtle.left(60)
turtle.forward(30)
turtle.pendown()

#Octagon
turtle.color("red")
turtle.begin_fill()
turtle.forward(60)
turtle.right(45)
turtle.forward(60)
turtle.right(45)
turtle.forward(60)
turtle.right(45)
turtle.forward(60)
turtle.right(45)
turtle.forward(60)
turtle.right(45)
turtle.forward(60)
turtle.right(45)
turtle.forward(60)
turtle.right(45)
turtle.forward(60)
turtle.right(45)
turtle.forward(60)
turtle.end_fill()

#Picking up the pen
turtle.penup()
turtle.forward(120)
turtle.left(90)
turtle.forward(85)
turtle.pendown()

#Square
turtle.color("yellow")
turtle.begin_fill()
turtle.left(45)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.end_fill()


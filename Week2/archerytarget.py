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

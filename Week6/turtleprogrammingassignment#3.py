#Maahir Vohra
#10/24/21
#Turtle program that writes numbers 1-15 with a line representing it after each number.
import turtle
turtle.color("black")
for lines in range(15):
    turtle.write(1+lines)
    turtle.right(90)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()
    turtle.forward(150)
    turtle.penup()
    turtle.left(180)
    turtle.forward(160)
    turtle.right(90)
    turtle.forward(20)
    turtle.pendown()
    
    


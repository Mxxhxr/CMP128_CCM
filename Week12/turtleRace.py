
#Maahir Vohra
#10/24/21
#Turtle program that writes numbers 1-15 with a line representing it after each number.
import turtle
import random
turtle.speed(15)
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

#New
blue = turtle.Turtle()
blue.penup()
blue.setx(-20)
blue.sety(-40)
blue.pendown()
blue.shape("turtle")
blue.color("blue")

red = turtle.Turtle()
red.penup()
red.setx(-20)
red.sety(-70)
red.pendown()
red.shape("turtle")
red.color("red")

yellow = turtle.Turtle()
yellow.penup()
yellow.setx(-20)
yellow.sety(-100)
yellow.pendown()
yellow.shape("turtle")
yellow.color("yellow")

green = turtle.Turtle()
green.penup()
green.setx(-20)
green.sety(-140)
green.pendown()
green.shape("turtle")
green.color("green")

for x in range(100):
    green.forward(random.randint(1,5))
    red.forward(random.randint(1,5))
    yellow.forward(random.randint(1,5))
    blue.forward(random.randint(1,5))

#end=turtle.xcor()
#while green.xcor() < end and red.xcor() < end and yellow.xcor() < end and blue.xcor() < end:
    #green.forward(random.randint(1,5))
    #red.forward(random.randint(1,5))
    #yellow.forward(random.randint(1,5))
    #blue.forward(random.randint(1,5))

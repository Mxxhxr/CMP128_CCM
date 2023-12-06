import turtle
import random #used to gen a random number
print(turtle.xcor(), turtle.ycor())
turtle.circle(50)
print(turtle.xcor(), turtle.ycor())
turtle.penup()
turtle.setx(100)
turtle.sety(50)
turtle.pendown()
turtle.forward(1)
x = random.randint(-200,0)
y = random.randint(0,200)
turtle.setx(x)
turtle.sety(y)
turtle.forward(20)
turtle.penup()
turtle.forward(100)
turtle.pendown()
turtle.dot(4, "red")
if x > 100:
    print("3 points")
    

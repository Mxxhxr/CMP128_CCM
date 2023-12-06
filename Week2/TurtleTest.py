import turtle #this line will allow us to use turtle graphics
turtle.color("blue") #this will change the color of the pen
turtle.begin_fill() #this will fill the shape
turtle.forward(100) #this will move it in the direction you choose
turtle.forward(50)
turtle.right(90) #this will change the direction 
turtle.forward(75)
turtle.right(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(75)
turtle.end_fill() #need to put this to end fill
turtle.penup() #this will pick up the pen
turtle.forward(30)
turtle.pendown() #this puts the pen down
turtle.forward(150)
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()

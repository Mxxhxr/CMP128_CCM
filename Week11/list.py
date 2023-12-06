import turtle

def drawBar(t,height,linecolor,fillcolor):
    t.color(linecolor)
    t.fillcolor(fillcolor)
    t.penup()
    t.sety(-20)
    t.pendown()
    t.penup()
    t.sety(0)
    t.pendown()
    t.begin_fill()
    t.left(90)               
    t.forward(height)
    t.write(str(height))
    t.right(90)
    t.forward(40)            
    t.right(90)
    t.forward(height)
    t.left(90)               
    t.end_fill()
    t.penup()
    t.forward(3)
    t.pendown()

values = []

for x in range(8):
    values.append(int(input("Enter a number between 0 and 300")))
    
for num in values:
    drawBar(turtle,values[counter],
    drawBar(turtle, num, "red", "black"

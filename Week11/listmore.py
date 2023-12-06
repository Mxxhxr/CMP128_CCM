import turtle

def drawBar(t,height,linecolor,fillcolor,label):
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
    t.sety(-30)
    x = t.cor()
    t.pendown()
    t.setx(x-40)
    t.write(label)
    t.penup
    t.sety(0)
    t.setx(x+40)
    t.forward(3)
    t.pendown()
def doaverage(thelist, avglist):
    total = 0
    for num in range(1,5):
        total += thelist[num]
    average = total/4
    avglist.append(average)
    
    
list1 = ["A", 44.0, 38.9, 30.8, 29.4]
list2 = ["B", 25.6, 30.2, 23.2, 20.1]
list3 = ["C", 10.0, 15.4, 21.6, 12.9]
#empty lists
items = []
averages = []

items.append(list1[0])
items.append(list2[0])
items.append(list3[0])

doaverage(list1, averages)
doaverage(list2, averages)
doaverage(list3, averages)


print(items)
print(averages)

#for x in averages:
for x in range(3):
    drawBar(turtle,x,"black","purple","Label",items[x])

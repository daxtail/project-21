import turtle

turtle.pensize(4)
turtle.pencolor("OliveDrab")
turtle.setpos(-50, 0)

def repeated_tasks(c,s,a):
    turtle.fillcolor(c)
    turtle.begin_fill()
    for i in [0, 1, 2]:
        turtle.forward(s)
        turtle.left(a)
        
        
    turtle.end_fill()
repeated_tasks("Olive",175,120)

turtle.forward(25)
turtle.right(90)
repeated_tasks("PeachPuff",125,90)


#The below steps till the end are for drawing a circle(window)
turtle.penup()
turtle.forward(62.5)
turtle.left(90)
turtle.forward(25)
turtle.right(90)



turtle.fillcolor("black")
turtle.begin_fill()
turtle.circle(15)
turtle.end_fill()
turtle.pendown()


turtle.hideturtle()

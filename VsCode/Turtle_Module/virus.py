import turtle as t 

tim = t.Turtle()
tim.speed('fastest')
t.pencolor("green")
screen = t.Screen()
screen.bgcolor("black")

a = 0
b = 0
t.hideturtle()
t.penup()
t.goto(0,200)
t.pendown()

while(True):
    t.forward(a)
    t.right(b)
    a+=3
    b+=1

    if b == 210:
        break
    

screen.exitonclick()
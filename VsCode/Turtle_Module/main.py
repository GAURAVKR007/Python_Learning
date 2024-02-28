import turtle as turtle
import random

t = turtle.Turtle()
turtle.colormode(255)
# colors = ['gainsboro','dim gray','royal blue','light blue','powder blue','azure','turquoise','dark orange','firebrick','linen','dark violet']

t.shape("classic")
# t.color("orange")

# t.forward(100)
# t.right(90)

# make a Square 

# for i in range(4):
#     t.forward(100)
#     t.right(90)



# draw a Dashed Line

# for i in range(15):
#     t.forward(10)
#     t.penup()
#     t.forward(10)
#     t.pendown()      

# Draw Shapes

# full_angle = 360
# for i in range(3,11):
#     angle = full_angle / i
#     for j in range(i):
#         t.forward(100)
#         t.right(angle)

# Random color

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    rgb = (r,g,b)

    return rgb


# Random Walk

# directions = [0,90,180,270]
# t.width(15)
# t.speed("fastest")
# for i in range(200):
#     t.color(random_color())
#     t.forward(30)
#     t.setheading(random.choice(directions))


# Draw a SPirograph
# t.speed("fastest")
# def draw_sPirograph(size_of_gap):
#     for i in range(int(360/size_of_gap)):
#         t.color(random_color())
#         t.circle(150)
#         current_heading = t.heading()
#         t.setheading(current_heading + size_of_gap)

# draw_sPirograph(5)





screen = turtle.Screen()
screen.exitonclick()
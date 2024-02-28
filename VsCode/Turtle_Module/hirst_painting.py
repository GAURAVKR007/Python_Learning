import colorgram
import turtle as t
import random
t.colormode(255)
tim = t.Turtle()

# Extract 10 colors from an image.
# colors = colorgram.extract('color_img.jpg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b

#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82)]


tim.speed("fastest")
tim.hideturtle()
tim.setheading(225)
tim.penup()
tim.forward(250)
tim.pendown()
tim.setheading(0)
num_of_dots = 100
for i in range(1,num_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.forward(50)
    tim.pendown()

    if i % 10 == 0:
        tim.penup()
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
        tim.pendown()


screen = t.Screen()
screen.exitonclick()
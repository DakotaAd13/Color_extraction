import colorgram
import turtle as turtle_mod
import random

colors = colorgram.extract('image.jpg', 30)

rgb_colors = []

johny_rango = turtle_mod.Turtle()
johny_rango.penup()
johny_rango.hideturtle()
johny_rango.speed("fastest")



turtle_mod.colormode(255)

turtle_mod.bgpic("ricky.gif")

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    #touple
    new_color = (r, g, b)
    rgb_colors.append(new_color)


color_list = [(253, 251, 247), (253, 248, 252), (235, 252, 243), (198, 13, 32), (248, 236, 25), (40, 76, 188),
              (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17),
              (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62),
              (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238),
              (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51)]

johny_rango.setheading(225)
johny_rango.forward(300)
johny_rango.setheading(0)
number_of_dots = 90

for dot_count in range(1, number_of_dots +1):

    johny_rango.dot(30, random.choice(color_list))
    johny_rango.fd(50)

    if dot_count % 10 == 0:
        johny_rango.setheading(90)
        johny_rango.fd(50)
        johny_rango.setheading(180)
        johny_rango.fd(500)
        johny_rango.setheading(0)

screen = turtle_mod.Screen()
screen.exitonclick()










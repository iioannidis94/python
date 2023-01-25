from turtle import Turtle, Screen, colormode
from random import choice, randint
tim = Turtle()

colors = ["red", "blue", "green", "yellow", "violet", "cyan", "black", "orange", "purple", "brown", "white smoke",
           "dark slate gray", "maroon", "thistle", "pale violet red", "orange red", "green yellow", "honeydew",
           "dark khaki", "gold", "rosy brown", "midnight blue", "light sky blue", "yellow green", "light slate gray",
           "mint cream", "medium turquoise", "khaki", "royal blue", "light goldenrod yellow", "tan", "peach puff", ]
tim.shape("turtle")


# # paint a square
# for _ in range(4):
#     tim.fd(100)
#     tim.right(90)

# import heroes
# print(heroes.gen())

# # paint a not straight line
# for _ in range(15):
#     tim.fd(10)
#     tim.pu()
#     tim.fd(10)
#     tim.pd()
# # multiple triangle - square - polygon generate
# z = 3
# y = 3
# for _ in range(7):
#     colors = ["red", "blue", "green", "yellow", "violet", "cyan", "black", "orange", "purple", "brown", "white smoke",
#           "dark slate gray", "maroon", "thistle", "pale violet red", "orange red", "green yellow", "honeydew",
#           "dark khaki", "gold", "rosy brown", "midnight blue", "light sky blue", "yellow green", "light slate gray",
#           "mint cream", "medium turquoise", "khaki", "royal blue", "light goldenrod yellow", "tan", "peach puff", ]
#     TheColor = choice(colors)
#     tim.color(TheColor)
#     turn = 360
#     turn /= z
#     for x in range(y):
#         tim.fd(100)
#         tim.right(turn)
#     y += 1
#     z += 1



# # simple same exampled
# colors = ["red", "blue", "green", "yellow", "violet", "cyan", "black", "orange", "purple", "brown", "white smoke",
#           "dark slate gray", "maroon", "thistle", "pale violet red", "orange red", "green yellow", "honeydew",
#           "dark khaki", "gold", "rosy brown", "midnight blue", "light sky blue", "yellow green", "light slate gray",
#           "mint cream", "medium turquoise", "khaki", "royal blue", "light goldenrod yellow", "tan", "peach puff", ]
# #
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.fd(100)
#         tim.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     tim.color(choice(colors))
#     draw_shape(shape_side_n)

# # random color walk + tuple
# colormode(255)
#
#
# def random_color():
#     r = randint(0, 255)
#     g = randint(0, 255)
#     b = randint(0, 255)
#     my_tuple = (r, g, b)
#     return my_tuple
#
#
# def walk():
#     direction = [0, 90, 180, 270]
#     tim.setheading(choice(direction))
#
#
# tim.speed(0)
# tim.width(10)
# for _ in range(800):
#     walk()
#     tim.fd(20)
#     tim.pencolor(random_color())
#     tim.color(choice(colors))

# # creating a spiralgraph circle
colormode(255)


def random_color():
     r = randint(0, 255)
     g = randint(0, 255)
     b = randint(0, 255)
     my_tuple = (r, g, b)
     return my_tuple


tim.speed("fastest")


def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        tim.setheading(tim.heading() + size_of_gap)
        tim.color(random_color())
        tim.color(choice(colors))
        tim.circle(100)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()

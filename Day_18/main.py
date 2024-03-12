from turtle import  Screen
import turtle as t
import random as r

tim = t.Turtle()
tim.shape("turtle")
tim.color("blue")

t.colormode(255)

# for i in range(4):
#     tim.left(90)
#     tim.forward(100)

#____________________________________________________________

# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

#____________________________________________________________


# def draw_shape(num_sides):
#     angle = 360 / num_sides 
#     for i in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)

# colors = ["blue", "green", "yellow", "red", "orange", "pink", "darkgreen","black", "gray","lightblue" ]

# for shape_side_n in range(3,11):
#     tim.color(r.choice(colors))
#     draw_shape(shape_side_n)

#____________________________________________________________

# colors = ["blue", "green", "yellow", "red", "orange", "pink", "darkgreen","black", "gray","lightblue" ]
# directions = [0,90,180,270]
# tim.pensize(15)

# for i in range(200):
#     tim.color(r.choice(colors))
#     tim.forward(30)
#     tim.setheading(r.choice(directions))

#____________________________________________________________


# def random_color():
#     r_value = r.randint(0, 255)
#     g_value = r.randint(0, 255)
#     b_value = r.randint(0, 255)
#     random_color = (r_value, g_value, b_value)
#     return random_color

# directions = [0,90,180,270]
# tim.pensize(15)
# tim.speed("fastest")

# for i in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(r.choice(directions))



screen = Screen()
screen.exitonclick()
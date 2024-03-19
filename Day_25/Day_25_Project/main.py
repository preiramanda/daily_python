import turtle
import pandas as pd

IMAGE = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S. States Game")
#Loading image
screen.addshape(IMAGE)
turtle.shape(IMAGE)

data = pd.read_csv("50_states.csv")
states = data["state"].to_list()
#do not forget to turn the series into a list

def get_mouse_click_coor(x,y):
    print(x,y)

turtle.onscreenclick(get_mouse_click_coor)

answer = screen.textinput(title="Guess the state",prompt="Insert the name of a State").title()

game = True
count_states = 0

while game:
    if answer == "Exit":
        break
    if answer in states:
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        location = data[data.state == answer]
        t.goto(int(location["x"]), int(location["y"]))
        t.write(location.state.item())
        #item removes the series information
        count_states += 1
        answer = screen.textinput(title=f"{count_states}/50",prompt="Insert the name of a State").title()
    else:
        answer = screen.textinput(title=f"{count_states}/50",prompt="Insert the name of a State").title()

    if count_states > 50:
        game = False



#replaces the exitonclick
turtle.mainloop()



from turtle import Turtle, Screen
import random as r

race = False
screen = Screen()
screen.setup(width=500,height=400)

colors =['red','orange', 'yellow', 'green', 'blue', 'purple']

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)

while True:
    if user_bet not in colors:
        user_bet = screen.textinput(title="Must be one of the rainbow colors!", prompt="Which turtle will win the race? Enter a color: ")
    else:
        race = True
        break

turtle_list = [] 
y = -80
for i in colors:
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(i)
    turtle.goto(x=-220,y=y) 
    y += 30
    turtle_list.append(turtle) 

while race:
    for i in turtle_list:
        
        if i.xcor()>230:
            race = False
            winner = i.pencolor()
            if winner == user_bet:
                screen.title(f"You win! Congrats {winner}!")
            else:
                screen.title(f"You lose! The winner was {winner}!")


        rand_distance = r.randint(0,10)
        i.forward(rand_distance)

screen.exitonclick()




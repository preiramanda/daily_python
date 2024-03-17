import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

texts = Turtle()
texts.hideturtle()
texts.penup()
player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.go_up, "Up")

score = 0
game = True
while game:
    texts.goto(-260, 280)
    texts.write(f"Score: {score}", align= "center",font= ("Courier", 12, "normal"))
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

#detect colision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game = False
            texts.goto(0, 0)
            texts.write("Game Over!", align= "center",font= ("Courier", 20, "normal"))

    if player.at_finish_line():
        player.restart_turtle()
        car_manager.level_up()
        texts.clear()
        score += 1

screen.exitonclick()
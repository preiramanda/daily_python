from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 14,"normal")

class Texts(Turtle):
    
    def __init__(self):
        super().__init__()
        
        self.score = 0
        self.penup()
        self.goto(0,-300)
        self.hideturtle()
        self.update_score()
    
    def mark(self):
        self.color("black")
        self.goto(230,-300)
        self.write(f"Made by Amanda Coper", align="center", font=("Courier", 8,"normal"))

    def update_score(self):
        self.write(f" Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.color("black")
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)



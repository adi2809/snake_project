from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 24,"normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.color("white")

        self.hideturtle()
    def update(self):
        self.write(f"score : {self.score}", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score+=1
        self.clear()
        self.update()
    def game_over(self):
        self.clear()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)



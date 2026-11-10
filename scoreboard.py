from turtle import Turtle
import os
import sys

#
def highscore_path():
    if getattr(sys, "frozen", False):
        base = os.path.join(os.environ["APPDATA"], "TinySnake")
        os.makedirs(base, exist_ok=True)
    else:
        base = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base, "Your_Highscore.txt")
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as data_highscore:
            data_highscore.write("0")
    return path

ALIGNMENT = "center"
ALIGNMENT1 = "left"
FONT = ('Courier', 14, 'bold')
FONT1 = ('Courier', 8, 'normal')
Title = "My tiny snake game"
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open(highscore_path(), encoding="utf-8") as data_highscore:
            self.highscore = int(data_highscore.read() or 0)
        self.color("white")
        self.penup()
        self.update_board()
        self.hideturtle()


    def update_board(self):
        self.clear()
        self.goto(0, 275)
        self.pencolor("white")
        self.write(f"Score: {self.score} High Score: {self.highscore}", move=True, align=ALIGNMENT, font=FONT)
        self.goto(-100, 265)
        self.pencolor("purple")
        self.write(f"You play: {Title}", move=True, align=ALIGNMENT1, font=FONT1)

    def increase_score(self):
        self.update_board()
        self.score += 1
        #self.write(f"Score: {self.score}", move=True, align=ALIGNMENT, font= FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open(highscore_path(), "w", encoding="utf-8") as data_highscore:
                data_highscore.write(str(self.highscore))
        self.score = 0
        self.update_board()







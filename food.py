from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(stretch_len = 0.75, stretch_wid = 0.75)
        self.color("green")
        self.speed("fastest")
        self.penup()
        self.refresh()


    def refresh(self):
        rand_x = random.randint(-275, 275)
        rand_y = random.randint(-275, 275)
        self.goto(rand_x, rand_y)



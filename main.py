from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My tiny Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()

#set PC keys to play with
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

#As long as the game is running:
Playing = True

while Playing:
    screen.update()
    time.sleep(0.11)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 17:
        print("nom nom nom")
        food.refresh()
        scoreboard.increase_score()
        snake.grow()
     #Detect collision with wall
    if snake.head.xcor() < -285 or snake.head.xcor() > 285 or snake.head.ycor() < -285 or snake.head.ycor() > 285:
        scoreboard.reset()
        snake.reset()

    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
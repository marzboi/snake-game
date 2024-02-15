from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()

screen.onkeypress(snake.up, 'w')
screen.onkeypress(snake.down, 's')
screen.onkeypress(snake.right, 'd')
screen.onkeypress(snake.left, 'a')


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # detect collision
    if snake.head.distance(food) < 15:
        food.refresh()

screen.exitonclick()

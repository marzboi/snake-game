from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

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
        score.increase_score()
        snake.extend((snake.snake[len(snake.snake) - 1].xcor(), snake.snake[len(snake.snake) - 1].ycor()))

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    # detects collision with tail
    for part in snake.snake:
        if part == snake.head:
            pass
        elif snake.head.distance(part) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()

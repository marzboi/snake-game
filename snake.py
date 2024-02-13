from turtle import Turtle
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.snake = []
        self.initial_x = 0
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for _ in range(3):
            snake_part = Turtle('square')
            snake_part.penup()
            snake_part.color('white')
            snake_part.goto(x=self.initial_x, y=0)
            self.initial_x -= 20
            self.snake.append(snake_part)

    def move(self):
        for part in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[part - 1].xcor()
            new_y = self.snake[part - 1].ycor()
            self.snake[part].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if not self.head.heading() == 270:
            self.head.seth(90)

    def down(self):
        if not self.head.heading() == 90:
            self.head.seth(270)

    def right(self):
        if not self.head.heading() == 180:
            self.head.seth(0)

    def left(self):
        if not self.head.heading() == 0:
            self.head.seth(180)

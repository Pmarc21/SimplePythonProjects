# Simple Pong in Python 3 for Beginners
# By @TokyoEdTech

import turtle
import os
import random

wn = turtle.Screen()
wn.title("Snake")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score = 0

# Snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("white")
snake.shapesize(stretch_wid=5, stretch_len=1)
snake.penup()
snake.goto(0, 0)

# Ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(260, 0)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0", align="center", font=("Courier", 24, "normal"))


# Functions
def snake_up():
    y = snake.ycor()
    y += 20
    snake.sety(y)


def snake_down():
    y = snake.ycor()
    y -= 20
    snake.sety(y)


def snake_left():
    x = snake.xcor()
    x -= 20
    snake.setx(x)


def snake_right():
    x = snake.xcor()
    x += 20
    snake.setx(x)
    snake.tilt(90)


def new_position_ball():
    new_x = random.randint(-390, 390)
    new_y = random.randint(-290, 390)


# Keyboard bindings
wn.listen()
wn.onkeypress(snake_up, "w")
wn.onkeypress(snake_down, "s")
wn.onkeypress(snake_left, "a")
wn.onkeypress(snake_right, "d")

# Main game loop
while True:
    wn.update()

    # Moving the ball

    # Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Left and right


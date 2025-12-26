"""
This is the main entry point for the Snake game.
It brings together all the different modules (snake, food, scoreboard)
and runs the main game loop.
"""

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# --- Screen Setup ---
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Turns off automatic screen updates

# --- Game Objects Initialization ---
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# --- Keyboard Bindings ---
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# --- Main Game Loop ---
game_is_on = True
while game_is_on:
    screen.update()  # Manually update the screen
    time.sleep(0.1)  # Control the game speed
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    # Slicing the list to exclude the head
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

# --- Exit on Click ---
screen.exitonclick()

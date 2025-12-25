"""
A turtle race game where a user can bet on which of the seven rainbow-colored turtles will win.
"""
from turtle import Turtle, Screen
import random

# --- Screen Setup ---
# Initialize the screen, set its dimensions, and background color.
screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("black")

# --- User Bet ---
# Prompt the user to enter their bet on which turtle will win.
user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win the race? Enter a color from the rainbow: "
)


# --- Turtle Setup ---
# Define the colors and starting y-positions for the turtles.
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
y_positions = [-70, -40, -10, 20, 50, 80, 100]
all_turtles = []

# Create a turtle for each color and move it to its starting position on the left edge of the screen.
for turtle_index in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()  # Lift the pen to avoid drawing a line when moving to the start.
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

# --- Race Logic ---
is_race_on = False
if user_bet:
    is_race_on = True

# The main loop for the race. It continues as long as the race is on.
while is_race_on:
    for turtle in all_turtles:
        # Check if a turtle has crossed the finish line (the right edge of the screen).
        if turtle.xcor() > 230:
            is_race_on = False  # Stop the race.
            winning_color = turtle.pencolor()

            # --- Announce Winner ---
            # Compare the winning turtle's color with the user's bet.
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            break  # Exit the for-loop as soon as a winner is found.

        # Move the turtle forward by a random distance.
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

# --- Exit ---
# Keep the screen open until it's clicked.
screen.exitonclick()


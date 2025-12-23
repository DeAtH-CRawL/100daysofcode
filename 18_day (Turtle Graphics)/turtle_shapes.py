# Import necessary libraries
import turtle as tim
import random

# Initialize the screen and set its background color
screen = tim.Screen()
screen.bgcolor("black")

# A list of colors for the shapes
colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "white", "grey", "cyan", "magenta", "lime", "maroon", "navy", "olive", "teal"]

# Set the turtle's shape
tim.shape("turtle")

# Set the initial pen color
tim.pencolor("pink")

# Set the turtle's speed to a very high value
tim.speed(10000000)

# Position the turtle to the starting point
tim.penup()
tim.goto(-200,300)
tim.pendown()

# Loop to draw shapes with an increasing number of sides (from triangle to nonagon)
for num_of_sides in range(3,10):
    # Choose a random color for each shape
    tim.color(random.choice(colors))
    # Calculate the angle for each side of the shape
    angle = 360/num_of_sides
    # Loop to draw each side of the shape
    for i in range(num_of_sides):
        tim.forward(100)
        tim.right(angle)

# Keep the window open until it is clicked
screen.exitonclick()
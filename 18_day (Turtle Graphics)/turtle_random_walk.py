# Import necessary libraries
import turtle as tim
import random

# Initialize the screen and set its background color
screen = tim.Screen()
screen.bgcolor("black")

# Set the screen size
tim.screensize(1000, 1000)

# A list of colors for the turtle's path
colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "white", "grey", "black", "cyan", "magenta", "lime", "maroon", "navy", "olive", "teal"]
# A list of possible step sizes for the turtle
steps = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Set the turtle's shape and pen size
tim.shape("turtle")
tim.pensize(15)

# A list of possible headings (directions) for the turtle
directions = [0, 90, 180, 270, 360, 450, 540, 630, 720, 810, 900]

# Set the initial pen color and speed
tim.pencolor("pink")
tim.speed("fastest")

# Main loop to create the random walk
for _ in range(300):
    # Choose a random color for the pen
    tim.color(random.choice(colors))
    # Move the turtle forward by a random step size
    tim.forward(random.choice(steps))
    # Set the turtle's heading to a random direction
    tim.setheading(random.choice(directions))
    
# Keep the window open until it is clicked
screen.exitonclick()

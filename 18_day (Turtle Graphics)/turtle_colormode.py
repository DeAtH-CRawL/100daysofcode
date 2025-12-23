# Import necessary libraries
import turtle as tim
import random

# Set the color mode to 255 to allow for RGB color values
tim.colormode(255)
# Set the turtle's speed to the fastest setting
tim.speed("fastest")

# Function to generate a random RGB color
def random_color():
    """Generates a random RGB color tuple."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

# Function to draw a spirograph
def draw_spirograph(size_of_gap):
    """Draws a spirograph pattern by drawing circles at different angles."""
    # Loop to draw circles and create the spirograph effect
    for _ in range(int(360 / size_of_gap)):
        # Set the turtle's color to a new random color for each circle
        tim.color(random_color())
        # Draw a circle with a radius of 100
        tim.circle(100)
        # Change the turtle's heading to create the spirograph pattern
        tim.setheading(tim.heading() + size_of_gap)

# Call the function to draw the spirograph with a small gap between circles
draw_spirograph(1)

# Get the screen object and set it to exit on click
screen = tim.Screen()
screen.exitonclick()
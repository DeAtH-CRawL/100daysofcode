# Import necessary libraries
import turtle as turtle_module
import random

# Set the color mode to 255 to allow for RGB color values
turtle_module.colormode(255)

# Initialize the turtle and screen objects
tim = turtle_module.Turtle()
screen = turtle_module.Screen()

# Set the background color of the screen to black
screen.bgcolor("black")

# Set the turtle's shape and speed
tim.shape("turtle")
tim.speed("fastest")

# Lift the pen to prevent drawing while repositioning
tim.penup()
# Hide the turtle icon for a cleaner look
tim.hideturtle()

# Position the turtle to the starting point of the drawing
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

# Define the total number of dots to be drawn
numer_of_dots = 100

# A list of RGB colors to be used for the dots
color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

# Loop to draw the grid of dots
for dot_count in range(1, numer_of_dots + 1):
    # Create a dot with a random color from the list
    tim.dot(20, random.choice(color_list))
    # Move the turtle forward to the next dot position
    tim.forward(50)
    
    # Check if a row of 10 dots is complete
    if dot_count % 10 == 0:
        # Move the turtle up to the next row
        tim.setheading(90)
        tim.forward(50)
        # Move the turtle back to the starting horizontal position
        tim.setheading(180)
        tim.forward(500)
        # Reset the turtle's heading for the new row
        tim.setheading(0)
        
# Keep the window open until it is clicked
screen.exitonclick()
"""
This module defines the Food class for the Snake game.
The Food class is responsible for creating and positioning the food pellets.
"""

from turtle import Turtle
import random


class Food(Turtle):
    """A class to represent the food in the game. Inherits from Turtle."""

    def __init__(self):
        """Initializes the food object with its shape, color, and initial position."""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Make the food smaller
        self.color("blue")
        self.speed("fastest")  # So the food appears instantly
        self.refresh()

    def refresh(self): 
        """Moves the food to a new random position on the screen."""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

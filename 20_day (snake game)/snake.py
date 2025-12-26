"""
This module defines the Snake class for the classic Snake game.
It handles the snake's creation, movement, and growth.
"""

from turtle import Turtle

# Constants for the snake's initial setup and movement
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """A class to represent the snake in the game."""

    def __init__(self):
        """Initializes the snake's body and sets its head."""
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Creates the initial snake body from the starting positions."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """
        Adds a new segment to the snake at a given position.

        Args:
            position (tuple): A tuple (x, y) representing the position for the new segment.
        """
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """Adds a new segment to the end of the snake's tail."""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Moves the snake forward by one step."""
        # The segments follow the head by moving to the position of the segment in front of them
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Changes the snake's heading to up, if not currently moving down."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Changes the snake's heading to down, if not currently moving up."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Changes the snake's heading to left, if not currently moving right."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Changes the snake's heading to right, if not currently moving left."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        """Resets the snake to its initial state after a collision."""
        # Move old segments off-screen before clearing
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

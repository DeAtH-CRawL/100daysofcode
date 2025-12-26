"""
This module defines the Scoreboard class for the Snake game.
It handles displaying the score and the high score, and also
reading/writing the high score from a file.
"""

from turtle import Turtle

# Constants for scoreboard alignment and font
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """A class to represent the scoreboard. Inherits from Turtle."""

    def __init__(self):
        """Initializes the scoreboard, loads the high score, and displays it."""
        super().__init__()
        self.score = 0
        # Use a relative path for the data file
        with open(r"C:\Users\Jeeya Jhawar\OneDrive\Desktop\100daysofcode\20_day (snake game)\data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clears the old score and writes the new score."""
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        """Resets the score and updates the high score if the current score is higher."""
        if self.score > self.high_score:
            self.high_score = self.score
            # Write the new high score to the data file
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        """Increases the score by one and updates the scoreboard display."""
        self.score += 1
        self.update_scoreboard()

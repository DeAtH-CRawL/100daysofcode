"""
This module defines the Scoreboard class for the Snake game.
It handles displaying the score.
"""
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
INSTRUCTION_FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    """A class to represent the scoreboard."""

    def __init__(self):
        """Initializes the scoreboard and displays it."""
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clears the old score and writes the new score."""
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increases the score by one and updates the scoreboard display."""
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        """Resets the score to 0 and prepares for a new game."""
        self.score = 0
        self.goto(0, 270)  # Reposition turtle to the top for the score
        self.update_scoreboard()

    def game_over(self):
        """Displays 'GAME OVER' and restart instructions."""
        self.goto(0, 20)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        self.goto(0, -20)
        self.write("Press Space to Play Again", align=ALIGNMENT, font=INSTRUCTION_FONT)
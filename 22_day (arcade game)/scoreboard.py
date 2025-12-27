from turtle import Turtle

class Scoreboard(Turtle):
    """
    The Scoreboard class is responsible for displaying the score, the center divider,
    and game over messages. It inherits from the Turtle class.
    """
    def __init__(self):
        """Initializes a new Scoreboard object."""
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.draw_divider()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clears the previous score and redraws the divider and the updated scores."""
        self.clear()
        self.draw_divider()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        """Increases the left player's score and updates the scoreboard."""
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """Increases the right player's score and updates the scoreboard."""
        self.r_score += 1
        self.update_scoreboard()

    def draw_divider(self):
        """Draws a dashed line in the center of the screen."""
        self.goto(0, 300)
        self.setheading(270)
        for _ in range(15):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
        self.hideturtle()

    def game_over(self):
        """
        Displays the 'GAME OVER' message, the winner, and instructions to restart or quit.
        """
        self.goto(0, 50)
        self.write("GAME OVER", align="center", font=("Courier", 40, "normal"))
        self.goto(0, 0)
        if self.l_score > self.r_score:
            self.write("Left Player Wins!", align="center", font=("Courier", 20, "normal"))
        else:
            self.write("Right Player Wins!", align="center", font=("Courier", 20, "normal"))
        self.goto(0, -50)
        self.write("Press 'r' to restart or 'space' to quit.", align="center", font=("Courier", 15, "normal"))

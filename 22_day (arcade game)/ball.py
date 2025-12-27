from turtle import Turtle

class Ball(Turtle):
    """
    The Ball class represents the ball in the Pong game.
    It inherits from the Turtle class and is responsible for its own
    movement, bouncing, and position resetting.
    """
    def __init__(self):
        """Initializes a new Ball object."""
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """Moves the ball by updating its x and y coordinates."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Reverses the ball's y-direction to simulate a bounce off a horizontal surface."""
        self.y_move *= -1

    def bounce_x(self):
        """
        Reverses the ball's x-direction to simulate a bounce off a vertical surface (paddle).
        Also increases the ball's speed slightly upon collision.
        """
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """
        Resets the ball to the center of the screen and reverses its horizontal direction
        after a player scores.
        """
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()

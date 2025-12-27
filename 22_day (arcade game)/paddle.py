from turtle import Turtle

class Paddle(Turtle):
    """
    The Paddle class represents a paddle in the Pong game.
    It inherits from the Turtle class and is responsible for creating the paddle
    and controlling its movement.
    """
    def __init__(self, position):
        """
        Initializes a new Paddle object.
        :param position: A tuple (x, y) representing the initial position of the paddle.
        """
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        """Moves the paddle up by 20 pixels."""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """Moves the paddle down by 20 pixels."""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

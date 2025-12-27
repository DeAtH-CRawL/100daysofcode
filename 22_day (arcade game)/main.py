# main.py
# This script runs the Pong game by coordinating the screen, paddles, ball, and scoreboard.

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# --- Constants ---
WINNING_SCORE = 5

# --- Game Loop ---
def game_loop(screen, r_paddle, l_paddle, ball, scoreboard):
    """
    The main loop for a single round of Pong.
    Handles ball movement, collision detection, and scoring.
    """
    game_is_on = True
    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        # Detect collision with top and bottom walls
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        # Detect collision with paddles
        if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or \
           (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
            ball.bounce_x()

        # Detect when right paddle misses
        if ball.xcor() > 380:
            ball.reset_position()
            scoreboard.l_point()

        # Detect when left paddle misses
        if ball.xcor() < -380:
            ball.reset_position()
            scoreboard.r_point()

        # Check for a winner
        if scoreboard.l_score >= WINNING_SCORE or scoreboard.r_score >= WINNING_SCORE:
            game_is_on = False
            scoreboard.game_over()

# --- Main Game Setup ---
def main():
    """
    Sets up the game screen and all game components, and binds user input.
    """
    # --- Screen Setup ---
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.title("Pong")
    screen.tracer(0)  # Turn off automatic screen updates

    # --- Game Objects ---
    r_paddle = Paddle((350, 0))
    l_paddle = Paddle((-350, 0))
    ball = Ball()
    scoreboard = Scoreboard()

    # --- Event Listeners ---
    screen.listen()
    screen.onkeypress(r_paddle.go_up, "Up")
    screen.onkeypress(r_paddle.go_down, "Down")
    screen.onkeypress(l_paddle.go_up, "w")
    screen.onkeypress(l_paddle.go_down, "s")

    def restart_game():
        """Resets the game to its initial state for a new round."""
        scoreboard.l_score = 0
        scoreboard.r_score = 0
        scoreboard.update_scoreboard()
        ball.reset_position()
        screen.onkeypress(None, "r")  # Disable 'r' until the current game is over
        game_loop(screen, r_paddle, l_paddle, ball, scoreboard)
        screen.onkeypress(restart_game, "r") # Re-enable 'r' for the next game over

    def quit_game():
        """Exits the game."""
        screen.bye()

    screen.onkeypress(restart_game, "r")
    screen.onkeypress(quit_game, "space")

    # --- Initial Start Message ---
    scoreboard.goto(0, 0)
    scoreboard.write("Press 'r' to Start", align="center", font=("Courier", 20, "normal"))
    screen.update()
    
    # The first game starts when the user presses 'r'.
    # Subsequent games are also handled by the restart_game function.


if __name__ == "__main__":
    main()
    # Keep the window open until it's clicked
    screen = Screen()
    screen.exitonclick()
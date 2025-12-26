# Snake Game

This is a classic Snake game implemented in Python using the `turtle` module.

## Description

The player controls a snake that moves around the screen. The objective is to eat the food pellets that appear at random locations. Each time the snake eats a pellet, it grows longer and the player's score increases. The game ends if the snake collides with the walls of the screen or with its own tail. The game keeps track of the high score, which is saved locally in `data.txt`.

## File Structure

- `main.py`: The main entry point for the game. It handles the game loop and brings all the modules together.
- `snake.py`: Defines the `Snake` class, which controls the snake's behavior, including movement and growth.
- `food.py`: Defines the `Food` class, which manages the food pellets.
- `scoreboard.py`: Defines the `Scoreboard` class, which handles the scoring and high score persistence.
- `data.txt`: A text file that stores the high score.

## How to Run

1.  Ensure you have Python installed on your system.
2.  Navigate to the `20_day (snake game)` directory in your terminal.
3.  Run the following command:

    ```bash
    python main.py
    ```

## Controls

- **Up Arrow**: Move the snake up
- **Down Arrow**: Move the snake down
- **Left Arrow**: Move the snake left
- **Right Arrow**: Move the snake right

Enjoy the game!

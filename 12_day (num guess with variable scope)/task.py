import random

def check_guess(guess):
    if guess > secret_number:
        print("Too high.")
    elif guess < secret_number:
        print("Too low.")
    else:
        print(f"You got it! The answer was {secret_number}.")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return 10
    elif level == "hard":
        return 5
    else:
        print("Invalid input. Please choose 'easy' or 'hard'.")
        return set_difficulty()

secret_number = random.randint(1,100)

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")

attempts = set_difficulty()
def game(check_guess, secret_number, attempts):

    guess=0
    for i in range(attempts):
        print(f"You have {attempts - i} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        check_guess(guess)
        if guess == secret_number:
            break

    if guess != secret_number:
        print(f"You've run out of guesses, you lose. The correct answer was {secret_number}.")

game(check_guess, secret_number, attempts)


 
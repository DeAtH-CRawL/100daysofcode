import random
random_number = random.randint(0, 1)
if random_number == 0:
    print("Tails")
else:
    print("Heads")
# This code simulates a coin toss by generating a random integer (0 or 1)
# and printing "Tails" for 0 and "Heads" for 1.
# It uses the random module to achieve this functionality.
# The random.randint(a, b) function returns a random integer N such that a <= N <= b.
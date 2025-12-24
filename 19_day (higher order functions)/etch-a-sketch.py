from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

tim.shape("turtle")
tim.pensize(2)
tim.speed("fastest")

# State to hold which keys are currently pressed
keys_pressed = set()

def forward():
    tim.forward(10)

def backward():
    tim.backward(10)

def left():
    tim.left(10)

def right():
    tim.right(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

# Movement loop
def move():
    if 'w' in keys_pressed:
        forward()
    if 's' in keys_pressed:
        backward()
    if 'a' in keys_pressed:
        left()
    if 'd' in keys_pressed:
        right()
    # Rerun the move function after a short delay
    screen.ontimer(move, 30) # Using a 30ms delay for smoother movement

# Key press/release handlers 
def add_key(key):
    keys_pressed.add(key)

def remove_key(key):
    # Use discard to avoid errors if the key is already not in the set
    keys_pressed.discard(key)

screen.listen()

# Bind key press events
screen.onkeypress(lambda: add_key('w'), "w")
screen.onkeypress(lambda: add_key('s'), "s")
screen.onkeypress(lambda: add_key('a'), "a")
screen.onkeypress(lambda: add_key('d'), "d")

# Bind key release events
screen.onkeyrelease(lambda: remove_key('w'), "w")
screen.onkeyrelease(lambda: remove_key('s'), "s")
screen.onkeyrelease(lambda: remove_key('a'), "a")
screen.onkeyrelease(lambda: remove_key('d'), "d")

# Bind clear screen function to 'c' (using onkey is fine for single press)
screen.onkey(clear, "c")

# Start the movement loop
move()

screen.exitonclick()

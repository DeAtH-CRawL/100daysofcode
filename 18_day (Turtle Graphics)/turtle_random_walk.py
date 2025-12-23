import turtle as tim
import random
screen = tim.Screen()
screen.bgcolor("black")
tim.screensize(1000, 1000)
colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "white", "grey", "black", "cyan", "magenta", "lime", "maroon", "navy", "olive", "teal"]
steps = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(tim)
tim.shape("turtle")
tim.pensize(15)
directions = [0, 90, 180, 270, 360, 450, 540, 630, 720, 810, 900]
tim.pencolor("pink")
tim.speed("fastest")

for _ in range(300):
    tim.color(random.choice(colors))
    tim.forward(random.choice(steps))
    tim.setheading(random.choice(directions))
    
screen.exitonclick()

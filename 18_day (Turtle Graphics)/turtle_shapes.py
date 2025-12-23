import turtle as tim
import random
screen = tim.Screen()
screen.bgcolor("black")
colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "white", "grey", "black", "cyan", "magenta", "lime", "maroon", "navy", "olive", "teal"]
print(tim)
tim.shape("turtle")
# set the color of the turtle to (186, 184, 108) olive green (red, green, blue)
tim.pencolor("pink")
# (n(n-2))/180 
tim.speed(10000000)
tim.penup()
tim.goto(-200,300)
tim.pendown()
for num_of_sides in range(3,10):
    tim.color(random.choice(colors))
    angle = 360/num_of_sides
    for i in range(num_of_sides):
        tim.forward(100)
        tim.right(angle)
    num_of_sides += 1


    
    #making a pentagon




screen.exitonclick()
""" There is a lot of fun stuff you can do with your turtles. You can find full documentation here:"""
# https://docs.python.org/3.3/library/turtle.html?highlight=turtle

""" Comment the turtle program below, then add some of your own commands to make some turtles do some fun stuff."""

import turtle
import random

HEIGHT = 600
WIDTH = 800
MAX = max(HEIGHT, WIDTH)
NUM_TURTLES = 5


def create_screen():
    wn = turtle.Screen()
    wn.setup(1200, 1080, startx=None, starty=None)
    wn.colormode(255)
    wn.title("Turtle Tag")
    return wn


def create_turtles():
    turtle_list = []
    for i in range(NUM_TURTLES):
        new_turtle = turtle.Turtle()
        new_turtle.shape("turtle")
        new_turtle.penup()
        new_turtle.fillcolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        new_turtle.left(random.randint(0, 180))
        new_turtle.forward(random.randint(1, MAX/2))
        turtle_list.append(new_turtle)
    return turtle_list


def chase(turtle_list):
    for i in range(NUM_TURTLES-1):

        position = turtle_list[i+1].position()
        direction = turtle_list[i].towards(position)

        distance = turtle_list[i].distance(position)

        turtle_list[i].setheading(direction)
        turtle_list[i].forward(distance)
        print(i, position, distance, direction)


def main():
    wn = create_screen()
    turtle_list = create_turtles()
    chase(turtle_list)
    wn.mainloop()

main()
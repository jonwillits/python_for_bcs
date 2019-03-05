""" Now let's put together what we know about inheritance with what we know about the turtle class, and create a
    a special enhanced turtle class.

    If we want to use the Turtle class as a base, and enhance our turtles, we can do that by inheriting it. We just make
    the Turtle class an input parameter in our class definition. Before, when we inhereted Animal into Bird, we just
    had class Bird(Animal). This time, since the Turtle class is in the turtle module (and not defined in this file), we
    need to put turtle.Turtle as the input parameter in the class definition. And then we need to remember to call
    Turtle's init function as the first line of our init function.

    Then we can add other attributes and methods.


"""

import turtle


class SuperTurtle(turtle.Turtle):

    def __init__(self, name):
        turtle.Turtle.__init__(self)
        self.name = name
        self.shape('turtle')
        self.speed('fastest')
        self.ondrag(self.draw)
        self.onclick(self.glow)
        self.onrelease(self.unglow)

    def glow(self, x, y):
        self.fillcolor(255, 0, 0)

    def unglow(self, x, y):
        self.fillcolor("")

    def draw(self, x, y):
        self.ondrag(None)
        self.setheading(self.towards(x, y))
        self.goto(x, y)
        self.ondrag(self.draw)


wn = turtle.Screen()
wn.delay(1)
wn.colormode(255)

my_turtle = SuperTurtle('Jon')
wn.mainloop()

""" the advantage to creating these custom classes is that we can put all the complex program code in our class 
defitions, and maek the actual code that we use to do stuff simple and easy to read. WHen you add stuff to a list,
dozens of lines of code are executed. But they are all in the list class definition, and so you can just type 
list.append() without needing to copy and paste that code every time. And then if you want to change how it works,
you only need to change it in the class definition, not everywhere you used it."""

# Comment this code and then add your own turtle functions.

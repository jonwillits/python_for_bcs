""" Now we get to have some fun with some very basic animations. Python has a built-in library called turtle, that
allows us to create turtle graphics. First, we have to import the turtle module."""

import turtle               # allows us to use the turtles library

""" Turtle is a module that has a number of built in classes.

One such class is Screen(), which creates a window object for the turtles to appear in. With this line, we are creating 
an instance of the Screen class, and storing it in the variable wn."""
wn = turtle.Screen()        # creates a graphics window

"""If you run the program like this, you'll probably see a window flash into existence and then disappear almost 
immediately. """

""" If you comment the four lines below and then run the program, you should see something happen"""
jon = turtle.Turtle()
jon.forward(150)
jon.left(90)
jon.forward(75)

""" The first line creates an instance of the Turtle class. Note the capitalization; remember that module names are 
lower cased, and we access stuff in the module with a period. Class names are usually Capitalized. So since the Turtle
class is inside the turtle module, we access it with turtle.Turtle(). """

""" The next three lines are methods of the turtle class. The forward() method moves the turtle forward a specified
number of pixels. The left() method rotates the turtle the number of degrees specified.

After these actions are completed, the window once again disappears. We can stop this by using the following command,
which calls a built-in method of the Screen class, which keeps the window open until it is clicked on.
"""
wn.exitonclick()

""" Take a look at your terminal window. You'll notice that this time, while the screen is still open, the program
is still running, as evidenced by the fact that you cannot type new stuff into it while the turtle window is open."""

""" Also, mac users may see a weird error:
 2019-02-25 17:00:51.535 Python[60326:7980585] ApplePersistenceIgnoreState: Existing state will not be touched.
 
 You can make this error go away by pasting and entering the following in your terminal window:
 defaults write org.python.python ApplePersistenceIgnoreState NO
 """
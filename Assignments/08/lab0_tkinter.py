import tkinter as tk
import sys
import time

"""
tkinter is a module that can be used to build simple graphical user interfaces (GUIs) in python. If you don't already
have tkinter installed, you will need to install it by running the command "python3 -w pip install tkinter" in your
terminal window

there are a couple of basic things to understand about tkinter, demonstrated in the program below. In it, I have a
simple main function with three lines. The first line just defines the size of the window that will open.
The second line creates on instance of the Simulation class. The third line is necessary to keep the window open, while
the program waits for stuff to happen. If you were to comment out the last line, you would see the window appear and 
then immediately disappear when you ran the program.

Besides the main function, this program has a "Simulation" class and a "Hunter" class. The Hunter is a class that 
defines an agent that can move around in the window. Scroll down and look at it first, and read the text there.

GO READ THE HUNTER CLASS NOW

In addition to the Hunter class, there is a Simulation class. It has many methods and attributes. They are explained
step-by-step below.
"""


class Simulation:
    ###############################################################################################################
    def __init__(self, screen_size):

        """
        In the class's init function, we see the line: self.root = tk.Tk(). Think of "root" as the highest level
        reference to your window. It is like the main window that you put everything inside. we attach it to the class
        by creating self.root. The next line allows us to change the name on the window. The next line takes the screen
        size variable we passed to the class, and stores it as a member of the class, but this line doesnt do anything
        to the window (like change the size), we're just storing the variable for use later.

        The next five lines keep track of some variables we are interested in tracking in the simulation.
            - whether the simulation is running or not
            - what time the simulation started
            - how long it has been running
            - where someone clicked the mouse
            - what key someone pressed

        Next, we create a Hunter instance and attach it to this class. Note here is another example of a class being a
        attribute of a class.

        Finally, we call our two methods that create the actual window. To make things look nice, we have divided our
        window into two "frames", one where our stuff will appear, and one where the user interface buttons will appear.
        """

        self.root = tk.Tk()
        self.root.title("Tkinter Demonstration")
        self.screen_size = screen_size

        self.running = False
        self.start_time = 0
        self.run_time = 0
        self.last_click_position = None
        self.last_key_press = None

        self.hunter = Hunter()

        self.create_button_frame()
        self.create_main_frame()

    def create_button_frame(self):
        '''
        In this method, first we have to create an actual frame, and we pass it the window's root variable, which
        tells tkinter that the button_frame belongs to the root window (in other words, root is its parent).

        Next we create our actual buttons. Buttons have a bunch of arguments, the first is the frame that they go
        in. In other words, you are specifying that buttons belong to a frame, or which frame is their parent. In this
        way, we could have lots of different frames in our window and say which buttons go where. The other parameters
        let us specify the text, the text color, and what functions get called when the button is clicked.

        Last, you see that for each element (the frame and the buttons themselves), we have to call the pack() method.
        Pack() is what actually puts them into their parent. If you forget this line, they wont actually appear.
        Pack arranges elements in the frame in the order that you call them. The argument passed to pack tells pack how
        to arrange each element relative to the previous element it packed. By specifying left, they will all go with
        the previous element on their left. Try removing this argument and seeing what happens.
        '''

        self.button_frame = tk.Frame(self.root)
        self.start_button = tk.Button(self.button_frame, text="Start", fg="black", command=self.start_stop)
        self.reset_button = tk.Button(self.button_frame, text="Reset", fg="black", command=self.reset)
        self.quit_button = tk.Button(self.button_frame, text="Quit", fg="black", command=self.quit)
        self.button_frame.pack()
        self.start_button.pack(side=tk.LEFT)
        self.reset_button.pack(side=tk.LEFT)
        self.quit_button.pack(side=tk.LEFT)

    def create_main_frame(self):
        '''
        Next we have our main frame, where we are going to put our content. There is not a lot here, since all the main
        action is done in other functions. But what is here? We create a frame, and pack it. Note that it gets packed
        relative to the last thing that was packed in tk.root (its parent), not the last thing we packed overall (the
        buttons), because their parents were not the same as this frame.

        Next we create a canvas, and put it inside the frame. A canvas is a tkinter element that we can draw stuff in,
        like shapes, lines, text, and images. We pack it in its parent (the main_frame). We also tell tkinter to
        focus_set() the canvas, meaning that it is to be treated as the currently selected object, for reasons I will
        explain later.

        Lastly, we prepare the Simulation window to handle events like mouse clicks and key presses. we do this by
        using the bind() function on the canvas. Bind can take many different arguments for different kinds of binding
        events, but two very common ones are key presses and mouse clicks, as shown below. The second argument for bind
        specifies the function that will be called when one of those events occurs.

        A couple of notes. First, The key press binding will notice any key press. But if you want it to limit to a
        single kind or set of key presses (like just space bar, or arrow keys, or something), you can do that. Second,
        note that the .bind() function is called on the canvas object. This means that it will only notice mouse clicks
        in the canvas, not, for example in the button frame. Because the <Key> bind was done to the canvas, it will
        only register key presses when the canvas is the program's actively focused object. This is why we need the
        focus_set() method used. We could instead have have called bind("<BUTTON>") or bind("<KEY">) on button frame,
        and then it would have only have registered those events when they happened in that frame. If we have used
        bind() on self.root, then the events would be registered  no matter where they happen in the window. You could
        also use bind() on specific objects (like the hunter image), and then it will only register clicks on the hunter
        or key presses when the hunter was activated.

        Finally, this function calls redraw_window(), which does all the drawing in the window itself.
        '''

        self.main_frame = tk.Frame(self.root, width=self.screen_size[0], height=self.screen_size[1])
        self.main_frame.pack()
        self.main_canvas = tk.Canvas(self.main_frame, width=self.screen_size[0], height=self.screen_size[1],
                                     background='black')
        self.main_canvas.pack()
        self.main_canvas.focus_set()
        self.main_canvas.bind("<Button-1>", self.main_canvas_click)
        self.main_canvas.bind("<Key>", self.key_press)
        self.redraw_window()

    def redraw_window(self):
        '''
        redraw window does a bunch of stuff. See if you can understand it below, and comment each line
        it might help you to understand some of the lines by commenting them out or changing them, and running
        the program and seeing what happens.
        '''

        # comment here
        if self.last_click_position is None:
            x = None
            y = None
        else:
            x = self.last_click_position.x
            y = self.last_click_position.y

        # comment here
        if self.last_key_press is None:
            key = None
            key_x = None
            key_y = None
        else:
            key = self.last_key_press.keysym
            key_x = self.last_key_press.x
            key_y = self.last_key_press.y

        # comment here
        self.main_canvas.delete("all")

        # comment here
        self.main_canvas.create_image(self.hunter.x, self.hunter.y, anchor=tk.NW, image=self.hunter.image)

        # comment here
        self.main_canvas.create_text(self.screen_size[0] / 2, self.screen_size[1] / 2 - 30,
                                     text="Running Time: {:0.2f}".format(self.run_time),
                                     fill='white')
        # comment here
        self.main_canvas.create_text(self.screen_size[0] / 2, self.screen_size[1] / 2,
                                     text="Last Click Position: ({},{})".format(x, y),
                                     fill='white')

        # comment here
        self.main_canvas.create_text(self.screen_size[0] / 2, self.screen_size[1] / 2 + 30,
                                     text="Last Key Press: {} while cursor at ({},{})".format(key, key_x, key_y),
                                     fill='white')

        # comment here
        self.root.update()
        self.root.update_idletasks()

    def key_press(self, key):
        '''
        this is called when a key is pressed. It is passed a "key" object, which contains a lot of useful information,
        like what key was pressed but also where the cursor was when a key was pressed. Add a print statement here that
        prints out the value of key whenever a key is pressed, and observe what is printed in the terminal

        redraw window is called because, as you observed, what gets drawn to the window changes when a key is pressed
        '''
        self.last_key_press = key
        self.redraw_window()

    def main_canvas_click(self, event):
        '''
        this is called when a the left mouse button is pressed in the main canvas. It is passed a mouse press object,
        which contains a lot of useful information, like where the cursor was when the mouse was clicked. Add a print
        statement here that prints out the value of mouse click object whenever it is clicked
        '''
        self.last_click_position = event
        self.redraw_window()

    def start_stop(self):
        '''
        this is called whenever the start/pause button is pressed. add comments that explain the behavior of this
        function
        '''
        # your comments here
        if self.running:
            self.running = False
            self.start_button.config(text="Start")
        else:
            self.start_time = time.time()
            self.running = True
            self.start_button.config(text="Pause")

        # your comments here
        while self.running:
            self.run_time += (time.time() - self.start_time)
            self.hunter.move()
            self.redraw_window()
            time.sleep(0.01)

    def reset(self):
        '''
        this is called whenver the reset button is pressed. it calls the hunter's reset method (which sets them
        back to their initial position and direction), and resets all the classes attributes to their original states,
        and redraws the window.
        '''
        self.hunter.reset()
        self.run_time = 0
        self.last_click_position = None
        self.last_key_press = None
        self.redraw_window()

    def quit(self):
        '''
        this is called when the quit button is pressed. it quits the program.
        '''
        sys.exit()


class Hunter:
    '''
    The hunter class has four attributes. Its x position, y position, direction it is moving, and the image associated
    with the hunter. This image line is new, using the tk.PhotoImage method, which is the way you need to load an image
    from your computer to be used with tkinter.

    The hunter class has two methods, one that resets the hunter back to its original state (which is also called when
    a new hunter instance is created), and one that moves the hunter according to a simple set of rules.
    ADD SOME COMMENTS THAT EXPLAIN HOW THE HUNTER WILL MOVE. Then return to the top and resume reading about tkinter.
    '''

    def __init__(self):
        self.x = None
        self.y = None
        self.direction = None
        self.image = tk.PhotoImage(file='hunter.gif')
        self.reset()

    def reset(self):
        self.x = 100
        self.y = 100
        self.direction = 'right'

    def move(self):
        if self.direction == 'right':
            if self.x >= 700:
                self.direction = 'left'
                self.x -= 10
            else:
                self.x += 10
        else:
            if self.x <= 100:
                self.direction = 'right'
                self.x += 10
            else:
                self.x -= 10


def main():
    screen_size = (800, 600)
    my_simulation = Simulation(screen_size)
    my_simulation.root.mainloop()


main()

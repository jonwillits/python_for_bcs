import tkinter as tk
from turtle import RawTurtle, TurtleScreen
import random
import math
import sys
import time

# comment here
SCREEN_SIZE = 500
MAX_LOCATION = SCREEN_SIZE / 2 - 10


class Sugar:

    def __init__(self, turtle_window, id_number):

        # comment here
        self.turtle_window = turtle_window
        self.id_number = id_number
        self.name = 'Sugar'

        # comment here
        self.turtle_object = RawTurtle(self.turtle_window.wn)
        self.turtle_object.hideturtle()
        self.turtle_object.shape('square')
        self.turtle_object.penup()
        self.turtle_object.color("black", "white")
        self.place()
        self.turtle_object.showturtle()

        # comment here
        self.turtle_object.ondrag(self.drag)

    def place(self):
        # comment here
        self.turtle_object.goto(random.randint(-MAX_LOCATION, MAX_LOCATION),
                                random.randint(-MAX_LOCATION, MAX_LOCATION))

    def drag(self, x, y):
        # comment here
        self.turtle_object.goto(x, y)
        self.turtle_window.wn.update()


class Vehicle:

    def __init__(self, turtle_window, id_number):

        # comment here
        self.turtle_window = turtle_window
        self.id_number = id_number

        # comment here
        self.speed_params = [20, 0.2, 6]
        self.turn_parameters = [20]

        # comment here
        self.turtle_object = RawTurtle(self.turtle_window.wn)
        self.turtle_object.hideturtle()
        self.turtle_object.shape('turtle')
        self.turtle_object.turtlesize(1)
        self.turtle_object.penup()

        # comment here
        self.likes_food_dict = {'Sugar': random.choice([True, False])}

        # comment here
        if self.likes_food_dict['Sugar']:
            self.turtle_object.color("red", (1, 0.85, 0.85))
        else:
            self.turtle_object.color("blue", (0.85, 0.85, 1))

        # comment here
        self.place()
        self.turtle_object.showturtle()

    def place(self):
        # comment here
        self.turtle_object.goto(random.randint(-MAX_LOCATION, MAX_LOCATION),
                                random.randint(-MAX_LOCATION, MAX_LOCATION))
        self.turtle_object.right(random.randint(0, 360))

    def move(self):

        # comment here
        cumulative_speed = 0
        cumulative_turn_amount = 0

        # comment here
        for food_source in self.turtle_window.food_source_list:

            # comment here
            likes_food = self.likes_food_dict[food_source.name]

            # comment here
            input_distance = self.turtle_object.distance(food_source.turtle_object.pos())

            # comment here
            input_angle = self.turtle_object.heading() - self.turtle_object.towards(food_source.turtle_object.pos())

            # comment here
            sin_angle = math.sin(math.radians(input_angle))

            # comment here
            left_sensor_distance = input_distance - sin_angle
            right_sensor_distance = input_distance + sin_angle

            # comment here
            left_speed, right_speed, combined_speed = self.compute_speed(left_sensor_distance,
                                                                         right_sensor_distance,
                                                                         likes_food)

            # comment here
            turn_amount = self.turn_parameters[0] * (right_speed - left_speed)

            # comment here
            cumulative_speed += combined_speed
            cumulative_turn_amount += turn_amount

        # comment here
        if isinstance(cumulative_turn_amount, complex):
            cumulative_turn_amount = 0

        # comment here
        if cumulative_speed < 0:
            cumulative_speed = 0

        # comment here
        self.turtle_object.right(cumulative_turn_amount)
        self.turtle_object.forward(cumulative_speed)

        # comment here
        self.check_border_collision()

    def check_border_collision(self):
        '''
        comment here. Make one big comment for the function, but it must be more specific and detailed then
        just repeating the function name...
        '''

        if self.turtle_object.xcor() > MAX_LOCATION:
            self.turtle_object.goto(MAX_LOCATION, self.turtle_object.ycor())
        if self.turtle_object.xcor() < -MAX_LOCATION:
            self.turtle_object.goto(-MAX_LOCATION, self.turtle_object.ycor())

        if self.turtle_object.ycor() > MAX_LOCATION:
            self.turtle_object.goto(self.turtle_object.xcor(), MAX_LOCATION)
        if self.turtle_object.ycor() < -MAX_LOCATION:
            self.turtle_object.goto(self.turtle_object.xcor(), -MAX_LOCATION)

        if self.turtle_object.ycor() <= -MAX_LOCATION:
            if 0 <= self.turtle_object.heading() <= 180:
                turn_angle = 180 - self.turtle_object.heading()
                self.turtle_object.setheading(turn_angle)
            else:
                turn_angle = abs(360 - self.turtle_object.heading())
                self.turtle_object.setheading(turn_angle)

        if self.turtle_object.ycor() >= MAX_LOCATION:
            if 0 <= self.turtle_object.heading() <= 180:
                turn_angle = 360 - self.turtle_object.heading()
                self.turtle_object.setheading(turn_angle)
            else:
                turn_angle = 360 - (self.turtle_object.heading() - 180)
                self.turtle_object.setheading(turn_angle)

        if self.turtle_object.xcor() <= -MAX_LOCATION:
            if 0 <= self.turtle_object.heading() <= 90:
                turn_angle = 360 - self.turtle_object.heading()
                self.turtle_object.setheading(turn_angle)
            if 270 < self.turtle_object.heading() <= 360:
                turn_angle = 360 - self.turtle_object.heading()
                self.turtle_object.setheading(turn_angle)
            if 90 < self.turtle_object.heading() < 180:
                turn_angle = self.turtle_object.heading() - 90
                self.turtle_object.setheading(turn_angle)
            if 180 <= self.turtle_object.heading() <= 360:
                turn_angle = self.turtle_object.heading() + 90
                self.turtle_object.setheading(turn_angle)

        if self.turtle_object.xcor() >= MAX_LOCATION:
            if 0 <= self.turtle_object.heading() <= 180:
                turn_angle = self.turtle_object.heading() + 90
                self.turtle_object.setheading(turn_angle)
            else:
                turn_angle = self.turtle_object.heading() - 90
                self.turtle_object.setheading(turn_angle)

    ###############################################################################################################
    def compute_speed(self, left_distance, right_distance, likes_food):

        '''
        comment here. Make one big comment for the function, but it must be more specific and detailed then
        just repeating the function name... explain this in Braitenberg's terms
        '''

        if likes_food:
            left_speed = (self.speed_params[0] / (right_distance ** self.speed_params[1])) - self.speed_params[2]
            right_speed = (self.speed_params[0] / (left_distance ** self.speed_params[1])) - self.speed_params[2]
        else:
            left_speed = (self.speed_params[0] / (left_distance ** self.speed_params[1])) - self.speed_params[2]
            right_speed = (self.speed_params[0] / (right_distance ** self.speed_params[1])) - self.speed_params[2]
        combined_speed = (left_speed + right_speed) / 2
        return left_speed, right_speed, combined_speed


###################################################################################################################
###################################################################################################################
class TurtleWindow:
    ###############################################################################################################
    def __init__(self, num_vehicles, num_food_sources):
        self.root = None
        self.canvas = None
        self.wn = None
        self.button_frame = None
        self.start_button = None
        self.stop_button = None
        self.reset_button = None
        self.quit_button = None

        self.num_food_sources = num_food_sources
        self.food_source_list = []

        self.num_vehicles = num_vehicles
        self.vehicle_list = []

        self.running = False

        self.create_window()
        self.wn.tracer(0, 0)
        self.create_food_sources()
        self.create_vehicles()
        self.wn.update()

    ###############################################################################################################
    def create_window(self):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=SCREEN_SIZE, height=SCREEN_SIZE)
        self.canvas.pack()
        self.wn = TurtleScreen(self.canvas)
        self.root.title("Braitenberg's Vehicle #2")
        self.wn.onkey(self.start_stop, "space")
        self.wn.listen()

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack()

        self.start_button = tk.Button(self.button_frame, text="Start", fg="black", command=self.start_stop)
        self.reset_button = tk.Button(self.button_frame, text="Reset", fg="black", command=self.reset)
        self.quit_button = tk.Button(self.button_frame, text="Quit", fg="black", command=self.quit)
        self.start_button.pack(side=tk.LEFT)
        self.reset_button.pack(side=tk.LEFT)
        self.quit_button.pack(side=tk.LEFT)

    ###############################################################################################################
    def create_food_sources(self):
        for i in range(self.num_food_sources):
            food_type = random.choice(['sugar'])
            if food_type == 'sugar':
                self.food_source_list.append(Sugar(self, i))
        print(self.food_source_list)

    ###############################################################################################################
    def create_vehicles(self):
        for i in range(self.num_vehicles):
            self.vehicle_list.append(Vehicle(self, i))

    ###############################################################################################################
    def start_stop(self):
        if self.running:
            self.running = False
            self.start_button.config(text="Start")
        else:
            self.running = True
            self.start_button.config(text="Pause")

        while self.running:
            for i in range(self.num_vehicles):
                self.vehicle_list[i].move()
            self.wn.update()
            time.sleep(0.01)

    ###############################################################################################################
    def reset(self):
        self.vehicle_list = []
        self.food_source_list = []

        self.wn.clear()
        self.wn.tracer(0, 0)
        self.create_food_sources()
        self.create_vehicles()
        self.wn.update()

    ###############################################################################################################
    @staticmethod
    def quit():
        sys.exit()


###################################################################################################################
###################################################################################################################
###################################################################################################################
###################################################################################################################

def main():
    num_turtles = 3
    num_food_sources = 3
    turtle_window = TurtleWindow(num_turtles, num_food_sources)
    turtle_window.wn.mainloop()


main()

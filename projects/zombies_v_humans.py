import turtle
import random
import time
import sys
import os


class Agent(turtle.Turtle):
	def __init__(self, screen_size, start_position=None):
		turtle.Turtle.__init__(self)
		self.name = "Agent"
		self.hideturtle()
		self.penup()
		self.movement_speed = 20
		self.movement_jitter = 0
		self.screen_size = screen_size
		self.interest_list = []

		self.start_position = start_position
		self.closest_agent_index = None
		self.closest_agent_position = None
		self.closest_agent_distance = None

		self.place()

	def place(self):
		max_location = self.screen_size / 2 - 200
		if self.start_position is None:
			x = random.randint(-max_location, max_location)
			y = random.randint(-max_location, max_location)
			self.setpos(x, y)
		else:
			self.setpos(self.start_position)
		self.check_border_collision()
		self.showturtle()

	def find_closest(self, world):
		self.closest_agent_index = None
		self.closest_agent_position = None
		self.closest_agent_distance = 1000000
		for i in range(len(world.agent_list)):
			current_agent = world.agent_list[i]
			if current_agent.name in self.interest_list:
				agent_position = world.agent_list[i].pos()
				agent_distance = self.distance(agent_position)
				if agent_distance < self.closest_agent_distance:
					self.closest_agent_distance = agent_distance
					self.closest_agent_index = i
					self.closest_agent_position = agent_position

	def check_border_collision(self):
		max_location = self.screen_size / 2 - 50
		if self.xcor() > max_location:
			x = max_location + random.randint(-self.movement_jitter, self.movement_jitter)
			y = self.ycor() + random.randint(-self.movement_jitter, self.movement_jitter)
			self.goto(x, y)
		if self.xcor() < -max_location:
			x = -max_location + random.randint(-self.movement_jitter, self.movement_jitter)
			y = self.ycor() + random.randint(-self.movement_jitter, self.movement_jitter)
			self.goto(x, y)
		if self.ycor() > max_location:
			x = self.xcor() + random.randint(-self.movement_jitter, self.movement_jitter)
			y = max_location + random.randint(-self.movement_jitter, self.movement_jitter)
			self.goto(x, y)
		if self.ycor() < -max_location:
			x = self.xcor() + random.randint(-self.movement_jitter, self.movement_jitter)
			y = -max_location + random.randint(-self.movement_jitter, self.movement_jitter)
			self.goto(x, y)


class Zombie(Agent):

	def __init__(self, screen_size, start_position=None):
		Agent.__init__(self, screen_size, start_position=None)
		self.name = 'zombie'
		self.shape('images/zombie.gif')
		self.movement_speed = 20
		self.movement_jitter = 30
		self.start_difference = 5
		self.interest_list = ['civilian', 'soldier']

	def take_turn(self, the_world):
		self.find_closest(the_world)
		if self.closest_agent_distance > 100:
			self.wander()
		else:
			self.chase()
			if self.closest_agent_distance < 25:
				new_zombie = self.attack(the_world)
				the_world.agent_list.append(new_zombie)
		self.check_border_collision()

	def wander(self):
		self.setheading(random.randint(0, 360))
		self.forward(self.movement_speed/2)

	def chase(self):
		direction = self.towards(self.closest_agent_position)
		self.setheading(direction + random.randint(-self.movement_jitter/2, self.movement_jitter/2))
		if self.closest_agent_distance < self.movement_speed:
			self.forward(self.closest_agent_distance)
		else:
			self.forward(self.movement_speed)

	def attack(self, the_world):

		target = the_world.agent_list[self.closest_agent_index]
		print("ATTACK!:", self.position(), target.position())

		x_diff = random.randint(-self.start_difference, self.start_difference)
		y_diff = random.randint(-self.start_difference, self.start_difference)
		new_start_pos = (target.position()[0]+x_diff, target.position()[1]+y_diff)
		print("new start:", new_start_pos)
		new_zombie = Zombie(the_world.screen_size, new_start_pos)

		the_world.agent_pop_size_dict[target.name] -= 1
		the_world.agent_pop_size_dict['zombie'] += 1

		the_world.agent_list[self.closest_agent_index].hideturtle()
		the_world.agent_list.remove(the_world.agent_list[self.closest_agent_index])

		return new_zombie


class Civilian(Agent):

	def __init__(self, screen_size, start_position=None):
		Agent.__init__(self, screen_size, start_position=None)
		self.name = 'civilian'
		self.movement_speed = 30
		self.movement_jitter = 20
		self.strategy = random.choice(['random', 'away'])
		if self.strategy == 'random':
			self.shape('images/homer.gif')
		else:
			self.shape('images/lisa.gif')
		self.interest_list = ['zombie']

	def take_turn(self, the_world):
		if self.strategy == 'away':
			self.run_away(the_world)
		elif self.strategy == 'random':
			self.run_random()
		else:
			self.run_random()
		self.check_border_collision()

	def run_random(self):
		self.setheading(random.randint(0, 360))
		self.forward(self.movement_speed)

	def run_away(self, the_world):
		self.find_closest(the_world)
		if self.closest_agent_index is not None:
			direction = self.towards(self.closest_agent_position)
			self.setheading(direction-180)
			self.forward(self.movement_speed)
			x = self.xcor()+random.randint(-self.movement_jitter, self.movement_jitter)
			y = self.xcor()+random.randint(-self.movement_jitter, self.movement_jitter)
			self.goto(x, y)
			self.check_border_collision()


class Soldier(Agent):

	def __init__(self, screen_size, start_position=None):
		Agent.__init__(self, screen_size, start_position=None)
		self.name = 'soldier'
		self.shape('images/soldier.gif')
		self.movement_speed = 10
		self.movement_jitter = 0
		self.shooting_range = 50
		self.interest_list = ['zombie']

	def take_turn(self, the_world):
		self.find_closest(the_world)
		self.chase()
		if self.closest_agent_distance < self.shooting_range:
			self.shoot(the_world)

	def chase(self):
		if self.closest_agent_index is not None:
			direction = self.towards(self.closest_agent_position)
			self.setheading(direction)
			if self.closest_agent_distance > self.shooting_range:
				self.forward(self.movement_speed)

	def shoot(self, the_world):
		target = the_world.agent_list[self.closest_agent_index]
		bullet = Bullet(target, self.position())
		hit = bullet.shoot(self.shooting_range, the_world)
		if hit:
			target.hideturtle()
			the_world.agent_list.remove(target)
			the_world.agent_pop_size_dict[target.name] -= 1
		del bullet


class Bullet(turtle.Turtle):
	def __init__(self, target, origin):
		turtle.Turtle.__init__(self)
		self.target = target
		self.shape('images/bullet.gif')
		self.origin = origin
		self.penup()
		self.hideturtle()
		self.precision = 5
		self.goto(origin)
		self.setheading(self.towards(target.position()))
		self.showturtle()

	def shoot(self, shooting_range, the_world):
		for i in range(int(shooting_range/5)):
			self.forward(2)
			the_world.wn.update()
			if self.distance(self.target) < self.precision:
				self.hideturtle()
				return True
		self.hideturtle()
		return False


class World:

	def __init__(self, agent_type_list, starting_pop_counts, screen_size):
		self.agent_type_list = agent_type_list
		self.agent_pop_size_dict = {}
		self.starting_pop_counts = starting_pop_counts
		self.screen_size = screen_size
		self.wn = None
		self.agent_list = None
		self.animation_delay = 0

		self.num_agent_types = len(self.agent_type_list)
		if self.num_agent_types != len(self.starting_pop_counts):
			print("ERROR: number of starting pop counts must equal number of agent types {}".format(self.num_agent_types))
			sys.exit(2)

		self.create_screen()
		self.load_images()
		self.add_agents()

	def create_screen(self):
		self.wn = turtle.Screen()
		self.wn.title("Zombies!")
		self.wn.tracer(0, 0)
		self.wn.colormode(255)
		self.wn.bgcolor("white")
		self.wn.setup(self.screen_size, self.screen_size, startx=None, starty=None)

	def load_images(self):
		image_list = os.listdir('images/')
		for image in image_list:
			if image[0] != '.':
				self.wn.register_shape('images/' + image)

	def add_agents(self):
		self.agent_list = []

		for i in range(self.num_agent_types):
			agent_type = self.agent_type_list[i]
			num_agents = self.starting_pop_counts[i]
			self.agent_pop_size_dict[agent_type] = num_agents
			for j in range(num_agents):
				if agent_type == 'zombie':
					new_agent = Zombie(self.screen_size)
				elif agent_type == 'civilian':
					new_agent = Civilian(self.screen_size)
				elif agent_type == 'soldier':
					new_agent = Soldier(self.screen_size)
				else:
					print("ERROR: Unrecognized agent type {}".format(agent_type))
					sys.exit()
				self.agent_list.append(new_agent)

		self.wn.update()

	def take_turn(self):
		i = 0
		while i < len(self.agent_list):
			self.agent_list[i].take_turn(self)
			self.wn.update()
			time.sleep(self.animation_delay)
			i += 1
			output_string = "Turn {}:".format(i)
			for agent_type in self.agent_pop_size_dict:
				output_string += "    {}: {}".format(agent_type, self.agent_pop_size_dict[agent_type])

	def get_num_non_zombies(self):
		num_non_zombies = 0
		for agent_type in self.agent_pop_size_dict:
			if agent_type != 'zombie':
				num_non_zombies += self.agent_pop_size_dict[agent_type]
		return num_non_zombies


def main():
	agent_type_list = ['civilian', 'zombie', 'soldier']
	starting_pop_counts = [10, 1, 1]

	the_world = World(agent_type_list, starting_pop_counts, 800)

	while the_world.get_num_non_zombies() > 0:
		the_world.take_turn()

	the_world.wn.mainloop()


main()


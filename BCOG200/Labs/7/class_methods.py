""" have already introduced kind of class function, __init__ ."""

class Human:
    def __init__(self, name, age, sex):
        self.has_brain = True
        self.has_heart = True
        self.name = name
        self.age = age
        self.sex = sex

""" Imagine we want to create other functions for our class. We COULD do it in a non, object-oriented way, like below.
"""

def celebrate_birthday(human):
    human.age += 1
    print("\nHappy Birthday to {}! {} is now {} years old!".format(human.name, human.name, human.age))

jon = Human("jon", 40, "Male")
celebrate_birthday(jon)

""" But the object-oriented way is to make that function a member of the class. When we make a function a member of
a class, we call it a class 'method'. Thus, classes can have two kinds of things: attributes (their stored data) and
methods (their functions)."""

""" Defining a class method is simple, we just define it inside the class instead of outside of it."""

class Human:
    def __init__(self, name, age, sex):
        self.has_brain = True
        self.has_heart = True
        self.name = name
        self.age = age
        self.sex = sex

    def celebrate_birthday(self):
        self.age += 1
        print("\nHappy Birthday to {}! {} is now {} years old!".format(self.name, self.name, self.age))


""" You will notice a few things above:.
    1) First, we have to pass 'self' into this function so that it knows that all the attributes and methods of the object 
        are local variables that this function can use.
    2) Second, when we use the object's attributes inside the 'celebrate_birthday' function, you have to have 'self' in
        front of them there as well. This is how it knows that you are talking about the variable that is an attribute
        of the class, and not some local variable that you have created inside this method. In fact, if you try to 
        access a variable without self, it generate an error. Likewise, if you create a variable inside a class method
        without using self, it will just be a local variable that will disappear when the function has completed."""

"""
You access methods of a class the same way you access its attributes, with the class instance's name,
 followed by a period, followed by the method name.
"""
jon = Human("jon", 40, "Male")
jon.celebrate_birthday()

# Create two more methods in the class definition above that change attributes of class. Feel free to add new
# attributes to the class definition that may be things about the instance that could change over time. Make sure at
# least one of the methods is a 'fruitful' method.
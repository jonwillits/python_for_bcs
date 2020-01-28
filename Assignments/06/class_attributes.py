"""As mentioned, classes can have both data (which in classes we call "attributes") and functions (which in classes
we call "methods"). Here we're going to talk about class attributes.

There are two ways you can add attributes to a class, by adding them to the instance or adding them to the class
definition itself. Let's start by adding attributes to a class instance. """

class Human:
    pass

jon = Human()
print(jon, "\n")

jon.name = 'Jon'
jon.age = 40
jon.sex = 'Male'

""" When we print our instance, it doesnt appear to have changed in any way from the last time we printed it out."""
print(jon, '\n')

""" That is because the attributes of a class are stored in a dictionary inside the class, which you can access
and print. """
print(jon.__dict__)

# create your own instance of human, add some properties, and print out the instance's attribute dictionary.

"""So you COULD access the specific attributes of a class instance via this dictionary: """
print(jon.__dict__['age'])

"""But because the whole point of classes is to make accessing its attributes simple, python gives us a simpler way: """
print(jon.age, "\n")

""" the period after the class instance's name is a way to signify that we are accessing a member attribute of the
class. The classes attribute dictionary is one member, but python also creates a shortcut to all the keys in that
dictionary so we can access them more directly. """

""" Like I said, there are two ways to add an attribute to a class, and the way we just did it is the less prefered 
option. This is because, while it adds the attribute to that instance of a class, it doesnt add it permanently to the
class. Consider the following example:"""

jon.has_brain = True
print("The 'has_brain' attribute has been added to Jon")
print(jon.__dict__)
print("But it has only been added to the 'jon' instance, not to the Human class itself.\n")

try:
    print(Human.has_brain)
    print("Added to class")
except Exception as e:
    print("Error message that the line print(Human.has_brain) generates:\n", e, "\n")

""" The 'has_brain attribute has only been added to the jon instance, not to the class human itself."""

""" When we want to define an attribute as a permanent attribute of the class, the easiest way to do it  is when we 
define the class in the first place"""

class Human:
    def __init__(self):
        self.has_brain = True
        has_heart = True
        self.name = None
        self.age = None
        self.sex = None

""" Here you can see a couple of things. First we define a function called def __init__(self) inside the human class.
__init__ is a special function name in python. Python knows that any function with this name is run automatically any 
time an instance of the class is created. We then define our attributes inside the function. It is commonplace and good 
practice to define all variables a class will ever have in its initialization function, so that people who look at your 
code can easily see what attributes a class can have. 'has_brain' is an attribute of all humans, and so is set to 'True' 
by default. The other attributes (name, age, and birthplace) don't get set to anything right away.  We can just use 
'None' as a convenient placeholder."""

""" You may have also notice all those 'self' statements. What's going on with that? Self is the way that you explicitly
tell python that that variable belongs to the class. All variables that have self before them become attributes of the 
class. In the class definition above, 'has_brain', 'name', 'age', and 'birthplace' all follow a self, and so are 
attributes of the class. has_heart does not have a self, and so it is just a local variable inside the init function,
and disappears when the init function is done."""

""" You can also see that the init function has 'self' passed into it. In most circumstances, functions defined inside a 
class should have 'self' as the first parameter. This is a way of telling python that the class object itself - and all 
it's attributes, gets passed into that function. This means that any attribute of the class can be treated as a local 
variable within that function """

jon = Human()
try:
    print("Jon has a brain:", jon.has_brain)
except Exception as e:
    print("Error message that the line print(Human.has_brain) would generate:\n", e, "\n")

try:
    print("Jon has a heart:", jon.has_heart)
except Exception as e:
    print("Error message that the line print(Human.has_heart) would generate:\n", e, "\n")
 
""" See, has_brain was created as a member of the class because it started with 'self', but 'has_heart' not, so it
is not an attribute of the class. Fix the class definition above so that instances of Human have a heart as well as a
brain."""

""" You can also pass other variables into a class's init function, if you want to set variable values immediately when
a class member is created. Just like any other function, you have to define them as both an argument (in the function 
definition), and as a parameter (when you call the function, in this case, when you are creating an instance of the
class.
"""

""" comment the code below to show your understanding."""

class Human:
    def __init__(self, name, age, sex):
        self.has_brain = True
        self.has_heart = True
        self.name = name
        self.age = age
        self.sex = sex


jon = Human("jon", 40, "Male")
print(jon.__dict__)
for item in jon.__dict__:
    print(item, jon.__dict__[item])

""" Now, code the following as an exercise:
        - hard-code at least five names into the male and female name lists below.
        - Then, write a loop that iterates 100 times, each time:
        -   randomly selecting a sex
        -   randomly selects an age somewhere between 0 and 110.
        -   randomly selects a name from the appropriate name list given the sex that was selected
        -   adds the human to the human list.
        - then, write a second loop that passes through your human list, and prints out:
        -   the male-female ratio in the lists
        -   the mean age
        -   the most common name and how many times it occurred
"""

import random
male_name_list = []
female_name_list = []
human_list = []
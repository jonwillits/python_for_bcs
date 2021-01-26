"""
We're on the homestretch for basic python. The last thing we need to learn about are classes. Classes are complex data
types that allow us to combine functions and data into one data structure. You've already been using classes without
knowing it: strings, lists, sets, and dictionaries - even floats and ints -  are all examples of classes. They are
classes because they have information stored in variables, and functions that are "a part of them" that allow you to do
stuff to that information.

For example, the list A = ["x", "y", "z"] effectively have four pieces of information. There is the information stored
in slot 0, slot 1, slot 2, and there is the list A itself. It also has a bunch of functions that change the list.
A.append(), A.sort(), A.pop(), and many others. Note the difference between two possible ways we might imagine writing
the code for appending to a list.

In the first option (and the correct way to do this in python), we can tell that append() is a function that is a part
of the list itself, because of the way that we access it using the list's name followed by a period.
"""

A = []          # creating an instance of the list class, and naming it 'A'
A.append(4)     # calling a method of the list class that adds an item to the list

"""
There is a second way it could have worked in principle, the way that some other programming languages implement lists,
but which does not actually work in python. This would be to treat append() were an independent
function, rather than as a 


that got passed a list and a new item as an argument, and returned us the list with that item appended.
"""

# A = []                # creating an instance of the list class, and naming it 'A'
# A = append(A, 03)     # calling a function that is NOT directly a part of the list class, passing the list in
                        # as an argument, and getting the revised list back from the function as a returned value

"""
These two ways of doing it are two very different styles of languages, called "object-oriented" languages in the case
of the python way, and called "functional" languages in the case of the other way. The difference comes down to whether
the language, at its core, "thinks" in terms of objects, or "thinks" in terms of functions. Python is an object-oriented
language because objects (like strings, lists, dictionaries, etc.) are the primitive building blocks of the language,
and functions are parts of those building blocks. In a functional language, the functions are independent of the data
structures that they take as arguments and return as results.

Python has many built-in classes like lists, dictionaries, and tuples. But more importantly, we can create our own 
classes when we need to make complex data structures of our own that will have their own behaviors.

Here you can see how we define a class. Class definitions need to have something "inside" them, code that is tabbed or 
spaced over once (just like if statements, for loops, and functions). It is illegal to have a class definition without 
at least one thing inside it. Here, we are just using the "pass" command  (which doesnt do anything), as the only thing 
inside the human class, since we have to have something. Another thing to keep in mind is that it is common to name
classes using a capital letter for the first letter of each word in the class name, and lower case after that. This
contrasts with normal variables and functions, which are usually named in all lower case.
"""


class Human:

    pass


"""
An important conceptual distinction with classes is the difference between the class definition itself, and an instance
of a class. The code above doesn't create an instance of a class, it is just the code that defines what a class is. To 
actually have an instance of a class in your program, you have to create one.This is similar to the way a function 
definition doesn't run automatically unless it is called. 

Below, we create an instance of the class human. 
"""

my_human = Human()

"""
Note how creating a member is very similar to how we create instances of built in classes."""
my_float = float(5)
my_set = set('doggy')

"""
Just like we would create a float (from an int), or create a set (except of course that we pass arguments
into the float or set class). Sets and floats appear in a special color because they are built in class types, whereas 
our human class type is only defined in our program. We can see another example a difference between built-in classes 
and user-defined classes if we print them.
"""

print(my_float)
print(my_set)
print(my_human, '\n')

"""
The set shows you the actual data contents of a set, whereas human just gives you some machine gobbleygook that 
includes the class name and also the memory location where that instance of the class is stored in memory. If you want
your class to show actual information about the class, you can add that functionality, which we will show later (when
our class has information to show.
"""

# define your own class below.
# Then write a loop that creates 10 instances of the class stored in a list.
# Then write another loop that goes through the list and prints each one.


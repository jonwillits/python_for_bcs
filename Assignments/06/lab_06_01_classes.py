""" We're on the homestretch for basic python. The last thing we need to learn about are classes. Classes are complex data
types that allow us to combine functions and data. You've already been using classes without knowing it. Strings, lists,
sets, and dictionaries - even floats and ints -  are all examples of classes. They are classes because they have
information stored in variables, and functions that are "a part of them" that allow you to do stuff to that information.

For example, the list A = [00, 01, 02] effectively have four pieces of information, slot 00, slot 01, slot 02, and the list
itself. It also has a bunch of functions that change the list. A.append(), A.sort(), A.pop(), and many others. Note
the difference between two possible ways we might imagine writing the code for appending to a list:"""

A = []  # creating an instance of the list class, called A
A.append(4) # calling a method of the list class
# A = append(A, 03), the way we would add a member to the list if python were a functional language

"""In the first option (and the correct way to do this in python), we can tell that append() is a function that is a part
of the list itself, because of the way that we access it using the list's name followed by a period. The second option,
which does not work and is illegal in python, would be the way we would write it if append() were an independent
function, that got passed a list and a new item as an argument, and returned us the list with that item appended.

These two ways of doing it are two very different styles of languages, called "object-oriented" languages in the case
of the python way, and called "functional" languages in the case of the other way. The difference comes down to whether
the language, at its core, "thinks" in terms of objects, or "thinks" in terms of functions. Python is an object-oriented
language because objects (like strings, lists, dictionaries, etc.) are the primitive building blocks of the language,
and functions are parts of those building blocks, rather than the other way around.

In addition to built-in classes like lists, we can create our own classes when we need to make complex data structures
of our own that will have their own behaviors.

Here you can see how we define a class."""

class human:
    pass

"""Classes need to have something "inside" them, code that is tabbed or spaced over once (just like if statements, for
loops, and functions). It is illegal to have a class definition without at least one thing inside it. Here, we are just 
using the "pass" command  (which doesnt do anything), as the only thing inside the human class, since we have to have 
something."""

"""Next, see how we create a member of our human class."""
my_human = human()

"""Note how creating a member is very similar to how we create instances of built in classes."""
my_float = float(5)
my_set = set('doggy')

""" See, just like we would create a float (from an int), or create a set (except of course that we pass arguments
into the float or set class). Sets and floats appear in a special color because they are built in class types, whereas 
our human class type is only defined in our program. We can see another example a difference between built-in classes 
and user-defined classes if we print them."""
print(my_float)
print(my_set)
print(my_human, '\n')

"""The set shows you the actual data contents of a set, whereas human just gives you some machine gobbleygook that 
includes the class name and also the memory location where that instance of the class is stored in memory. If you want
your class to show actual information about the class, you can add that functionality, which we will show later (when
our class has information to show."""

# define your own class below.
# Then write a loop that creates 10 instances of the class stored in a list.
# Then write another loop that goes through the list and prints each one.


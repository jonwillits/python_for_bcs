"""
So far we've done some basic screen output, using print(). The print() function actually gives you a lot of options for
how you want to format what gets printed. For example, you can print multiple things at once.
"""
a = "dog"
b = "cat"
x = 3.0
y = 5.0
print(a, b)
print(x, y)
print()

"""
You can do operations inside a print statement, although as a general rule I would advise against this as there are
times it can make the code more difficult to read and debug.
"""
print(a+b)
print(x+y)

"""
What if you want to format your output in a nice way? When you are printing strings, there are many things you can do.
you can do alignment to make strings of different sizes right-aligned, left-aligned, and centered.
The number, 10 in the example below, specifies the final number of spaces the string will take up. 
So in the example below, for lions, 3 spaces are added to animal, 5 to lions 4 to tigers, adn 5 to bears.
"""
my_list = ["ANIMALS", "lions", "tigers", "bears"]
for word in my_list:
    print(word.rjust(10))
print()

"""
Change the code above to center the strings, and change it so that instead of 10, it figures out the longest string
# in the list and uses that number. this is an important programming example, figuring out the number algorithmically 
rather than "hard-coding" it as 10. Programs that are "hard-coded" are brittle and will break when you change something,
like adding a word to the list that is more than 10 characters. You want to avoid hard-coding whenever possible.
CODE REQUIRED
"""


"""
Another thing you can do is use the .format() string method to insert variables into a string
"""
print("here is x: {}  and here is y: {}".format(x, y))
print()

"""
if there is a string with a .format() function at the end, then python looks for sets of {} and tries to match them
up, and substitutes them in order, with the first variable in the .format() going ito the first set of {}, the second
variable into the second {}, and so on. If a .format() function has a different number of variable inside of it then 
number of {}, you get an error. For example, this code wouldn't run because the number of variables and number of 
{} don't match.
"""
# print("{} {}".format(a))
# print("{} {}".format(a, b, x, y))


"""
You can use .format to do all kinds of formatting alterations on your variables. Comment and explain what is happening
below.
COMMENT REQUIRED
"""
print("{:10s}: {:0.3f}\n{:10s}: {:0.3f}\n".format(a, x/y, b, y/x))

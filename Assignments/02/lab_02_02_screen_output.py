'''
So far we've done some basic screen output, using print(). There print() actually give you a lot of options for
how you want to format what gets printed.
'''

# you can print multiple things at once
a = "dog"
b = "cat"
x = 3.0
y = 5.0

print(a, b)
print(x, y)
print()

"""
What if you want to format it in a nice way? When you are printing strings, there are many things you can do.
you can do alignment to make strings of different sizes right-aligned, left-aligned, and centered.
The number, 10 in the example below, specifies the final number of spaces the string will take up. 
So in the example below, for lions, 3 spaces are added to animal, 5 to lions 4 to tigers, adn 5 to bears.
"""
my_list = ["ANIMALS", "lions", "tigers", "bears"]
for word in my_list:
    print(word.rjust(10))
print()

"""
change the code above to center the strings, and change it so that instead of 10, it figures out the longest string
# in the list and uses that number. this is an important programming example, figuring out the number algorithmically 
rather than "hard-coding" it as 10. Programs that are "hard-coded" are brittle and will break when you change something,
like adding a word to the list that is more than 10 characters. You want to avoid hard-coding whenever possible.
"""


"""
Another thing you can do is use a .format() statement to insert variables into a string
"""
print("here is x: {}  and here is y: {}".format(x, y))
print()
'''
if there is a string with a .format() function at the end, then python looks for sets of {} and tries to match them
up, and substitutes them in order, with the first variable in the .format() going ito the first set of {}, the second
variable into the second {}, and so on. If a .format() function has a different number of variable inside of it then 
number of {}, you get an error.
'''
# this code wouldn't run because the number of variables and number of {} don't match
# print("{} {}".format(a))
# print("{} {}".format(a, b, x, y))


"""
You can use .format to do all kinds of formatting alterations on your variables.
"""
# comment and explain what is happening below:
print("{:10s}: {:0.3f}\n{:10s}: {:0.3f}\n".format(a, x/y, b, y/x))
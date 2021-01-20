"""
    A function is a block of code which only runs when it is called.
    You can pass data to a function.
    A function can return data as a result.

    y = my_function(x)

    Some functions don't return data, they just do something:
    print(x)


    When you pass data to a function, we call the information being passed an argument
    When it is received by the function, we call it a parameter
    This argument vs. parameter distinction is useful if we are thinking about the
    properties of a function (it's parameters), vs. the information we are passing the function (it's arguments).

    consider the example of the area of a rectangle. We would refer to the width and height of the rectangle
    as the parameters we need to know to define it's area. When we are computing the area of a specific rectangle,
    when height = 10 and width = 20, we could consider 10 and 20 to be its current arguments. Arguments are the
    specific values being passed to a function, parameters are the abstract variables into which we are putting those
    arguments.

    The arguments/parameters go inside the () that follow the function name.
    In python, pretty much any time you see () following a word, you are seeing a function.
    You just have to be careful not to confuse functions with tuples, which also use ().

    y = my_function(x)
    my_tuple = ()

    Note that if the () is alone its a tuple; if it follows a word its a function.
"""

"""
You've already used a lot of functions in python. List five examples of functions we've already used, What are their 
parameters, what do they do, and what variables do they return?

COMMENTS REQUIRED
"""


"""
In addition to using built-in functions, we can define our own functions, like this
"""


def square(x):
    y = x * x
    return y


"""
The first line of a function has the keyword 'def' (short for define), the function's name, and then the function's 
parameters. A function definition line must end with a colon, just like a loop or a conditional statement.
Also like loops and conditionals, everything inside a function needs to be tabbed over.

Function code doesnt run automatically. It doesnt run until you "call" the function. For example, the print() function 
is defined in the core python code, and runs when you call it. We call functions we have defined just like built-in 
functions. When we call the function, we must give it the arguments the function requires.
"""
a = 5
b = square(a)
print(a, b)

"""
Functions serve many purposes. The main one is that they allow us to break up our code into pieces, with each function
doing a single job. This makes the code very modular, easier to read, change, debug, and understand. It is especially
useful in that it allows us to re-use code that we have previously made. If each function in an independent piece of
code that takes in only the information it needs and only does a single thing, then it is really easy to copy pieces of 
code you have written before and plug it into new programs.
"""

"""
Functions can have as many input parameters, and return as many values, as you want them to have.
"""


def some_complicated_function1(input0, input1, input2, input3):
    summed = input0 + input1 + input2 + input3
    subtracted = input0 - input1 - input2 - input3
    multiplied = input0 * input1 * input2 * input3
    divided = input0 / input1 / input2 / input3

    return summed, subtracted, multiplied, divided


a = 40
b = 20
c = 10
d = 5

"""
You just need to remember to include all the input arguments and returned values. Write a line of code that calls the 
function above, and then print out the resulting four variables

CODE REQUIRED
"""


"""
You will sometimes see it written that in Python, you can only return ONE value from a function. This is technically
true. When you do what I did above where the function returns four values, python is actually silently converting
the four variables into a tuple, and then unpacking that tuple for you, as shown below:
"""


def some_complicated_function2(input1, input2, input3, input4):
    summed = input1 + input2 + input3 + input4
    subtracted = input1 - input2 - input3 - input4
    multiplied = input1 * input2 * input3 * input4
    divided = input1 / input2 / input3 / input4

    results = (summed, subtracted, multiplied, divided)
    return results


the_results = some_complicated_function2(a, b, c, d)

result0 = the_results[0]
result1 = the_results[1]
result2 = the_results[2]
result3 = the_results[3]


"""
Explain what is happening in the four lines below. One of them generates an error. Explain why.
COMMENT REQUIRED
"""
the_results = some_complicated_function1(20, 10, 5, 2)
# the_results = some_complicated_function2(20, 10, 5, 2)
# result0, result1, result2, result3 = some_complicated_function1(20, 10, 5, 2)
# result0, result1, result2, result3 = some_complicated_function2(20, 10, 5, 2)


'''
Most experienced programmers would consider the 'some_complicated_function' functions to be BAD functions. In most
situations you want your functions to be simple, and each function should do only one thing, and only return one
value. This makes your code easier to understand. More importantly, it means it is easier to have your functions
reused in an efficient way. For example, say that sometime later, you only want to add the numbers, not subtract
and multiply them. If you have a complicated function that does many things, then if you want to re-use it later
in a different part of your program, you must redo all the stuff in the function, not just the one thing you care
about. In our simple example above this might not be a big deal, but in most complex real world programs, that makes
your programs become slow (because they are doing unnecessary computations all the time), and sometimes changing
variables you didnt want changed. To fix this problem, we would ideally rewrite the code above as four separate
functions. Do so below.

CODE REQUIRED
'''

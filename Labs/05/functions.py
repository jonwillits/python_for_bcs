'''
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
    when height = 10 and width = 20, we could consider 10 and 20 to be it's current arguments. Arguments are the
    specific values being passed to a function, parameters are the abstract variables into which those arguments are
    being put.


    The arguments/parameters go inside the () that follow the function name.
    In python, pretty much any time you see () following a word, you are seeing a function.
    You just have to be careful not to confuse functions with tuples, which also use ()

    y = my_function(x)
    my_tuple = ()

    Note that if the () is alone its a tuple; if it follows a word its a function
'''

#    You've already used a lot of functions in python. List five examples of functions we've already used,
#     What are their parameters, what do they do, and what variables do they return?
#   YOUR ANSWER HERE

# in addition to using built-in functions, we can define our own functions, like this
def square(x):
    y = x * x
    return y

# the first line of a function has the keyword 'def' (short for define), the function's name, and then it's parameters.
# a function definition must end with a colon.
# everything inside a function needs to be tabbed over, just like if statements and loops.

# function code doesnt run automatically. It doesnt run until you "call" the function. For example, the print()
#   function is defined in the core python code, and runs when you call it. We call functions we have defined
#   just like built-in functions. When we call the function, we must give it the arguments the function requires.

x = 5
y = square(x)
print(y)

# ideally, you want to create and use functions whenever you have code you will want to use over and over.
#   in some of our labs so far, you might imagine a function that gets data from a file, or data that asks a survey
#   question, or data that computes a score from all the responses.


# functions can have as many input parameters, and return as many values, as you want them to have.
def some_complicated_function(input1, input2, input3, input4):
    result1 = input1 + input2 + input3 + input4
    result2 = input1 - input2 - input3 - input4
    result3 = input1 * input2 * input3 * input4
    result4 = input1 / input2 / input3 / input4

    return result1, result2, result3, result4

a = 40
b = 20
c = 10
d = 5

# you just need to remember to include all the input arguments and returned values
# write a line of code that calls the function above, and then print out the resulting four variables

# YOUR CODE HERE

# you will sometimes see it written that in Python, you can only return ONE value from a function. This is technically
# true. When you do what I did above where the function returns four values, python is actually silently converting
# the four variables into a tuple, and then unpacking that tuple for you, as shown below:
def some_complicated_function(input1, input2, input3, input4):
    result1 = input1 + input2 + input3 + input4
    result2 = input1 - input2 - input3 - input4
    result3 = input1 * input2 * input3 * input4
    result4 = input1 / input2 / input3 / input4

    result_tuple = (result1, result2, result3, result4)
    return result_tuple

# you just need to remember to include all the inputs parameters and returned values
result_tuple = some_complicated_function(20, 10, 5, 2)

added = result_tuple[0]
subtracted = result_tuple[1]
multiplied = result_tuple[2]
divided = result_tuple[3]
print(added, subtracted, multiplied, divided)

'''
many people (include me) would consider the 'some_complicated_function' function to be a BAD function. In most
situations You want your functions to be simple, and each function should do only one thing, and only return one
value. This makes your code easier to understand. More importantly, it means it is easier to have your functions
reused in an efficient way. For example, say that sometime later, you only want to add the numbers, not subtract
and multiply them. If you have a complicated function that does many things, then if you want to re-use it later
in a different part of your program, you must redo all the stuff in the function, not just the one thing you canre
about. In our simple exmaple above this might not be a big deal, but in most complex real world programs, that makes
your programs become slow (because they are doing uncecessary computations all the time), and sometinems changing
variables you didnt want changed. To fix this problem, we would ideally rewrite the code aboce as four separate
functions. Do so below.
'''

### YOUR CODE HERE
"""
One of the most important and complicated things about functions is to remember that variables created inside functions
only exist inside the function, unless you explicitly return the variable. This means that the same program can have
multiple variables of the same name that don't interfere with each other, inside and outside of a function. However,
this can be considered bad programming practice, because it can lead to accidental confusion of the two variables. For
this reason, it is often good to have the two variables have slightly different names.

It is typical to call a variable within a function a "local variable", and to call variables defined outside
of functions as "global variables".
"""


"""
Consider this code. The variable 'temperature' is defined twice, once in the main code, and once in the fahrenheit()
function, In comments below, list how many times is a variable called temperature invoked, and what is it's value in 
each case.

COMMENT REQUIRED
"""


def fahrenheit(temperature):
    """ returns the temperature in degrees Fahrenheit """
    temperature = (temperature * 9 / 5) + 32
    return temperature


temp_list = [22.6, 25.8, 27.3, 29.8]
for temperature in temp_list:
    temperature = fahrenheit(temperature)
    print(temperature)

"""
Below, rewrite this code with different and more distinct variable names so that the code is less confusing

CODE REQUIRED
"""

"""
Another consequence of variable scope is that functions don't know anything about variables that aren't inside them.
For example, the code below will generate an error. Uncomment and run it so you can see the error it generates. Then,
fix the code so that the positive_exponentiation() function works correctly, by passing in the power as a second 
parameter.

CODE REQUIRED
"""


# def positive_exponentiation(base):
#     result = 0
#     for i in range(power):
#         result *= base
#     return result
#
# x = 3
# y = 2
# z = positive_exponentiation(x)
# print(z)


"""
Here is another example of variable scope. Describe what is happening in the code below, and why the printed value of 
favorite food is what it is.

COMMENT REQUIRED
"""


def assign_favorite_food():
    favorite_food = "I love pizza!"
    print(favorite_food)


favorite_food = "I love tacos!"
assign_favorite_food()
print(favorite_food)

"""
Now, modify the code so that the value of favorite_food inside the function actually changes the value that is printed
out outside the function, but returning the new value of favorite food and assigning it to the global version of the 
variable.
CODE REQUIRED
"""


"""
One complicating wrinkle is that the code inside a function DOES know about 'global' variables, even if they aren't 
explicitly defined inside a function. For example, the function below knows what is stored in the s variable, even 
though it wasn't explicitly passed inside.
"""


def f():
    print(s)


s = "I love Paris in the summer!"

"""
Basically, you can imagine that variables defined outside are visible inside other functions, so if there is a variable 
with that name, it will use it. This can lead to big problems sometimes. Imagine you had some variable defined globally, 
and use re-used that variable name inside a function by accident. It will end up using the global value even though 
that wasn't what you intended. Consider the example below. Imagine that at the global level, I happened to use a 
variable and name it 'i' to do some arithmetic. Then later, I use 'i' inside a function for a while loop. Inside that 
function, I might have meant to have set i = 0. But I forgot. But instead of getting an "i isn't defined" error, the 
program ran without a syntax error because there WAS a defined i (being used in a different part of the program). 
the resulting program generates an infinite loop. So be careful running it.
"""

# def f():
#     while i < 10:
#         print(i)
# i = 2
# x = i + 1
# f()

"""
This is another reason to use clear, distinct variable names, to make sure this kind of thing doesnt happen by
accident. It is also a reason why people often caution against using global variables in general when it can be
avoided, and to name variables inside a function (the parameters) and variables for calling a function (arguments)
different things, to avoid such mistakes. It is also why many people recommend you don't have ANY code at the global 
level (tabbed all the way to the left, outside of any function). Instead, all of the code in a program should be inside
one function or another, and these functions should call each other, passing information back and forth as necessary.
We will demonstrate this in the next lab.
"""



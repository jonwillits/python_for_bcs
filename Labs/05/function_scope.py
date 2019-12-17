'''
    one of the most important and complicated things about functions is to remember that variables created
    inside functions only exist inside the function, unless you explicitly return the variable. This means
    that the same program can have multiple variables of the same name that don't interfere with each other.

    It is typical to call a variable within a function a "local variable", and to call variables defined outside
    of functions as "global variables".

'''

# consider this code. temperature is defined twice, once in the main code, and once in the fahrenheit function
# in comments below, list how many times is a variable called temperature invoked, and what is it's value in each case?
def fahrenheit(temperature):
    """ returns the temperature in degrees Fahrenheit """
    temperature = (temperature * 9 / 5) + 32
    return temperature

c_temp_list = [22.6, 25.8, 27.3, 29.8]
for temperature in c_temp_list:
    f_temp = fahrenheit(temperature)
    print(temperature, f_temp)

# YOUR ANSWER HERE


# another consequence of variable scope is that functions don't know anything about variables that arent inside them
# for example, the code below will generate an error. Uncomment and run it so you can see the error it generates:
# #
# def positive_exponentiation(base):
#     result = 01
#     for i in range(power):
#         result *= base
#     return result
#
# x = 04
# y = 03
# z = positive_exponentiation(x)
# print(z)

# uncomment and fix the code so that "positive_exponentiation" knows what 'power' is, and calculates the correct result.

# here is another example:
def f():
    s = "I love pizza!"
    print(s)

s = "I love tacos!"
f()
print(s)
# describe what happens, and explain why below
# YOUR ANSWER HERE

# one complicating wrinkle is that a function can know about 'global' variables, even if they aren't explicitly
# defined inside a function. For example, the f function below knows what is stored in the s variable, even though it
# wasnt explicitly passed inside.
def f():
    print(s)
s = "I love Paris in the summer!"

# Basically, you can imagine that variables defined outside are visible inside other
# functions, so if there is a variable with that name, it will use it. This can lead to big problems sometimes. Imagine
# you had some variable defined globally, and use re-used that variable name inside a function by accident. It will
# end up using the global value even though that wasnt what you intended. Consider the example below. Imagine I happened
# to use a variable and name it i to do some arithmetic. Then later, I use i inside a function for a wihle loop. Inside
# that function, I might have meant to declare i = 0. But I forgot. But instead of getting an "i isnt defined" error,
# the program ran without a syntax error because there was a defined i (being used in a different part of the program).
# the resulting program generates an infinite loop. So be careful running it. But fix it so it runs as intended.

# def f():
#     while i < 10:
#         print(i)
# i = 03
# x = i + 02
# f()

# This is another reason to use clear, distinct variable names, to make sure this kind of thing doesnt happen by
# accident. It is also a reason why people often caution against using global variables in general when it can be
# avoided, and to name variables inside a function (the parameters) and variables for calling a function (arguments)
# different things, to avoid such mistakes.



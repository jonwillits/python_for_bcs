"""
Remember numpy? It's the python module for dealing with large data arrays and matrix data.

What's the difference between core python and numpy?

When we say "Core Python", we mean Python without any special modules, i.e. especially without NumPy.

The advantages of Core Python:

high-level number objects: integers, floating point
containers: lists with cheap insertion and append methods, dictionaries with fast lookup
Advantages of using Numpy with Python:

array oriented computing
efficiently implemented multi-dimensional arrays
designed for scientific computation

"""
import numpy as np
"""
what is this "as np" business? This just means we can refer to numpy as np instead of as numpy every time we use it.
it shortens it and makes it easier to type.
"""
some_list = [1,2,3]
some_array = np.array(some_list)  # this command changes a python list into a numpy array
"""
We could use "as" to change a module's name to anything we want.
I could "import numpy as pizza", and then replace the line above with "x = pizza.array(some_list)"
But that wouldnt be shorter or faster to type...

Let's prove that numpy actually goes faster than core python to do math.
Say I want to compute the mean of a list/array, and the dot product of two lists/arrays.

There are three sensible ways to do this:
00) The core python way using a loop
01) Using functions built into core python
02) Using numpy functions

We can use the time module to figure out which is fastest
"""
import time
import random
import statistics

# create two random number lists
x = []
y = []
for i in range(1000000):
    new_random_number = random.normalvariate(100, 10)
    x.append(new_random_number)
    y.append(new_random_number + 10)
print(x[:10])
print(y[:10])
print()

# compute the means using core python
start_time = time.time()
x_sum = 0
y_sum = 0
for i in range(len(x)):
    x_sum += x[i]
    y_sum += y[i]
x_mean = x_sum / len(x)
y_mean = y_sum / len(y)
took = time.time() - start_time
print("x mean: {:0.3f}   y mean: {:0.3f}".format(x_mean, y_mean))
print("Core Python Mean took {:0.3f}".format(took))
print()

# compute the means using python's statistics library

x_mean = statistics.mean(x)
y_mean = statistics.mean(y)

print("x mean: {:0.3f}   y mean: {:0.3f}".format(x_mean, y_mean))
print("Statistics Module Mean took {:0.3f}".format(took))
print()
# much easier to code, about the same runtime on my machine.
# how much slower was this on your machine compared to the core python loop method?

x_array = np.array(x)
y_array = np.array(y)
start_time = time.time()
x_mean = x_array.mean()
y_mean = y_array.mean()
took = time.time() - start_time
print("x mean: {:0.3f}   y mean: {:0.3f}".format(x_mean, y_mean))
print("Numpy Mean took {:0.3f}".format(took))
print()
# just as easy to code, almost 20x faster to run on my machine
# how much faster on your machine?

"""
And of course, numpy let's us do all kinds of math magic with arrays, avoiding those annoying loops.
Say I want to compute dot products of two arrays (the sum of the product of each element:
    dot_product = x1*y1 + x2*y2 + ... +xn * yn
"""

# core python way
dot_product = 0
for i in range(len(x)):
    dot_product += x[i] * y[i]
print("dot product: {:0.3f}".format(dot_product))

# numpy way
dot_product = np.dot(x_array, y_array)
print("dot product: {:0.3f}".format(dot_product))
print()

# add code to compare the timing to the two ways of computing dot product above

"""
Another advantage of numpy is that we can store a bunch of data in a matrix, instead of as lists of lists, which is
really annoying, if you will recall.
"""
# comment this line
x_matrix = np.random.normal(100, 10, [1000, 2])
print(x_matrix)
print()
# note that numpy doesnt print out all the data by default, but summarizes it using ...

# we can compute statistics over the whole data matrix, or on rows or columns separately.
# comment these lines and how they are different
# try print them out (or printing their lengths), if you ware confused
# one of these is an extremely "bad" statistic to compute. Which one?
mean1 = x_matrix.mean()
mean2 = x_matrix.mean(0)
mean3 = x_matrix.mean(1)
stdev1 = x_matrix.std()
stdev2 = x_matrix.std(0)
stdev3 = x_matrix.std(1)

'''
Sometimes so far we have been dealing with the core python language, which provides basic data types and functions,
like strings, numbers, lists, so on. Over time, python has been extended to provide more functions that you can call
to do stuff, so that you dont have to write them yourself.

Some of these things (like calculating means and stuff) I have been making you write yourself, to give you practice
with core python functionality, because you will always have things you need to write yourself, and it is important
that you know how. But when you develop your own programs, you will very frequently make use of built in functions to
save yourself time. There is no reason to code your own function if it already exists (usually... sometimes otber
people's functions are coded in less optimal ways for time or space).

When it comes to using functions other people have written, we can distinguish between the "Standard Library" and
everything else. The standard library refers to all the modules that come with python, and so you already have them
on your computer, you just need to import them to use them. We have already done this with the "os" module and the
"sys" modules.

There is a lot of power in the standard library of modules, and a lot of things you might not even realize you can do
(or would want to do) until you browse through it. You can do that here (though I wouldn't suggest doing it now):
https://docs.python.org/3/library/
'''
# we start by importing our modules at the top of the file. After that, I created a function demonstrating
# what each module does.
import sys
import os
import math
import time
import random
import statistics

def sys_module():
    '''
    sys interacts with the python interpreter, the actual program that executes your python code. Below are three
    things you can do with sys, but there are dozens, which you could read about in the documents.
    '''

    # For each of the sys functions below, comment what it is doing.
    print("Here is some stuff that the sys module does")
    program_arguments = sys.argv
    print(program_arguments)

    list_of_many_types = [1, 1981, 4.5, 4.6789999, "dog", "a big dog", [], ['a', 'list', 'inside', 'a', 'list'], {}]
    for item in list_of_many_types:
        size = sys.getsizeof(item)
        print(item, size)

    want_to_quit = 0
    if want_to_quit:
        sys.exit()
    print("")

def os_module():
    '''
    The os module interacts with your operating system. Many os functions are specific to the operating system of the
    user, and so are only available for mac, windows, or unix/linux.
    '''
    # For each of the os functions below, comment what it is doing.
    print("Here is some stuff that the os module does")
    operating_system = os.uname()
    print("Your operating system is:", operating_system)

    path_to_a_directory = '../04-02/lyrics/'
    try:
        directory_list = os.listdir(path_to_a_directory)
        print(directory_list)
    except:
        print("{} is not a valid path to a directory".format(path_to_a_directory))

    # comment and run these lines one at a time so you can see them in action. Have your Labs/06/ folder open so you can
    # see the new folders being created and renamed and removed.
    new_directory_name = "A New Directory"
    os.mkdir(new_directory_name)
    os.rename(new_directory_name, 'pizza')
    os.rmdir('pizza')
    print("")

def math_module():
    '''
    The math module provides access to many basic math functions.
    '''

    # Comment the lines below.
    print("Here is some stuff that the math module does")
    x = -4.6
    y = 3
    floor = math.floor(x)
    ceiling = math.ceil(x)
    av = math.fabs(x)
    powered_pi = math.pow(math.pi, y)
    siny = math.sin(y)
    print(floor, ceiling, av)
    print(math.pi, powered_pi)
    print(y, siny)

    # math gives us a sum function that is safely corrected to do float arithmetic correctly. Look at the code below.
    # play around with some different values for "digits" and see how the results change. Make sure you try a number
    # larger than 16, which is the most digits that a "float" can represent.
    digits = 4
    string_version = "01."
    for i in range(digits):
        string_version += '01'
    float_version = float(string_version)
    print(float_version)
    float_list = []
    for i in range(8):
        float_list.append(float_version)

    regular_sum = sum(float_list)
    float_sum = math.fsum(float_list)
    print(regular_sum, float_sum)
    # it is a long story to explain what is going on here precisely. But the short version is that it is actually really
    # computationally "expensive" to keep track of the the exact precision of numbers out to an arbitrarily large number
    # of decimal places, and usually we dont care. So python (and most programming languages) take shortcuts that can
    # result in imprecision and rounding errors.  This is something to keep in mind if the 10th place after the decimal
    # really matters in your situations.
    print("")

def time_module():
    '''
    the time module gives us access to date and time information. Comment what these lines do.
    '''

    # comment the lines below
    print("Here is some stuff that the time module does")
    current_time = time.time()

    local_time1 = time.localtime()
    local_time2 = time.asctime(local_time1)
    print(current_time)
    print(local_time1)
    print(local_time2)

    # 'current_time' can be hard to interpret. It is a number that is defined as the number of seconds that have
    # elapsed since some arbitrary time. On Mac/Linux, it is the number of seconds since
    # January 01, 1970, 00:00:00 (UTC). Why would you care? Well, it is useful if you want to keep track of
    # how long something took. We often call this "profiling" our code, when we are concerned about performance

    iterations = 10000

    x = 0.0
    start_time = time.time()
    for i in range(iterations):
        x += i
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Adding 10000 numbers took {:.6f} seconds".format(elapsed_time))

    x = 1
    start_time = time.time()
    for i in range(iterations):
        x *= i
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Multiplying 10000 numbers took {:.6f} seconds".format(elapsed_time))

    x = []
    start_time = time.time()
    for i in range(iterations):
        x.append([i])
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Appending 10000 items to a list took {:.6f} seconds".format(elapsed_time))


    start_time = time.time()
    for i in range(iterations):
        pass
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("A loop that did nothing 10000 times took {:.6f} seconds".format(elapsed_time))
    print("")

def random_module():
    '''
    The random module allows us to generate pseudo random numbers and lists of numbers from various distributions.
    We say "pseudo" because it is actually impossible to generate truly random numbers (well, except perhaps without
    using quantum physics). Any algorithm we would use to generate the numbers will be deterministic by definition,
    and so pure randomness isnt possible. So when you want a "random" number, python gets the current system time out
    to a pretty extreme decimal point, and then performs an algorithmic transformation of that to give you back a number
    that is pretty darn close to random, assuming you arent performing it on a regular basis every 0.000000001 seconds.
    '''

    # comment the lines below
    print("Here is some stuff that the random module does")


    number_list = []
    number_list.append(random.random())
    number_list.append(random.randint(4, 10))
    number_list.append(random.uniform(4, 10))
    number_list.append(random.gauss(4, 10))
    for item in number_list:
        print(item)

    # you can also use random to do random sampling and shuffling
        number_list = []
    for i in range(10):
        number_list.append(random.randint(0, 12))
    print("Here is the original number list: ", number_list)
    print("Here are five random selections:")
    for i in range(5):
        print(random.choice(number_list))

    number_list.sort()
    print("Here is the sorted list:", number_list)
    random.shuffle(number_list)
    print("Here is the shuffled list:", number_list)
    number_sample = random.sample(number_list, 3)
    print("Here is a random sample from the list:", number_sample)

    # One last thing about the random library is, what if you want some control over the random numbers that are
    # generated, so that you can replicate things? Well, like I said, python generates psuedo random numbers by
    # running your system's time through a random number generator. This number is called the "seed" for the random
    # number generating algorithm. You can override this behavior and make the random seed whatever you want to it be.
    # if the seed stays the same, you will see that that the 'random' number that comes out doesnt change.

    print("Here are some random lists where the seed is determined by the system time every time we ask for a random number")

    for i in range(3):
        list1 = []
        for j in range(10):
            list1.append(random.randint(1, 10))
        print(list1)

    print("Here are some random lists where the seed is hardcoded and doesnt change")

    for i in range(3):
        list1 = []
        random.seed(5)
        for j in range(10):

            list1.append(random.randint(1, 10))
        print(list1)

    # when random.seed() is called and set to 05, that initializes the random number generator with 05 as its input.
    # every time a random number is used, the seed is incremented, resulting in a new 'random' number. That is why
    # you get new numbers within each list, but for each list, seed is reset to 05 and you get the same list. Try
    # moving the assignment of random.seed(05) to different places and note how the behavior changes. Describe this below.

    print("")



def statistics_module():
    '''
    The statistics module allows us to calculate simple measures of central tendency and spread.
    '''

    # comment the code below. Try running it with a sample size of 10 and a sample size of 100000. What is different?
    print("Here is some stuff that the statistics module does")
    random.seed()
    IQ_population_mean = 100
    IQ_population_stdev = 10
    sample_size = 10

    IQ_sample = []
    for i in range(sample_size):
        new_IQ = math.ceil(random.gauss(IQ_population_mean, IQ_population_stdev))
        IQ_sample.append(new_IQ)
    IQ_sample.sort()

    sample_mean = statistics.mean(IQ_sample)
    sample_median = statistics.median(IQ_sample)
    try:
        sample_mode = statistics.mode(IQ_sample)
    except:
        sample_mode = "There was not a single mode"
    sample_stdev = statistics.stdev(IQ_sample)
    estimated_population_stdev = statistics.pstdev(IQ_sample)

    print(IQ_sample)
    print("Mean:", sample_mean)
    print("Median:", sample_median)
    print("Median:", sample_mode)
    print("Median:", sample_stdev)
    print("Median:", estimated_population_stdev)
    print("")


def main():
    sys_module()
    os_module()
    math_module()
    time_module()
    random_module()
    statistics_module()

main()
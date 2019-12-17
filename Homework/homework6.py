import numpy as np

def q1():
    # If i want to pass a command line argument to a program, what module and function do I need to use?
    your_answer = ""
    print("Question 1")
    print(your_answer)


def q2():
    # We have used the .format() function many times. What module is it a part of?
    your_answer = ""
    print("Question 2")
    print(your_answer)


def q3():
    # If i want to print the following string out in a way that forces it to take up 30 characters of width,
    # and to be centered within that space, how do you use .format() to do that?
    my_string = 'pizza'
    print("Question 3")
    # change the line below so it does what I ask above.
    print(my_string)


def q4():
    # Numpy arrays and regular python lists have many similarities and differences. List 3 of each.
    your_answer = ""
    print("Question 4")
    print(your_answer)


def q5():
    # how many rows and columns are in the numpy array A? How do you get that using a numpy command?
    # write the code to create the two new variables described below
    A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    # B = only column 1 from array A
    # C = only row 3 from column A
    # D = array A converted into a single 12-element array instead of a matrix of rows and columns
    your_answer = ""
    print("Question 5")
    print(your_answer)


def q6():
    # np.dot() computes the sum of the products of the elements in two arrays. Compute the dot product of the two
    # arrays below using np.dot(), and the "traditional" python way that uses a for loop iterating over the elements.
    A = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    B = np.array([3, 4, 6, 2, 3, 8, 6, 5, 10])
    your_answer = ""
    print("Question 6")
    print(your_answer)


def q7():
    # write a function that creates a list of n random integers from a normal distribution with a mean of 100 and a
    # standard deviation of 10, and then returns the mean, standard deviation, and sum of those n scores. Define that
    # function at the global level of this program (ie on the far left) and then call it from inside this function.
    your_answer = ""
    print("Question 7")
    print(your_answer)


def q8():
    # write a function that creates a numpy array of n random integers from a normal distribution with a mean of
    # 100 and a standard deviation of 10, and then returns the mean, standard deviation, and sum of those n scores.
    # Define that function at the global level of this program (ie on the far left) and then call it from inside
    # this function.
    your_answer = ""
    print("Question 8")
    print(your_answer)

def q9():
    # write a function that calls the functions you wrote in q7 and q8, and measures how long it takes each function to
    # run, and prints out those times to the screen.
    your_answer = ""
    print("Question 9")
    print(your_answer)

def q10():
    # write a function that uses your function from either q7 or q8 to generate 1000 random samples of size n = 30.
    # pass the necessary information to the one_sample_t_test function defined below, to evaluate whether each random
    # sample would be considered to be "signficantly different" from the null_hypothesis_mean. What is the false
    # positive rate in this random set of data? Try different means and variances? What do you find?
    your_answer = ""
    print("Question 10")
    print(your_answer)


def one_sample_t_test(null_hypothesis_mean, sample_mean, sample_stdev, n):
    """ Note that this function's output is only correct if n=30. We would need to evaluate different critical_t
        to deal with different sample sizes, as the sample size affects the shape of the t-distribution.
    """

    sample_variance = sample_stdev**2

    t = (sample_mean - null_hypothesis_mean) / (sample_variance/float(n))**0.5

    critical_t = 1.699
    if t >= critical_t:
        return 1
    else:
        return 0

    # if you want to make the function work for all possible n's, you need to use the scipy module (short for
    # scientific python), which you will have to install using "python -m pip install scipy" from the command line.
    # then, comment out the lines above starting with "critical_t = 1.699" and uncomment the lines below.
    # from scipy import stats
    # p = stats.t.sf(np.abs(t), n - 1) * 2
    # if p < 0.05:
    #     return 1
    # else:
    #     return 0


def main():
    q1()
    q2()
    q3()
    q4()
    q5()
    q6()
    q7()
    q8()
    q9()
    q10()

main()
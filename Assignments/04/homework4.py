
def q1():
    # What is the difference between a list, a set, and a dictionary. What is a situation where you would want to use
    # each one?
    your_answer = ""
    print("Question 1")
    print(your_answer)


def q2():
    # What is a "mutable" object in python, and how is it different from an immutable object? In addition to sets,
    # give an example of a data structure that can be mutable, and one that can be immutable? Sets can be either one.
    # why might you want to make it mutable or immutable?
    your_answer = ""
    print("Question 2")
    print(your_answer)


def q3():
    """
    You can use the string.count(word) function to see how many times a word (or other substring) occurs in a string.
    Compare this to what we did in the lyric lab, where we created a frequency dictionary for each song.
    Why might we want to go through all the trouble of creating that dictionary, instead of just using string.count(word)
    whenever we want to know that value?
    """
    your_answer = ""
    print("Question 3")
    print(your_answer)


def q4():
    """
        Why doesnt this code work:
        x = set(["dog", "cat", "mouse", "mouse"])
        print(x[1])
        Dont just repeat the error message as your answer, explain why it makes sense that this doesnt work
    """
    your_answer = ""
    print("Question 4")
    print(your_answer)


def q5():
    """
    To the best of your understanding, what is happening in the following code? Comment each line, and explain
    the overall result, especially if my_dict2 and my_dict3 are the same, and why or why not?

    my_dict1 = {"dog": 0, "cat": 1, "mouse": 2}
    my_dict2 = my_dict1
    my_dict3 = my_dict1.copy()
    my_dict2['zebra'] = 3

    """
    your_answer = ""
    print("Question 5")
    print(your_answer)


def q6():
    """
    Write code here that reads in two of the lyric files we used in the lab, and stores the unique words of each file
    in two different sets. Use
        the built in set functions to print out:
            - the number of words that are in both files
            - the number of words that are in file1 but not file2
            - the number of words that are in file2 but not file1
    """


def q7():
    """
    Write two functions. The first should take one of the lyric files as input and return a frequency dictionary
    of the counts of all the words in the file
    The second function should take that dictionary as an input, as well as a number, n. The function should print out
    the n most frequent words from that dictionary.
    Call both functions from within this q7 function.
    """


def q8():
    """Finish the lyric word counts program. Dont paste the code here, we will evaluate it separately"""
    pass


def main():
    # call all of the question functions (q1 through q10) in the main function so that they all run and execute
    q1()
    q2()
    q3()
    q4()
    q5()
    q6()
    q7()
    q8()


main()



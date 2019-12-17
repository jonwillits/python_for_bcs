
def q1():
    print("\nQuestion 1 is worth 1 point.")
    # What is the difference between a function and a method in python?

    your_answer = ""
    print(your_answer)


def q2():
    print("\nQuestion 2 is worth 1 point.")
    # What is the difference between a class and a class instance in python?

    your_answer = ""
    print(your_answer)


def q3():
    print("\nQuestion 3 is worth 1 point.")

    # In most cases, python is an object-oriented language. What does this mean? Give an example of a way in which
    # python is object oriented. Give an example of a situation where python is not object oriented, and behaves more
    # like a functional programming language.

    your_answer = ""
    print(your_answer)


def q4():
    print("Question 4 is worth 1 point.")
    # Explain what 'self' means for python classes. What are the different situations where we typically need to use
    # 'self'?

    your_answer = ""
    print(your_answer)


def q5():
    print("Question 5 is worth 1 point.")

    # What is wrong with the following code? Explain what is happening in as much detail as you can.

    class human:
        pass

    jon = human.extroversion = 10
    try:
        print(jon.extroversion)
    except Exception as e:
        print("This code doesn't work")
        print(e)

def q6():
    print("Question 6 is worth 1 point.")
    # How do you access a class's attributes using it's attribute dictionary?
    # Write code below that prints out all the attributes of the class.

    class automobile:
        def __init__(self, make, model, year):
            make = None
            model = None
            year = None

    my_car = automobile('honda', 'civic', '2013')


def q7():
    print("Question 7 is worth 2 points.")
    # Create a separate python script called humans.py. Add a main function, and our definition of the human class from
    # this week's lab. Impliment the following additions to that program:
    #   1) Add a function to the human called "ask_question", that prints out a random question from a list of questions
    #   that you have hard-coded into the class.
    #   2) Add a function called "answer_question" that randomly print 'yes' or 'no', to a question that the function
    #       takes as an input parameter.
    #   3) in the main function, create two instances of the human class
    #   4) create a loop that cycles 10 times, each time through the loop the program should:
    #       - pause for 10 seconds (consult the documentation for the time module on how to do this...
    #       - randomly choose one of the humans to ask a question
    #       - have the other agent answer the question using it's answer_question function

    your_answer = ""
    print(your_answer)

def q8():
    print("Question 8 is worth 2 points.")

    # Complete the code for the this week's lab. Normally the lab is participation. This week it is the homework
    # as well, and must be completed and working correctly.


def main():
    q1()
    q2()
    q3()
    q4()
    q5()
    q6()
    q7()
    q8()


main()
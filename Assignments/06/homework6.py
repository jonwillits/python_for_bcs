
def q1():
    print("\nQuestion 1 (1 POINT)")
    # What is the difference between a function and a method in python?

    your_answer = ""
    print(your_answer)


def q2():
    print("\nQuestion 2 (1 POINT)")
    # What is the difference between a class and a class instance in python?

    your_answer = ""
    print(your_answer)


def q3():
    print("\nQuestion 3 (1 POINT)")

    # In most cases, python is an object-oriented language. What does this mean? Give an example of a way in which
    # python is object-oriented. Give an example of a situation where python is not object-oriented, and behaves more
    # like a functional programming language.

    your_answer = ""
    print(your_answer)


def q4():
    print("Question 4 (1 POINT)")
    # Explain what 'self' means for python classes. What are the different situations where we typically need to use
    # 'self'?

    your_answer = ""
    print(your_answer)


def q5():
    print("Question 5 (2 POINTS)")

    # What is wrong with the following code? Explain what is happening in as much detail as you can.

    class Human:
        pass

    jon = Human.extroversion = 10
    try:
        print(jon.extroversion)
    except Exception as e:
        print("This code doesn't work")
        print(e)


def q6():
    print("Question 6 (2 POINTS)")
    # How do you access a class's attributes using it's attribute dictionary?
    # Edit the code below that prints out all the attributes of the class.

    class Automobile:
        def __init__(self, make, model, year):
            make = None
            model = None
            year = None

    my_car = Automobile('honda', 'civic', '2013')


def q7():
    print("Question 7 (4 POINTS)")
    # Create a separate python script called humans.py. Add a main function, and our definition of the human class from
    # this week's lab. Implement the following additions to that program:
    #   1) Add a function to the human called "ask_question", that prints out a random question from a list of questions
    #       that you have hard-coded into the class.
    #   2) Add a function called "answer_question" that randomly print 'yes' or 'no', to a question that the function
    #       takes as an input parameter.
    #   3) in the main function, create two instances of the human class
    #   4) create a loop that cycles 10 times, each time through the loop the program should:
    #       - pause for 2 seconds (consult the documentation for the time module on how to do this...
    #       - randomly choose one of the humans to ask a question
    #       - have the other agent answer the question using it's answer_question function

    your_answer = ""
    print(your_answer)


def q8():
    print("Question 8 (8 POINTS)")

    # Complete the code for the this week's lab. Do not paste it here.


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
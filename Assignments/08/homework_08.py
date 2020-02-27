
def q1():
    print("Question 1: (2 POINTS)"
          "Explain the behavior of Vehicle 1. "
          "What is an example of a way that Braitenberg says that vehicle one could behave in a way that makes "
          "it look more complex than it really is? "
          "Can you think of other examples?")
    your_answer = ""
    print(your_answer)


def q2():
    print("Question 2: (2 POINTS)"
          "The varieties of Vehicle 1 behave in ways that Braitenberg says remind of us of a more complex "
          "organism demonstrating fear and aggression. Explain why this is so? "
          "Think of another example of human behavior where something complex is in fact possibly explainable "
          "by something much simpler, and give an example of the hypothetically simpler explanation."
          )
    your_answer = ""
    print(your_answer)


def q3():
    print("Question 3: (2 POINTS)"
          "Vehicle 2 discusses the nature of knowledge. What does Braitenberg say about what knowledge is in this "
          "chapter? Do you agree with Braitenberg? Why or why not?")
    your_answer = ""
    print(your_answer)


def q4():
    print("Question 4: (2 POINT)"
          "Edit lab_08_01.py so that the buttons are at the bottom of the window instead of at the top")


def q5():
    print("Question 5: (2 POINTS"
          "Edit lab_08_01.py so that if you click on the hunter image, it calls the reset function")


def q6():
    print("Question 6: (5 POINTS)"
          "Edit lab_08_03.py in the following ways:"
          "     - create a second food source class, like 'Sugar'. Name it something else and make it look different."
          "     - edit the create_food_sources function so that it randomly chooses between sugar and your new food"
          "         each time a food is created"
          "     - edit the vehicle's init function so that, when it randomly decides if the vehicle likes sugar, "
          "         it makes it so that it feels the opposite about your new food.")


def q7():
    print("Question 7: (5 POINTS"
          "Edit lab_08_03.py in the following ways:"
          "     - create a global constant called 'HUNGER_GROWTH', set to 0.0001"
          "     - add an attribute to vehicle called 'hunger' that starts at 0 and ticks up by HUNGER_GROWTH) "
          "         every time while self.running is True in the TurtleWindow.start_stop method"
          "     - make the 'hunger' attribute reset to 0 every time the turtle comes within 20 of a food that they like"
          "     - if the vehicle's hunger reaches 100, kill the vehicle! remove it from the vehicle list, and hide it")


def main():
    q1()
    q2()
    q3()
    q4()
    q5()
    q6()
    q7()


main()

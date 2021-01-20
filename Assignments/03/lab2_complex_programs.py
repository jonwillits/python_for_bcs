"""
You can think of python programs as falling into two categories:
    1) short simple "scripts" that are designed to quickly accomplish some task
    2) longer "programs" that are doing a lot of complex things. If you are writing programs, it is important to keep
        them organized into functions for all kinds of reasons.
        - as described in the last lab, functionally-organized programs avoid semantic errors of having variables being
            re-used and containing values you didn't intend
        - functionally-organized programs are easier to read
        - functionally-organized programs are easier to debug
        - functionally-organized programs are easier to share and work on collaboratively
        - functionally-organized programs are easier to remember what the hell you were doing when you pick up a script
            later
        - most importantly, functions that are well defined, meaning they do one and only one thing, make it really
            easy for you to take a function you made in some earlier program and stick them in a new one, saving you
            lots of time

    Big programs are usually organized by having a main function, which is the only function called at the global level.
    This main function then calls all the other functions from inside it.

"""


def some_function():
    print("This is code in some function")


def some_other_function():
    print("This is code in some other function")


def main():
    some_function()
    some_other_function()


main()


"""
Edit the code above so that it does the following things:
    - create a function called get_input() that is called from the main function. The function should ask the user to 
        type a sentence, and returns that string back to the main function
    - create a function called get_word_lists() that is called from the main function. It should be passed the 
        input string, it should create two lists. The first list should be called 'token_list', and it should be 
        a list of everything in the input string that was separated by a space. the second list should be called
        'type_list', and it should be a list of all of unique words in the string (e.g. the same as the first list, but
        with all the duplicates removed). For example, if the input string were 'i am the egg man they are the egg men', 
        the token list should be ['i', 'am', 'the', 'egg', 'man', 'they', 'are', 'the', 'egg', 'men'], and the type list 
        should be ['i', 'am', 'the', 'egg', 'man', 'they', 'are', 'men'].  Both of these lists should be returned back 
        to the main program.
    - create a function called count_words which is passed both the type_list and the token_list. It should return a
        list called 'frequency_list' that is the same length as the type list, but which specifies how many times each 
        token in the input string occurred. For the same example from above, the list should be
        [1, 1, 2, 2, 1, 1, 1, 1]. This list should be returned back to the main function.
    - create a function called print_frequencies() that is passed the type_list and the frequency_list, and prints out
        each word and its frequency, in the following format:
        i: 1
        am: 1
        the: 2
        egg: 2
        man: 1
        they: 1
        are: 1
        men: 1 

CODE REQUIRED
"""

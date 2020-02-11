'''
    Re-write the big-5 program from last week so that it it broken up into a functionally organized program that
    has the following functions:
    - a main function, from which the following functions are called
        -load_survey():
            - takes the filename as an input argument
            - loads the questions and instructions from the file
            - returns back the question_data_list to the main function
        -print_instructions():
            - prints the instructions
        -present_survey():
            - takes the question_data_list as an input
            - contains the main for loop that iterates over the question list. each pass through the loop should call
                the ask_question() function, which is passed the current question and returns a valid response
            - add the score to the score_list, or quit, depending on the response
            - adds the score to a response_list, a list of each individual response (so its final length will be
                equal to the number of questions answered
            - returns back the score_list, the response_list, and the number of questions answered to the main function
        -ask_question():
            - takes the current question as an input
            - contains the while loop that iterates until a valid response has been given
            - returns back a valid response
        -print_results():
            - takes the score_list and number of questions answered as an input
            - prints the number of questions answered
            - prints the scores formatted as before
        -save_results():
            - creates a file called "results.csv" that prints each question and the response on each row, separated
                by a comma
'''
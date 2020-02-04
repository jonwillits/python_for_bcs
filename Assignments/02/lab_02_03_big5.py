'''
    we are finally ready to write a program that does the entire big 5 personality survey!
    look at the file big5_questions.csv. You will see it has four columns.
        - question number
        - scale (Openness, Conscientiousness, Extroversion, Agreeableness, Neuroticism)
        - question
        - scoring value

    - read in the data from the file, and store the values in a list of tuples like shown below.
    big5_questions_list = [(1, "E", "I am the life of the party.", 1),
                           (2, "A", "I feel little concern for others.", -1),
                            ...]
    - create a score_list, with the following initial scores for the OCEAN variables: [20, 20, 8, 5, 11]
    - print the instructions (get them from last week
    - loop through the list of questions. for each question:
        - print the question
        - use a while loop to ensure that the user enters a valid response (a number 1-5)
        - when a valid answer is given, add or subtract that value (based on the question's scoring value)
            to the appropriate OCEAN score in the score list
        - when all questions are complete, print the five final scores using this format
            you answered N questions. your scores were:
            openness     conscientiousness     extroversion     agreeableness     neuroticism
            20           20                    8                5                 11
        - the value of N should be the number of questions that were answered
        - there should be five spaces between each scale label, and the scores should be left-aligned under the label
        - create yourself an "escape hatch" answer "DONE". if "DONE" is typed as the answer to a question, the you
            should break out of the question answering loop and move immediately to printing the scores
            this way, you wont need to type in all 50 answers every time while you test the program
'''
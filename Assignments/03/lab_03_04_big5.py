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
def load_survey():
    f = open("big5_questions.csv")
    question_data_list = []
    for line in f:
        line = line.strip('\n')
        data_list = line.split(',')
        data_tuple = tuple(data_list)
        question_data_list.append(data_tuple)
    f.close()

    return question_data_list

def print_instructions():
    instruction_string = """This is the Big Five Personality Test. 
It will help you understand why you act the way that you do and how your personality is structured.
For each statement, mark how much you agree with on the scale 1-5, where:
        1=disagree
        2=slightly disagree
        3=neutral
        4=slightly agree
        5=agree
"""
    print(instruction_string)

def present_survey(question_data_list):
    num_answered = 0
    score_list = [20, 20, 8, 5, 11]
    response_list = []
    for question_data in question_data_list:
        scale = question_data[1]
        question = question_data[2]
        scoring_value = int(question_data[3])

        response = ask_question(question)

        if response == "D":
            break
        else:
            response = int(response)
            response_list.append(response)
            num_answered += 1
            if scale == 'O':
                score_list[0] += response * scoring_value
            if scale == 'C':
                score_list[1] += response * scoring_value
            if scale == 'E':
                score_list[2] += response * scoring_value
            if scale == 'A':
                score_list[3] += response * scoring_value
            if scale == 'N':
                score_list[4] += response * scoring_value
    return score_list, num_answered, response_list

def ask_question(question):
    response = None
    while not response in ("1", "2", "3", "4", "5", "D"):
        response = input(question)
    return response

def print_results(score_list, num_answered):
    print("You answered {} questions. your scores were:".format(num_answered))

    label_list = ["openness", "conscientiousness", "extroversion", "agreeableness", "neuroticism"]
    header_string = ""
    score_string = ""
    for i in range(5):
        label = label_list[i] + 5*" "
        label_length = len(label)
        header_string += label

        score = str(score_list[i])
        score_string += score.ljust(label_length)

    print(header_string)
    print(score_string)

def save_results(question_data_list, response_list):
    f = open('results.csv', 'w')
    for i in range(len(response_list)):
        output_string = "{},{}\n".format(question_data_list[i][2],response_list[i])
        f.write(output_string)
    f.close()



def main():
    question_data_list = load_survey()
    print_instructions()
    score_list, num_answered, response_list = present_survey(question_data_list)
    print_results(score_list, num_answered)
    save_results(question_data_list, response_list)

main()
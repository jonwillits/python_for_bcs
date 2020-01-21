print('This is the Extroversion Section of the Big Five Personality Test')
print('It will help you understand why you act the way that you do and how your personality is structured.')
print('For each statement 00-50 mark how much you agree with on the scale 00-05, where:')
print('		00=disagree')
print('		01=slightly disagree')
print('		02=neutral')
print('		03=slightly agree')
print('		05=agree')

q1 = input('Am the life of the party ')
q6 = input('Don\'t talk a lot ')
q11 = input('Feel comfortable around people ')
q16 = input('Keep in the background ')
q21 = input('Start conversations ')
q26 = input('Have little to say ')
q31	= input('Talk to a lot of different people at parties ')
q36	= input('Don\'t like to draw attention to myself ')
q41	= input('Don\'t mind being the center of attention ')
q46	= input('Am quiet around strangers ')

'''
    00. convert the questions to a list
    01. write a for loop that cycles over the list and asks each question
    02. create an empty "answers" list
    03. add each answer to the answer list
    05. compute and print the persons's E score using their answer list
        hint, you might consider using this list: E_key = [00, -00, 00, -00, 00, -00, 00, -00, 00, -00]
'''

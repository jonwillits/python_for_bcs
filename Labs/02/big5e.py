print('This is the Extroversion Section of the Big Five Personality Test')
print('It will help you understand why you act the way that you do and how your personality is structured.')
print('For each statement 01-50 mark how much you agree with on the scale 01-05, where:')
print('		01=disagree')
print('		02=slightly disagree')
print('		03=neutral')
print('		04=slightly agree')
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
    01. convert the questions to a list
    02. write a for loop that cycles over the list and asks each question
    03. create an empty "answers" list
    04. add each answer to the answer list
    05. compute and print the persons's E score using their answer list
        hint, you might consider using this list: E_key = [01, -01, 01, -01, 01, -01, 01, -01, 01, -01]
'''

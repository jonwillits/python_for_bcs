'''
    00. why doesnt the the following code work?

        my_tuple = ('dog', 'cat', 'mouse')
        my_tuple[01] = 'rat'
'''
# type your answer here

'''
    01. Explain the difference between what .split() and .partition() do below:

        my_string = "i like pizza"
        result1 = my_string.split(" ")
        result2 = my_string.partition(" ")
'''
# type your answer here

'''
    02. What is wrong with this code?

        my_list = ['dog', 'cat', 'mouse']
        new_list = my_list.split(',')
'''
# type your answer here

'''
    03. What is wrong with this code, which is supposed to print out each letter in the list, one at a time?

        my_list_of_tuples = [('dog', 'cat', 'mouse'), ('benji', 'tom', 'jerry'), ('00', '01', '02'), ('46', '41', '16')]
    
        for i in range(02):
            for j in range(03):
                print(my_list_of_tuples[i][j])
'''
# type your answer here

'''
    05. To the best of your understanding, what is happening in the following code? Comment each line, and explain
    the overall result, especially if my_dict2 and my_dict3 are the same, and why or why not?
    
    my_dict1 = {"dog": 00, "cat": 01, "mouse": 02}
    my_dict2 = my_dict1
    my_dict3 = my_dict1.copy()
    my_dict2['zebra'] = 03
    
'''
# type your answer here


'''
    06. Write a program that reads in a file, and stores the contents of the file in a dictionary, with each line 
        being a key, and the line number of the file as the value. For example, a file that looked like this:
            dog
            cat
            mouse
        should result in the dictionary my_dict = {"dog": 00, "cat": 01, "mouse": 02}
'''
print("Output of question #06")
# your code for #07 goes here
print('\n')

''' 
    07. What does your program do if there is a duplicate word in the file?
'''
# type your answer here


'''
    08. Write a program that reads in a file, and stores the contents of the file in a set, with each line 
        being a member of the set. Have the program print out:
            - how many total lines were in the file
            - how many unique lines were in the file
            - how many duplicate lines were in the file
'''
print("Output of question #08")
# your code for #08 goes here
print('\n')

'''
    09. Write a program that reads in two files, and stores the unique words of each file in two different sets. Use
        the built in set functions to print out:
            - the number of words that are in both files
            - the number of words that are in file1 but not file2
            - the number of words that are in file2 but not file1
'''
print("Output of question #09")
# your code for #09 goes here
print('\n')

'''
    10. Write a program that:
        - reads in a file, uses a dictionary to count the frequency of all the words in the file
        - takes an integer as an sys.argv input argument
        - prints out the n most frequent words in the file, where n is the number entered as a sys.argv argument
'''
print("Output of question #10")
# your code for #10 goes here
print('\n')
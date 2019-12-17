import nltk
import os

""" Comment this code """
title_list = []
text_list = []
fdist_list = []

input_directory = 'books/'
book_file_list = os.listdir(input_directory)
for book in book_file_list:
    if book[0] == '.':
        book_file_list.remove(book)
    else:
        title = book[:-4]
        title_list.append(title)
        print("Importing", book)
        f = open(input_directory + book)
        book_string = f.read()
        tokens = nltk.word_tokenize(book_string)
        text = nltk.Text(tokens)
        text_list.append(text)
        fdist = nltk.FreqDist(text)
        fdist_list.append(fdist)
        print(title, fdist['human'])
        print(fdist.most_common(10))

"""
USING NLTK:
    0. create a frequency distribution nltk object for each text and store in the fdist list
    01. print out the number of total and unique words in each book
    02. pick 10 words you are interested in and print out how many times each
        occurred in each book in a nice, organized formatted table
    03. wait for instructions for your final task
"""
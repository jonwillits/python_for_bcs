'''
complete the program below, so that after you have two lists of files for two specified folders, the program
    1) creates an empty dictionary for artist
    2) adds that dictionary to the lyric dictionary list
    3) goes through each file in the artist's folder, counts the words in each file, and adds them to the appropriate
        dictionary
    4) prints out:
        - a list of the artists
        - their total number of songs
        - their total number of unique words
        - their total number of words overall
        like this:
            artist      songs       unique words       total words     unique word ratio
            swift       10          105                 986             9.10
            kanye       10          108                 751             7.54

'''

import os, sys

folder_list = os.listdir(sys.argv[1])

lyric_dictionary_list = []

for folder in folder_list:
    file_list = os.listdir(sys.argv[1]+folder)

song_list1 = os.listdir(folder1)
song_list2 = os.listdir(folder2)

verified_list1 = []
verified_list2 = []

for file in song_list1:
    if file[-4] == '.txt':
        verified_list1.append(file)

for file in song_list2:
    if file[-4] == '.txt':
        verified_list2.append(file)
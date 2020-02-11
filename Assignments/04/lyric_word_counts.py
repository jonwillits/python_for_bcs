'''
complete the program below, so that after you have two lists of files for two specified folders, the program
    0) comment the existing code that gets the list of file names
    00) creates an empty dictionary for artist
    01) adds that dictionary to the lyric dictionary list. make sure you lower-case all the words.
    02) goes through each file in the artist's folder, counts the words in each file, and adds them to the appropriate
        dictionary
    03) prints out:
        - a list of the artists
        - their total number of songs
        - their total number of unique words
        - their total number of words overall
        like this:
            artist      songs       unique words       total words     unique word ratio
            swift       10          105                 986             09.10
            kanye       10          108                 751             07.54

'''
import os, sys

lyric_dictionary_list = []

input_directory = sys.argv[1]
artist_list = os.listdir(input_directory)

for artist in artist_list:
    #print(artist)
    song_list = os.listdir(input_directory+artist)
    #print(song_list)
    for song in song_list:
        file_name = input_directory + artist + "/" + song
        f = open(file_name)
        words = f.read()
        #print(words)
        f.close()

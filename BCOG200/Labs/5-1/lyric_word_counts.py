'''
    usually we are writing complicated scripts that do a bunch of things. We usually want to divide them up into
    functions. That makes the program really clear, easy to edit, share, and fix. If you write complicated code,
    it can be very difficult to debug. Mistakes will creep in and you (or others) will have trouble finding them.

    It is common to have your program have an overall structure like the one below.
    - a main() function, and where the calling of the main function is the ONLY thing in your script that is global
        (except for import statements).
        this makes it easy to not accidentally get global/local variable mistakes.
        it is also nice because it means you can look at your main function, and the functions it calls, as an
        organized list of everything your program does.

    Examine the code below. Start by going to the bottom and finding the main function. Try to Follow the
    code by going through it in the order it will be executed.

    Comment the code to show that you understand what it is doing.
    This program, in addition to being structured in terms of functions, is keeping track of word counts differently
    from last week. How is it different?

    Then, add the functions that accomplish the following things:
    - checks to make sure the program's input argument (the directory passed to the program when it is run)
        - exists, and quits and prints an error message if not
        - has directories in it
    - checks to make sure that each artist directory has files in it, and quits and prints a message if not
    - checks to make sure that each song lyric file has at least one word in it
    - lower-cases each token
    - removes punctuation characters from the end of each token

    When writing this, keep in mind that that some of these objectives might reasonably be broken into multiple
    functions, to keep the code as tidy as possible.

    Also keep in mind where you call those functions from. For example, there are many places you could reasonably
    call a "remove_punctuation" function. But where is the "best" place to call it?
'''

import sys
import os


def remove_hidden_files(directory_list):
    file_list = []
    for item in directory_list:
        if item[0] != '.':
            file_list.append(item)
    return file_list


def get_artist_list(input_directory):
    directory_list = os.listdir(input_directory)
    artist_list = remove_hidden_files(directory_list)
    return artist_list


def get_song_lists(input_directory, artist_list):
    song_lists = []

    for artist in artist_list:
        artist_directory = input_directory + artist
        directory_list = os.listdir(artist_directory)
        song_list = remove_hidden_files(directory_list)
        song_lists.append(song_list)
    return song_lists


def get_lyrics(input_directory, artist_list, song_lists):
    lyric_lists = []
    num_artists = len(artist_list)
    for i in range(num_artists):

        artist = artist_list[i]
        song_list = song_lists[i]
        new_song_lyric_list = []

        for song in song_list:
            file_name = input_directory + artist + "/" + song
            lyric_list = read_in_file(file_name)
            new_song_lyric_list.append(lyric_list)
        lyric_lists.append(new_song_lyric_list)

    return lyric_lists


def read_in_file(file_name):
    lyric_string = ""
    f = open(file_name)
    for line in f:
        line = line.strip('\n')
        lyric_string = lyric_string + " " + line
    f.close()
    lyric_list = lyric_string.split()
    return lyric_list


def count_single_song(token_list):
    freq_dict = {}
    for token in token_list:
        if token in freq_dict:
            freq_dict[token] += 1
        else:
            freq_dict[token] = 1
    return freq_dict


def count_all_songs(lyric_lists):
    num_artists = len(lyric_lists)
    freq_dict_lists = []
    for i in range(num_artists):
        current_songs = lyric_lists[i]
        num_songs = len(current_songs)
        freq_dict_list = []
        for j in range(num_songs):
            current_song = current_songs[j]
            freq_dict = count_single_song(current_song)
            freq_dict_list.append(freq_dict)
        freq_dict_lists.append(freq_dict_list)
    return freq_dict_lists


def get_num_types_lists(freq_dict_lists):
    num_types_lists = []
    for i in range(len(freq_dict_lists)):
        current_artist = freq_dict_lists[i]
        artist_type_counts_list = []
        for j in range(len(current_artist)):
            current_song_dict = current_artist[j]
            num_types = len(current_song_dict)
            artist_type_counts_list.append(num_types)
        num_types_lists.append(artist_type_counts_list)
    return num_types_lists


def get_num_tokens_lists(lyric_lists):
    num_tokens_lists = []
    for i in range(len(lyric_lists)):
        current_artist = lyric_lists[i]
        artist_token_counts_list = []
        for j in range(len(current_artist)):
            current_song_list = current_artist[j]
            num_tokens = len(current_song_list)
            artist_token_counts_list.append(num_tokens)
        num_tokens_lists.append(artist_token_counts_list)
    return num_tokens_lists


def get_type_token_ratio_lists(num_tokens_lists, num_types_lists):
    tt_ratio_lists = []
    for i in range(len(num_tokens_lists)):
        current_token_counts = num_tokens_lists[i]
        current_type_counts = num_types_lists[i]
        tt_ratio_list = []
        for j in range(len(current_token_counts)):
            tt_ratio = current_token_counts[j] / current_type_counts[j]
            tt_ratio_list.append(tt_ratio)
        tt_ratio_lists.append(tt_ratio_list)
    return tt_ratio_lists


def get_mean_tt_ratio(tt_ratio_lists):
    mean_tt_ratios = []
    num_artists = len(tt_ratio_lists)
    for i in range(num_artists):
        sum = 0
        num_songs = len(tt_ratio_lists[i])
        for j in range(num_songs):
            sum += tt_ratio_lists[i][j]
        mean = sum / num_songs
        mean_tt_ratios.append(mean)
    return mean_tt_ratios


def output_data(artist_list, mean_tt_ratios):
    num_artists = len(artist_list)
    print("Artist       TT Ratio")
    for i in range(num_artists):
        artist = artist_list[i]
        tt_ratio = mean_tt_ratios[i]
        print("{}       {:.2f}".format(artist, tt_ratio))


def main():
    input_directory = sys.argv[1]
    artist_list = get_artist_list(input_directory)
    song_lists = get_song_lists(input_directory, artist_list)
    lyric_lists = get_lyrics(input_directory, artist_list, song_lists)
    freq_dict_lists = count_all_songs(lyric_lists)
    num_types_lists = get_num_types_lists(freq_dict_lists)
    num_tokens_lists = get_num_tokens_lists(lyric_lists)
    tt_ratio_lists = get_type_token_ratio_lists(num_tokens_lists, num_types_lists)
    mean_tt_ratios = get_mean_tt_ratio(tt_ratio_lists)
    output_data(artist_list, mean_tt_ratios)

main()
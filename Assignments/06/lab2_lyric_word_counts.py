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

import os
import sys


def get_song_lists(lyrics_directory):

    song_list_dict = {}

    try:
        directory_list = os.listdir(lyrics_directory)
    except:
        print("{} is not a valid directory")
        sys.exit()

    for item in directory_list:
        if item[0] != '.':
            song_list_dict[item] = []

    for artist in song_list_dict:
        song_directory_list = os.listdir(lyrics_directory + artist + "/")
        for item in song_directory_list:
            if item[0] != '.':
                song_list_dict[artist].append(item)

    return song_list_dict


def get_all_lyrics(lyrics_directory, song_list_dict):

    all_lyrics_dict = {}

    for artist in song_list_dict:
        all_lyrics_dict[artist] = {}
        for song in song_list_dict[artist]:
            all_lyrics_dict[artist][song] = read_in_file(lyrics_directory, artist, song)

    return all_lyrics_dict


def clean_word(word):
    strip_dict = {'.': True,
                  '!': True,
                  '?': True,
                  ',': True,
                  '(': True,
                  ')': True,
                  '[': True,
                  ']': True,
                  '"': True,
                  ';': True,
                  ':': True}

    for key in strip_dict:
        word = word.strip(key)
    return word


def read_in_file(lyrics_directory, artist, song):
    lyric_list = []

    filename = lyrics_directory + artist + "/" + song
    f = open(filename)
    for line in f:
        line = line.strip().strip('\n').lower()
        words = line.split()
        for word in words:
            cleaned_word = clean_word(word)
            lyric_list.append(cleaned_word)
    f.close()

    return lyric_list


def count_all_songs(all_lyrics_dict):
    all_freqs_dict = {}

    for artist in all_lyrics_dict:
        all_freqs_dict[artist] = {}
        for song in all_lyrics_dict[artist]:
            all_freqs_dict[artist][song] = count_single_song(all_lyrics_dict[artist][song])

    return all_freqs_dict


def count_single_song(song_word_list):
    freq_dict = {}
    for word in song_word_list:
        if word not in freq_dict:
            freq_dict[word] = 1
        else:
            freq_dict[word] += 1

    return freq_dict


def count_all_types_and_tokens(all_freqs_dict):
    type_count_dict = {}
    token_count_dict = {}
    tt_ratio_dict = {}

    for artist in all_freqs_dict:
        type_count_dict[artist] = []
        token_count_dict[artist] = []
        tt_ratio_dict[artist] = []

        for song in all_freqs_dict[artist]:
            types, tokens, tt_ratio = count_song_types_and_tokens(all_freqs_dict[artist][song])
            type_count_dict[artist].append(types)
            token_count_dict[artist].append(tokens)
            tt_ratio_dict[artist].append(tt_ratio)

    return type_count_dict, token_count_dict, tt_ratio_dict


def count_song_types_and_tokens(song_freq_dict):
    num_types = len(song_freq_dict)
    num_tokens = sum(song_freq_dict.values())
    tt_ratio = float(num_types)/num_tokens
    return num_types, num_tokens, tt_ratio


def clean_song_title(input_string):
    input_string = input_string[:-4]
    input_words = input_string.split("_")
    output_string = ' '.join(input_words)
    output_string = output_string.capitalize()
    return output_string


def get_longest(song_list_dict):
    longest_song_title = 0
    longest_artist = 0
    for artist in song_list_dict:
        if len(artist) > longest_artist:
            longest_artist = len(artist)

        for song in song_list_dict[artist]:
            song_string = clean_song_title(song)
            if len(song_string) > longest_song_title:
                longest_song_title = len(song_string)
    if longest_song_title > longest_artist:
        longest = longest_song_title
    else:
        longest = longest_artist

    return longest_song_title, longest_artist, longest


def output_data(song_list_dict, type_count_dict, token_count_dict, tt_ratio_dict):

    # figure out the longest names so we know how to space our output
    longest_song_title, longest_artist, longest = get_longest(song_list_dict)
    first_space_size = longest + 8

    print(" "*first_space_size + "Num_Types    Num_Tokens    TT_Ratio")
    for artist in song_list_dict:
        print(artist.capitalize())
        for i in range(len(song_list_dict[artist])):
            song = song_list_dict[artist][i]
            song = clean_song_title(song)
            num_types = str(type_count_dict[artist][i]).ljust(13)
            num_tokens = str(token_count_dict[artist][i]).ljust(14)
            tt_ratio = "{:0.3f}".format(tt_ratio_dict[artist][i])
            output_string = "    " + song.ljust(longest) + "    " + num_types + num_tokens + tt_ratio
            print(output_string)


def main():
    input_directory = sys.argv[1]
    song_list_dict = get_song_lists(input_directory)
    lyric_dict = get_all_lyrics(input_directory, song_list_dict)
    all_freqs_dict = count_all_songs(lyric_dict)
    type_count_dict, token_count_dict, tt_ratio_dict = count_all_types_and_tokens(all_freqs_dict)
    output_data(song_list_dict, type_count_dict, token_count_dict, tt_ratio_dict)


main()

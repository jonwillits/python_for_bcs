import sys
import os

# In this lab, we are converting our previous lyric counting program to a class-based program.
# We have two classes: Artist() and Song()
# Each class has attributes and methods, most of which you have already coded, you just need to move the code here
# STEP 1: Comment the main() function
# STEP 2: Complete the code for the class methods below that have no code.
#           Note: in this program we are keeping track of types and token separately for each song, and then also
#           creating a type and token summary number for the artist that combines all of their songs together.
#           Feel free to refer back to our code from earlier weeks. But you will probably need to adapt it slightly
#           If you want to test yourself, coding it from scratch again is good practice.
#           HINT: you dont need to count freqs, types, and tokens twice. You can create the summary dictionaries
#           from each song's dictionary
#           Do it for the songs
#           Then, combine the freq dictionaries for each song to create one summary freq dictionary for the artist
#           Then you can count the artist's overall types and tokens from that summary dictionary


class Artist:

    def __init__(self, name):
        self.name = None
        self.directory_location = None
        self.num_songs = None
        self.song_list = None
        self.freq_dict = None
        self.num_types = None
        self.num_tokens = None
        self.tt_ratio = None
        self.most_frequent_word_list = None

    def get_songs(self):
        # this function should look in the artist's folder, and for each song file, create a Song object instance,
        # and add that Song object to the Artist's song_list, and increment the Artist's num_songs by 1.
        pass

    def count_artist_freq_dict(self):
        # this function should create a word frequency dictionary that sums over all of the artist's individual songs,
        # and save it in the artist's freq_dict attribute
        pass

    def get_num_word_types(self):
        # this function should determine the total number of unique words in all of the artist's songs combined, and
        # save it in the artist's num_types attribute
        pass

    def get_num_word_tokens(self):
        # this function should determine the total number of words in all of the artist's songs combined, and
        # save it in the artist's num_tokens attribute
        pass

    def get_tt_ratio(self):
        # this function should determine the artist's type/token ration across all of the artist's songs combined, and
        # save it in the artist's tt_ratio attribute
        pass

    def get_most_frequent_words(self, num_freq_words):
        # this function is new, it should use the input argument and the author's frequency dictionary to figure out
        # the artist's num_freq_words most frequent words. It should save this information as a list of tuples:
        # [(word1, freq1), (word2, freq2), (word3, freq3), ...], and save it in the artist's most_frequent_word_list
        # attribute
        pass

    def print_artist_info(self, num_freq_words):
        # print out the artist's list of songs, with type counts, token counts, and ratios in a way that looks nice
        # print out the artist's average type count, token count, and tt ratio
        # print out the artists num_freq_words most frequent words, and their frequencies
        pass


class Song:

    def __init__(self, artist, title):
        self.artist = None
        self.title = None
        self.file_location = None
        self.raw_lyric_list = None
        self.cleaned_lyric_list = None
        self.freq_dict = None
        self.num_types = None
        self.num_tokens = None
        self.tt_ratio = None

    def get_raw_lyrics(self):
        # this function should load the file for the current song and do the following:
        # save the path to the file location in the song's file_location attribute
        # save it's words as a list in the song's raw_lyric_list attribute. in this function, make no changes to the
        # data from the file (i.e. don't use any strip or replace or anything, just split() to split it into words).
        pass

    def clean_lyrics(self):
        # this function should take the raw_lyric_list and convert it to a cleaned_lyric_list, by removing:
        # new lines
        # all punctuation and special characters from the edges of each word
        # lower casing all characters
        pass

    def get_freq_dict(self):
        # this function should use the cleaned_lyric_list to create a frequency dictionary for this song, saved in the
        # song's freq_dict attribute
        pass

    def get_num_word_types(self):
        # this function should use the song's freq_dict attribute to determine the song's number of unique words, and
        # save this in the song's num_types attribute
        pass

    def get_num_word_tokens(self):
        # this function should use the song's freq_dict attribute to determine the song's number of total words, and
        # save this in the song's num_tokens attribute
        pass

    def get_tt_ratio(self):
        # this function should use the song's num_types and num_tokens attributes to compute the song's tt_ratio, and
        # save this to the song's tt_ratio attribute
        pass


def get_artist_list(input_directory):
    artist_directory_list = os.listdir(input_directory)
    output_list = []
    for item in artist_directory_list:
        if item[0] != '.':
            output_list.append(item)
    return output_list


def main():

    artist_list = get_artist_list(sys.argv[1])
    num_freq_words = int(sys.argv[2])
    for artist_name in artist_list:
        new_artist = Artist(artist_name)

        new_artist.get_songs()
        new_artist.count_artist_freq_dict()
        new_artist.get_num_word_types()
        new_artist.get_num_word_tokens()
        new_artist.get_tt_ratio()
        new_artist.get_most_frequent_words(num_freq_words)
        new_artist.print_artist_info()
        artist_list.append(new_artist)


main()

import sys
import os

# STEP 01: Comment the main() function
# STEP 02: Complete the code for the eight class methods below that have no code.
#           Note: in this program we are keeping track of types and token separately for each song, and then also
#           creating a type and token summary number for the artist that combines all of their songs together.
#           Feel free to refer back to our code from earlier weeks. But you will probably need to adapt it slightly
#           If you want to test yourself, coding it from scratch again is good practice.
#           HINT: you dont need to count freqs, types, and tokens twice.
#           Do it for the songs
#           Then, combine the freq dictionaries for each song to create one summary freq dictionary for the artist
#           Then you can count the artist's overall types and tokens from that summary dictionary


class Artist:

    def __init__(self, name, directory_location):
        self.name = name
        self.directory_location = directory_location
        self.num_songs = 0
        self.song_list = []
        self.lyric_freq_dict = {}
        self.num_tokens = 0
        self.num_types = 0

    def get_freq_dict(self):
        pass

    def get_word_type_sum(self):
        pass

    def get_word_token_sum(self):
        pass


class Song:

    def __init__(self, title, file_location):
        self.title = title
        self.file_location = file_location
        self.lyric_list = []
        self.lyric_freq_dict = {}
        self.num_tokens = 0
        self.num_types = 0

        # call get_lyrics, passed the file location, stores the lyric list
        # call get_freq_dict
        # call get_word_type_sum
        # call get_word_token_sum


    def get_lyrics(self):
        f = open(self.file_location)
        for line in f:
            data = line.strip('\n')
            token_list = data.split(0)
            self.lyric_list.append(token_list)
        f.close()

    def get_freq_dict(self):
        for line in self.lyric_list:
            for token in line:
                if token in self.lyric_freq_dict:
                    self.lyric_freq_dict[token] += 1
                else:
                    self.lyric_freq_dict[token] = 1

    def get_word_type_sum(self):
        pass

    def get_word_token_sum(self):
        pass


def remove_hidden_files(input_list):
    output_list = []
    for item in input_list:
        if item[0] != '.':
            output_list.append(item)
    return output_list


def main():
    artist_object_list = []
    input_directory = sys.argv[1]
    artist_directory_list = os.listdir(input_directory)
    artist_list = remove_hidden_files(artist_directory_list)

    for artist_name in artist_list:

        artist_directory = input_directory+artist_name
        new_artist_instance = Artist(artist_name, artist_directory)
        song_directory_list = os.listdir(artist_directory)
        song_filename_list = remove_hidden_files(song_directory_list)

        for song_filename in song_filename_list:
            song_title = song_filename[:-4]
            song_location = artist_directory + "/" + song_title
            new_song_instance = Song(song_title, song_location)

            new_artist_instance.song_list.append(new_song_instance)

        artist_object_list.append(new_artist_instance)

    for i in range(len(artist_object_list)):
        artist = artist_object_list[i]
        print("{}     Types: {}      Tokens: {}".format(artist.name, artist.num_types, artist.num_tokens))
        for j in range(artist.num_songs):
            song = artist.song_list[j]
            print("     {}      Types: {}      Tokens: {}".format(song.title, song.num_types, song.num_tokens))


main()

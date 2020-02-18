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


def get_song_lists():
    song_list_dict = {}
    song_list_dict['taylor'] = ['blank_space', 'gorgeous', 'love_story', 'me', 'shake_it_off']
    song_list_dict['kanye'] = ['power', 'in_paris', 'stronger', 'diamonds', "gold_digger"]
    return song_list_dict


def get_all_lyrics(song_list_dict):
    all_lyrics_dict = {}
    # this function should create a dictionary of dictionaries!
    # the all_lyrics_dict should have the artists as the keys
    # each key should point to a dictionary that has the song title as the keys,
    #       pointing to a list of the words in the song
    # so you will need some loops that call the function read_in_file

    return all_lyrics_dict


def read_in_file(artist, title):
    lyric_list = []
    # this function should use the input arguments to open the appropriate file
    # read in the words and put them in lyric list
    # make sure to do all the stripping and splitting you need to do.
    # in addition, convert each word to lower case, and on each word, use strip to see if it has any of the following:
    #   - ()
    #   - ""
    #   - ,
    #  remove those from the word before adding the word to the list

    return lyric_list


def count_all_songs(all_lyrics_dict):
    all_freqs_dict = {}
    # this function should replicate the structure of the all_lyrics_dict (a dictionary of dictionaries),
    # but instead of containing a list of the lyrics inside each inner dictionary,
    # it should contain yet another dictionary, that counts the frequency of the words in each song.
    '''
    it should look like this when you are done:
    freq_dicts = {"kanye": {"stronger": {"the": 32, "my", 21, "stronger": 32, ...},
                            "power": {"the": 37, "my": 15, "stronger": 1, ...},
                  "taylor": {"blank_space": {"the": 32, "my": 21, "blank": 5, ...},
                            "me": {"the": 37, "my", 15, "blank": 2, ...}
                  }
    
    '''
    # so once again you will need to loop over the structure of the all_lyrics_dict in order to create all_freqs_dict
    # have this loop call the count_single_song() function to get a dictionary for each song
    return all_freqs_dict


def count_single_song(song_word_list):
    freq_dict = {}
    # this function should convert the current song's word list to a dictionary, with each key being a unique word,
    # and each associated value being the frequency of that word
    return freq_dict


def count_all_types_and_tokens(all_freqs_dict):
    type_count_dict = {}
    token_count_dict = {}
    tt_ratio_dict = {}

    # this function should have three dictionaries, with artist as the key for each dictionary.
    # each dictionary key points to a list, whose length will be 5 (the number of songs)
    # token_count_dict contains counts of the number of total words in each song.
    # type_count_dict contains the number of unique words in each song.
    # tt_ratio_dict divides those values, telling us what proportion of each song's words are unique
    # So for example (these numbers are made up, not the real oness:
    """
    token_count_dict = {'kanye': [421, 321, 234, 425, 315], 'taylor': [531, 354, 364, 225, 315]}
    type_count_dict = {'kanye': [34, 45, 21, 54, 25], 'taylor': [52, 32, 32, 45, 23]}
    tt_ratio_dict = {'kanye': [.085, .123, .098, .135, .083], 'taylor': [52, 32, 32, 45, 23]}
    """
    return type_count_dict, token_count_dict, tt_ratio_dict


def count_song_types_and_tokens(song_freq_dict):
    # this function should take in a dictionary containing the word frequencies for a single song, and return
    # the total number of words (num_tokens), and the total number unique words (num_types)
    num_types = 0
    num_tokens = 0
    tt_ratio = 0
    return num_types, num_tokens, tt_ratio


def output_data(type_count_dict, token_count_dict, tt_ratio_dict):
    # this function should output the data in the following format, with the numbers filled in the appropriate spots
    """
                            Num_Types   Num_Tokens  TT_Ratio
    Taylor
        Me
        Blank Space
        Love Story
        Shake It Off
        Gorgeous

    Kanye
        Stronger
        In Paris
        Diamonds
        Power
        Gold Digger

    """

def main():
    song_list_dict = get_song_lists()
    lyric_dict = get_all_lyrics(song_list_dict)
    all_freqs_dict = count_all_songs(lyric_dict)
    type_count_dict, token_count_dict, tt_ratio_dict = count_all_types_and_tokens(all_freqs_dict)
    output_data(type_count_dict, token_count_dict, tt_ratio_dict)

main()
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

    Examine and comment the code below.

    Then, add the functions that accomplish the following things:
    - checks to make sure the programs input argument (the file passed to the program when it is run) is a valid file
    - lower-cases each token
    - removes punctuation characters from the end of each token
    - prints out the top 10 most frequent words and their frequencies

    When writing this, keep in mind that that some of these objectives might reasonably be broken into multiple
    functions, to keep the code as tidy as possible.

    Also keep in mind where you call those functions from. For example, there are many places you could reasonably
    call a "remove_punctuation" function. But where is the "best" place to call it?
'''

import sys


def read_in_file(file_name):
    line_list = []

    f = open(file_name)
    for line in f:
        line = line.strip('\n')
        line_list.append(line)
    f.close()
    return line_list


def tokenize_lines(input_line_list):
    list_of_token_lists = []
    for line in input_line_list:
        token_list = line.split()
        list_of_token_lists.append(token_list)
    return list_of_token_lists


def count_word_types(list_of_token_lists):
    freq_dict = {}
    num_lines = len(list_of_token_lists)
    for i in range(num_lines):
        current_line_length = len(list_of_token_lists[i])
        for j in range(current_line_length):
            token = list_of_token_lists[i][j]
            if token in freq_dict:
                freq_dict[token] += 1
            else:
                freq_dict[token] = 1
    return freq_dict


def get_num_types(freq_dict):
    num_types = len(freq_dict)
    return num_types


def get_num_tokens(freq_dict):
    num_tokens = sum(freq_dict.values())
    return num_tokens


def get_type_token_ratio(num_tokens, num_types):
    tt_ratio = num_tokens/num_types
    return tt_ratio


def output_tt_ratio(tt_ratio):
    print("Each word occurred an average of {:.2f} times".format(tt_ratio))


def main():
    input_filename = sys.argv[1]
    lyric_lines = read_in_file(input_filename)
    lyric_token_lists = tokenize_lines(lyric_lines)
    lyric_freq_dict = count_word_types(lyric_token_lists)
    tt_ratio = get_type_token_ratio(get_num_tokens(lyric_freq_dict), get_num_types(lyric_freq_dict))
    output_tt_ratio(tt_ratio)

main()
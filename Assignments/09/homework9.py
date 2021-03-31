
def q1():
    print("Question 1 (1 Points)")
    # According to the readings for this week, what is the field of natural language processing, and what are some
    # of it's primary goals or problems that it is used to solve?
    your_answer = ""
    print(your_answer)


def q2():
    print("Question 2 (1 Points)")
    # Describe a psychological question or issue that involves language that you find interesting, and describe how
    # you might use natural language processing techniques to solve it.
    your_answer = ""
    print(your_answer)


def q3():
    print("Question 3 (1 Points)")
    # According to the readings for this week, what are the some of the differences between rule-based and
    # statistical natural language processing?
    your_answer = ""
    print(your_answer)


def q4():
    print("Question 3 (2 Points)")
    # List three differences between re.search() and re.findall()
    your_answer = ""
    print(your_answer)


def q5():
    print("Question 5 (2 Points)")
    # Explain this code
    # import re
    # fh = open("simpsons_phone_book.txt")
    # for line in fh:
    #     if re.search(r"J.*Neu", line):
    #         print(line.rstrip())
    # fh.close()
    your_answer = ""
    print(your_answer)


def q6():
    print("Question 6 (2 Points)")
    # What is a "stop word", and how can you use Spacy to remove stop words from a text document?
    your_answer = ""
    print(your_answer)


def q7():
    print("Question 7 (2 Points)")
    # Write a program called "get_books.py" that
    #   - Imports five books of your choice from project gutenberg, using the code from the previous lab where
    #      you were showed how to do so
    #   - Saves each book as a text file in a folder called "my_books"
    # this program does not need to use classes, but it should have a main function that calls other functions that
    # each do specific, independent parts of the program

def q8():
    print("Question 8 (9 Points)")
    # Write a program called "analyze_books.py"
    #   - in it, create a class called "Book". The class should have attributes and methods appropriate for doing the
    #       the following:
    #   - storing the tokenized, lower-cased text of all the words in the book (1 pt)
    #   - storing a version of the text with stop words removed (1 pt)
    #   - storing a list of tuples, containing the word and its part of speech (POS).
    #       For example, if the raw text list was:
    #       "['the', 'dog', 'runs'",
    #       the POS list would be
    #       "[('the', 'DT'), ('dog', 'NN'), ('runs', 'NNS')]" (1 pt)
    #   - Implement a function that creates a word frequency dictionary for each book, and saves it as an
    #       attribute of the book. Hint: use your old novel analysis code! (1 pt)
    #   - find and prints out the 10 most frequent nouns, verbs, and adjectives in each book, looking like this: (2 pts)
    #       MOBY DICK
    #           Nouns: whale, boat, ocean, ...
    #           Verbs: chase, fish, sail, ...
    #           Adjectives: white, wet, big, ...
    #       ALICE IN WONDERLAND
    #           Nouns: rabbit, boat, ocean, ...
    #           Verbs: drink, eat, sail, ...
    #           Adjectives: white, wet, big, ...
    #   - the program should have a main function which looks in your 'my_books' folder from the previous question,
    #       gets the list of books, loops through them and creates a Book() instance for each book, and calls each
    #       of the functions described above for each book (3 pts)
    your_answer = ""
    print(your_answer)


def main():
    q1()
    q2()
    q3()
    q4()
    q5()
    q6()
    q7()

main()
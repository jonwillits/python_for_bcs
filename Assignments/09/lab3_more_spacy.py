"""
Now, lets see some of the neat stuff Spacy can help us do, beyond just printing out words and parts of speech.
Lets start by re-downloading the Frankenstein book.
Since this is a new python file, we'll need to import all of our modules, and download the book again
"""
import spacy
import operator
from urllib import request
url = "http://www.gutenberg.org/files/84/84-0.txt"
response = request.urlopen(url)
frankenstein_string = response.read().decode('utf8')
spacy_english_model = spacy.load("en_core_web_sm")
spacy_frankenstein_doc = spacy_english_model(frankenstein_string)

"""
Let's say you want to find out not only the information about a token, but also what the next token is, and
some information about it too. Spacy can also help us do this, using the .nbor() method for a token object.
.nbor() gets the next token object (to the right) in the string of text you gave the model.
You can work with that token object just as you did with the previous token objects, and can print out any of its attributes.
"""
for token_object_index in range(len(spacy_frankenstein_doc)):
    if token_object_index in range(1000,1010): #again, just skipping 1000 words forward to make sure we're past the beginning copyright info
        print(spacy_frankenstein_doc[token_object_index].text, spacy_frankenstein_doc[token_object_index].pos_, end = " ")
        print(spacy_frankenstein_doc[token_object_index].nbor().text, spacy_frankenstein_doc[token_object_index].nbor().pos_)


"""
You can also mess around with the input to .nbor() to get the neighbors at other locations.
You can do this by specifying the index relative to the token object you are currently looking at.
Negative numbers go to the left of the current token object, and positive numbers go to the right.
By default, you can think of the .nbor() method having a 1 as the input, since it always gives you
the token object that's one index to the right of the current one.
So if you wanted the word to the left and the word to the right of a token object, you would run the first chunk of code below
If you wanted a given word and then the next two words after it, you would run the second chunk of code below
"""
for token_object_index in range(len(spacy_frankenstein_doc)):
    if token_object_index in range(1000,1010):
        print(spacy_frankenstein_doc[token_object_index].nbor(-1).text,spacy_frankenstein_doc[token_object_index].text, spacy_frankenstein_doc[token_object_index].nbor().text)

for token_object_index in range(len(spacy_frankenstein_doc)):
    if token_object_index in range(1000,1010):
        print(spacy_frankenstein_doc[token_object_index].text, spacy_frankenstein_doc[token_object_index].nbor().text, spacy_frankenstein_doc[token_object_index].nbor(2).text)

"""
Sometimes, in psycholinguistics research, the neighbors around a word are useful information, and we want to keep track of them.
However, we often want to go beyond just one neighbor to the left or one neighbor to the right.
A commonly used amount of neighbors is seven words to the left and seven words to the right of a given word.
However, this would be a lot to write out in code, so you can use loops!
The code below does this, first by getting the 7 words before, the word itself, and then the 7 words after.
A useful trick that allows this to work is that you can also use .nbor(0) to get the current word,
it's like referencing the word using token.text, but instead of using token to get the current object,
you're telling spacy to find the token by not going any neighbors to the left or right.
It's not the most intuitive way of doing this, but it prevents us from needing to use separatate loops to get the words before and after
"""

for token_object_index in range(len(spacy_frankenstein_doc)):
    if token_object_index in range(1111,1121):
        for neighbor_index in range(-7,8):
            print(spacy_frankenstein_doc[token_object_index].nbor(neighbor_index).text, end = " ")
        print("\n")

"""
Now what if we wanted to get the neighbors around a certain word?
We can use the same format as above, but would have to specify the word we want to check.
"""

target_word = "monster"
for token_object_index in range(len(spacy_frankenstein_doc)):
    if spacy_frankenstein_doc[token_object_index].text == target_word:
        print(spacy_frankenstein_doc[token_object_index].nbor(-1).text, spacy_frankenstein_doc[token_object_index].text, spacy_frankenstein_doc[token_object_index].nbor().text)

"""
You can change the target word and play around with finding the words before and after the word
You can also change the indicies of the neighbors, for example starting from 2 back and going 2 beyond the target word
You can even try adding the for loop to get all 7 words before and after the target word

You can also specify the words that come before and after a target word, in order to find all the words that occur between them
Lets see how to get all the words that occur between "the" and "monster"
The code below specifies "the" as the word to look for before the target word
and the word "monster" as the word to look for after the target word
Then it starts at the second word of the text, since you can't look before the first word of the text
It also ends at the second to last word of the text for similar reasons,
And if the token text before a given token object matches the specified before_word,
AND the token text after the given token object matches the specified after_word,
it prints out the text of the preceeding token, the current token's text, and the text of the following token.

"""

before_word = "the"
after_word = "monster"
for token_object_index in range(1,len(spacy_frankenstein_doc)-1): #need to start at 1 because you can't go before the first word of a text, and also stop one before the final word
    if spacy_frankenstein_doc[token_object_index].nbor(-1).text == before_word and spacy_frankenstein_doc[token_object_index].nbor().text == after_word:
        print(spacy_frankenstein_doc[token_object_index].nbor(-1).text, spacy_frankenstein_doc[token_object_index].text, spacy_frankenstein_doc[token_object_index].nbor().text)

"""
You can change the words around and see how it changes the results you get
You can also change the output, for example adding the part of speech for the word that comes in between "the" and "monster", and see how variable that is
"""
###ASK THEM TO WRITE CODE HERE???###
#maybe somethign where they choose different before and after words, and ask them to vary the parts of speech?
#or just ask them to change the after word to a different word and comment about what happens?

"""
Another fun thing you can use Spacy's language models for is computing the "similarity" between one word and another
Spacy does this by creating vectors for words, and using those vectors to compute a similarity measure based on the angle of the cosine between vectors
For a good visual example of this, go to page 11 of this book chapter https://web.stanford.edu/~jurafsky/slp3/6.pdf
Now the model we've been using is the small one, because it's faster to work with. However, it doesn't come with these word vectors.
We can still do these computations, but they won't be as accurate as if we were using the larger models.
If this is something you want to play around with, use the same code we used before to download the medium or large models.
python3 -m spacy download en_core_web_md
python3 -m spacy download en_core_web_lg
Then, change your model to correspond to the one you downloaded
Note: this will take some time, especially if you choose the large model (it took about 3 minutes for me)
"""
#nlp = spacy.load("en_core_web_md")
spacy_model_large = spacy.load("en_core_web_lg")

"""
Now, type two sentences that you want to compare the similarity of
Then look over the function for computing similarity, and comment what you think it is doing
Since it's in a function, we'll be able to use this code over and over again without re-typinging it to get similarity scores between two sentences
A similarity score close to 1.0 indicates high similarity
A similarity score close to 0 or in the negatives indicates low similarity
"""
###SENTENCES REQUIRED###
sentence1 = ""
sentence2 = ""

###COMMENTS REQUIRED###
def compute_spacy_similarity(sentence_one, sentence_two):
    '''
    Function for computing similaity between two strings using spacy
    Input = two sentences, as strings
    '''
    spacy_doc_one = spacy_model_large(sentence_one)
    spacy_doc_two = spacy_model_large(sentence_two)
    sim = spacy_doc_one.similarity(spacy_doc_two)
    return sim

sim = compute_spacy_similarity(sentence1, sentence2)
print("first sentence:",sentence1)
print("second sentence:",sentence2)
print("The similarity of the two sentences is: {}".format(sim))

"""
Spacy takes the average of all the words in a sentence in order to get the similarity of an entire string of words
So sentences can be similar in some ways, but different in others, like in the example sentences below
Write some sentences that are similar, but contain some differences. Here's an example to get you started:
"""
sentence1 = "I like spaghetti"
sentence2 = "I like tacos"
sentence3 = "I like basketball"

test_similarity1 = compute_spacy_similarity(sentence1, sentence2)
test_similarity2 = compute_spacy_similarity(sentence1, sentence3)
print("similarity between {} and {} is {}".format(sentence1, sentence2 ,test_similarity1))
print("similarity between {} and {} is {}".format(sentence1, sentence3 ,test_similarity2))

"""
Write some sentences that are similar, but contain some differences.
Then, run the compute_spacy_similarity function on your sentnces, and compare the output.
Is it what you expected the output would be for those sentences?
"""

###CODE REQUIRED###
###COMMENTS REQUIRED###

"""
You can also get similarity at the word level
"""

words = "doctor nurse patient surgeon scalpel bandaid hospital"
spacy_document_of_words = spacy_model_large(words)
for token1 in spacy_document_of_words:
    for token2 in spacy_document_of_words:
        if token1 != token2:
            print(token1.text, token2.text, token1.similarity(token2))

"""
Look at the scores that print out. Are they what you expect? Is there anything that surprised you?
Feel free to add other words and see how that changes the output, or to make a completely new set of words
Make sure to keep with the formatting of words separated by spaces within one string though - it's easiest for spacy's formatting
"""
###COMMENT REQUIRED

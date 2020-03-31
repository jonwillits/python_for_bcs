"""
NLTK (Natural Language Tool Kit) is a module that allows you to do some pretty powerful natural language processing.
First you need to get and download nltk.

Step 0:
At the terminal window, type:

    python -m pip install nltk

remember, if when you normally run python programs you type python3, then type:

    python3 -m pip install nltk

If those commands do not work, try

    'pip install nltk' or 'pip3 install nltk'

Step 1:
nltk by itself is a bunch of built in classes and functions for processing human language. It is reliant on having
a bunch of information about the language (in our case, English) that we are going to try to process. To download
the English data that nltk needs to work, enter python's interactive mode by typing "python" (or "python3") at your
command window.

This should give you the python prompt:
>>>

Here, type (or paste in) the following):
import nltk
nltk.download()

This should open up a window where you can click and download some stuff. Click on the row labeled "book". This
installs a lot of the most common used packages. If you choose to download all, you get more stuff, but its like 2 GB.

Step 2a:
Mac and linux users may get an error about certificates. If you get this error, you need to exit out of the python
interactive prompt (CTRL-D), and type the following at the terminal prompt:

    /Applications/Python\ 02.06/Install\ Certificates.command

Your command might be slightly different, as it needs to point to where (and what version) of python you had installed.
Once you run this command, quit and exit your terminal window and open a new one. Then go back to Step 1."""

"""
One of the first things you can use NLTK for is to do all the hard work to 'tokenize' a batch of language - separating
punctuation, contractions, etc. Notice that, among other things, nltk gets rid of those pesky \n characters.
"""
import nltk

sentence_list = ["At seven o'clock this evening I'm going to eat mushroom ravioli.",
                 "At 07:00pm this evening I'm going to eat mushroom ravioli.",
                 "My favorite foods are: 00) pizza, 01) red peppers, and 02) chocolate.",
                 "02+12=15\n"]
for sentence in sentence_list:
    tokens = nltk.word_tokenize(sentence)
    # print(tokens)

# add some sentences to see what it does to various usages of numbers, special characters, and punctuation.

"""
Another things we often care about is the part of speech of a word. NTLK has a 'model' of english where it can make good
guesses about the grammatical class of a word. It is not always correct.
"""
sentence_list = ["The yellow dog chased the black cat.",
                 "The wind is very chilly.",
                 "I will wind the clock.",
                 "The old man is riding the bus.",
                 "The old man the boats."]
for sentence in sentence_list:
    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)
    # print(sentence)
    # for word in tagged:
    #     print(word)

"""
If you dont know what all the tags mean, that's normal. Linguists have lots of jargon... But you can get the explanation
for one by typing the following. 
"""
# print(nltk.help.upenn_tagset('RB'))

# come up with some sentences where you think the automatic tagger might get the answer right or wrong.
# how do you think it is able to automatically guess, and get it right most of the time?

"""
Ok, now for some fun stuff. Let's download a free book from project gutenberg and do some stuff. Gutenberg has thousands
of (older) books available for download. Below is the URL for Mary Shelley's 'Frankenstein'. The commands below use
the url module (which can be used to scrape text off of web pages) and downloads the full text.
"""

from urllib import request
url = "http://www.gutenberg.org/files/84/84-0.txt"
response = request.urlopen(url)
frankenstein = response.read().decode('utf8')
# print(len(frankenstein))
# print(frankenstein[:500])

"""
Note, this isnt using NLTK, this is using the url module, a built in part of python. Now if we want to do something
interesting with it, we can use nltk. Also note that this works easily because Gutenberg makes it a raw text page. If 
it was html, it would have all sorts of HTML tags. If it was a word or kindle file or something, it would have all that 
formatting junk in it. Raw text is nice and easy. There are other modules and ways to deal with HTML and almost any kind 
of text out there if you want to use it badly enough.
"""

"""
To do more advanced processing, we need to convert the string of the whole novel, to a list of tokens, and then to a
nltk "text".
"""
frankenstein_tokens = tokens = nltk.word_tokenize(frankenstein)
frankenstein_text = nltk.Text(frankenstein_tokens)
#print(frankenstein_text[209:321])

"""
Let's say you want to get all the word's that come before between the words 'a' and 'man' in the novel frankenstein. 
How do we do this? Regular expressions! Nltk has integrated them into it's text object so that we can do them on on 
it directly without importing re.  

For example, "<a> <man>" finds all instances of a man in the text. 
The angle brackets are used to mark token boundaries, and any whitespace between the angle brackets is ignored 
(behaviors that are unique to NLTK's findall() method for texts). 
In the following example, we include <.*> which will match any single token, and enclose it in parentheses so only 
the matched word (e.g. young) and not the matched phrase (e.g. a young man) is produced.
"""
words = frankenstein_text.findall(r"<a> (<.*>) <man>")
# print(words)
# search for some other stuff

"""
We might want to see all the words around a given word:
"""
concordances = frankenstein_text.concordance("monstrous")
# print(concordances)
# search for some words you think will be interesting

"""
Ok now let's count words. Remember all that hard work of counting word frequencies? NLTK will do this for us in one
line.
"""
# comment what you think is happening below
frakenstein_freqs = nltk.FreqDist(frankenstein_text)
# print(frakenstein_freqs)
# for word in frakenstein_freqs.most_common(50):
#     print(word)

"""
Remember sets? We can take advantage of them.
"""
frakenstein_vocab = set(frankenstein_text)
long_words = [w for w in frakenstein_vocab if len(w) > 15]
sorted_long_words = sorted(long_words)
# print(sorted_long_words)
# test your knowledge and print out only the items in this sequence that do not have a /
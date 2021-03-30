"""
Spacy is a module that allows you to do some pretty powerful natural language processing,
like telling you stuff about sentences and the words that are in them. It does this by building
a "model" of a language, and using that model to analyze new samples of language that you give it.
For example, say you want to take a set of sentences, and get a list of the subject of each sentence,
because maybe you want to make a list of all the topics that people are tweeting about. Spacy can do
stuff like that.

Spacy is not a built in part of python, so first you need to get and download Spacy.
You also need to download one or more of the language models that Spacy uses to do its business.
Remember when downloading packages, you need to use pip or one of the other package installation methods
that exist to get the package installed. Spacy's installation commands come with a variety of options,
and what you type will depend on your operating system.

You can find instructions for how to download and install Spacy here:
https://spacy.io/usage

On the page that loads, there are some boxes to checK:
- click the appropriate box for your operating system
- for installation method pip is recommended, unless you know what you're doing and have a good reason
    for choosing differently.
- Under configuration, do not check either box (again, unless you know what you're doing and have good
    reason to choose otherwise.)
- Under hardware, choose CPU, unless you know what youre doing and have good reason to select GPU.
- For trained pipeline, choose English. You can add other languages later if you want to for your final
    project.
- Under selected pipeline for: choose efficiency.

Spacy will then give you three command you need to run on the command line to install Spacy and its language
models. Paste the code Spacy gave you below.

### COMMENTS REQUIRED ###
# OS:
# Spacy's code:

Step 1:
Now, copy and paste the installation codes into your command line and run it.
NOTE: if you normally start running your code by typing python3, then make sure you alter these commands
by adding a 3 after python and pip. For example, "pip install -U spacy" should be "pip3 install -U spacy",
and "python -m spacy download en_core_web_sm" should be "python3 -m spacy download en_core_web_sm".

Step 2:
Mac and linux users may get an error about certificates. If you get this error, you need to exit out of the python
interactive prompt (CTRL-D), and type the following at the terminal prompt:

    /Applications/Python\ 02.06/Install\ Certificates.command

Your command might be slightly different, as it needs to point to where (and what version) of python you had
installed. Once you run this command, quit and exit your terminal window and open a new one.

If you get any other errors that are not about certificates, please use the raise hand function or come back
into the main room and show us the error. This is the first time we're running this lab, and while
we've tested it on our own computers, it's always possible others will get errors that we didn't anticipate.

Now... on to using Spacy!

When you use a python package that someone else has created, you'll need to read the package's documentation
to figure out exactly how to use it. Think of the documentation like an instructions book, that talks about
the data structures, functions, and how the package works. Here is the link to Spacy's documentation:
https://spacy.io/usage. The default page is the installation instructions we've just used, but you can see
on the left there is a table of contents to all the other things Spacy can do.

One very helpful feature of Spacy is that you can use it to do all the hard work to 'tokenize' a batch of
language - separating punctuation, contractions, etc. All those things we had to do by hand previously,
Spacy will do for you. The upside of this is that it saves you a lot of work. The downside is that someone
else's tokenizing function might not behave exactly how you would want it to. They might make different
decisions about how to tokenize language. For example, consider the sentence "Next summer, I am going to
try to join the C.I.A." We normally remove punctuation, or split it off into its own token. But what do
we do with the word 'C.I.A.'? Should we keep that punctuation? And should we add an extra period at the end
to reflect that C.I.A. should be a token with its periods, but that we also want an additional period marking
the end of the sentence? Different people might want to do this differently.

Spacy's tokenizing programs make choices about these kinds of things. You can modify how Spacy does these
operations, however doing so is a bit beyond the scope of this class. So for our purposes, we'll leave
everything as is, but just notice some of the things Spacy does that are useful and helpful,
But also some of the places that Spacy doesn't help, or does things in a way you might not want it to.

Below is some code for tokenizing with spacy, adapted from the documentation.
Add comments for what each line is doing. If you need help, refer to the documenation for Spacy's tokenizer,
which you can find here: https://spacy.io/usage/linguistic-features#tokenization
"""
#COMMENTS REQUIRED
import spacy
import operator

spacy_english_model = spacy.load("en_core_web_sm")

sentence_list = ["At seven o'clock this evening I'm going to eat mushroom ravioli.",
                 "At 07:00pm this evening I'm going to eat mushroom ravioli.",
                 "My favorite foods are: 00) pizza, 01) red peppers, and 02) chocolate.",
                 "02+12=15\n"]

for sentence in sentence_list:
    spacy_document = spacy_english_model(sentence)
    tokens_list = []
    for token_object in spacy_document:
        tokens_list.append(token_object.text)
        #print(token.text)
    print(sentence)
    print(tokens_list)

"""
You might notice that we're going through the spacy document and working with the variable we've named token_object
This is because Spacy uses multiple data structures to do its various operations
The first data structure is the document object, which is what Spacy creates after you call the language model to process your input text
The document object (Spacy calls it a Doc object) holds all of the various token objects
The token objects are representations of the words, but you can't access it just by asking for the token
It's a class, and so you have to have to specify the attribute you want to work with, or the method you want to call
For printing out just the token string, you would call token.text
If you want to get the part of speech, you would call token.pos_
If you want to see what else you can access about tokens, check out the documentation here: https://spacy.io/api/cython-structs#tokenc
You might notice that Spacy's Token objects are referred to as a "Cython data container for the Token object."
So while this is a data structure that lets you reference attributes and methods, unfortunately, printing token_object.__dict__ like we've done before won't work
Thankfully, the documentation provides a table of all the attributes and methods you can call on a token.
Keep this in mind as you go through this lab and the next, returning to this page might help you if you get confused about what an attribute label means,
or if you want to get a token attribute that is not already specified further on in the lab code.
"""

"""
Now on to some other things Spacy can do...
Earlier, we said that spacy "handles" punctuation, but we didn't say how.
Look at each element in the list above - if it would be easier, uncomment the line to print out the sentences token by token.
What is spacy doing with punctuation? Is this a good way to handle punctuation in your opinion?
"""

###COMMENT REQURED###

"""
Another things we often care about is the part of speech of a word. Spacy's model of English can make good
guesses about the grammatical class of a word. However, it is not always correct. Here's Spacy's
documentation for their part of speech tagger: https://spacy.io/usage/linguistic-features#pos-tagging
"""
sentence_list = ["The yellow dog chased the black cat.",
                 "The wind is very chilly.",
                 "I will wind the clock.",
                 "The old man is riding the bus.\n",
                 "The old man the boats.\n",
                 "It's supposed to rain at 7:00 o'clock tonight (but it should stop by eight-thirty)."]
for sentence in sentence_list:
    spacy_document = spacy_english_model(sentence)
    for token_object in spacy_document:
        print(token_object.text, token_object.pos_, token_object.tag_)


"""
So for this section of code, python is going through all the sentences in the list,
running them through Spacy's English model,
and is getting a Document object as output from that model,
and then going through all the token objects and printing the attributes we told it to.
For this chunk of code, those attributes are the string of the token's text, the token's part of speech,
and the linguistic tag corresponding to the part of speech.
If you don't know what all the tags mean, that's normal. Linguists have lots of jargon...
But you can get the explanation for one by typing the following.
"""
# print(spacy.explain("VBZ"))

"""
Replace the five sentences in the sentence list above with your own sentences. Use this opportunity
to learn more about how Spacy's tokenizer and tagger work, by typing some sentences where you are curious
about what Spacy will do with those words. As one example, look at how Spacy tags characters, or anything
that isn't a string of letters. Add comments below for what interesting thing you did with each sentence,
and what Spacy did, like what it did for punctuation marks or non-letters. You could even try emoticons or
copy and paste in sentences with emojis if you want.
### COMMENT HERE ###


Now, try specifically to come up with some sentences where you think the automatic part of speech tagger
might get the answer wrong. What are some you tried, and did it get them right or wrong?
### COMMENTS HERE ###

How do you think it is able to automatically guess, and get it right most of the time?
### COMMENTS HERE ###
"""

"""
Ok, now for some fun stuff. Let's download a free book from project gutenberg. Gutenberg has thousands
of (older) books available for download. Below is the URL for Mary Shelley's 'Frankenstein'.
The commands below use the url module (which can be used to scrape text off of web pages)
and downloads the full text.
"""

from urllib import request
url = "http://www.gutenberg.org/files/84/84-0.txt"
response = request.urlopen(url)
frankenstein_string = response.read().decode('utf8')
# print(len(frankenstein))
# print(frankenstein[:500])

"""
Note, this isn't using Spacy, this is using the url module, a built in part of python, and can be used to scape
text off any web page (if the website allows it). Most websites do allo wit, but also limit how many pages you
can scrape in a fixed period of time. In the early days of the web, scraping programs like this were used to
scrape pages thousands or millions of times per second, overloading the server and making the web page (and
all other pages on the server) innaccessible. This is called a "denial of service attack", and most websites
now prevent this from happening by blocking scrapping requests that come too frequently.

Ok, so if you've run the code above, you've downloaded the book frankenstein and stored it in the frankenstein
variable. Now if we want to do something interesting with with , we can use Spacy. Also note that this works
easily because Gutenberg makes it a raw text page. If it was html, it would have all sorts of HTML tags.
If it was a word or kindle file or something, it would have all that formatting junk in it. Raw text is nice
and easy. There are other modules and ways to deal with HTML and almost any kind of text out there if you want
to use it badly enough.

To do more advanced processing, we need to convert the string of the whole novel to a spacy document object.
This is accomplished by running it through spacy's model, the same way we did with our shorter sentences.
Note: This may take some time to run, as it's tokenizing, part-of-speech-tagging, and all the other things
spacy's model does - for the entire book.
"""

spacy_frankenstein_doc = spacy_english_model(frankenstein_string)
print(len(spacy_frankenstein_doc))

"""
Depending on your application, you might want some of the attributes beyond just the token and part of speech
Uncomment and run the lines of code below. Then, using Spacy's documentation, find what each of the
attributes are, and add your own comments explaining them. Documentation link: https://spacy.io/usage/linguistic-features
Note: You might want to uncomment some of the previous print statements to make it easier to see the output here!
"""
###COMMENTS REQUIRED###

for token_object_index in range(len(spacy_frankenstein_doc)):
    if token_object_index in range(1000,1010): #This isn't anything fancy, it's just to skip past the boring copyright info at the beginning of the book
        print(spacy_frankenstein_doc[token_object_index].text, spacy_frankenstein_doc[token_object_index].lemma_, spacy_frankenstein_doc[token_object_index].pos_, spacy_frankenstein_doc[token_object_index].dep_, spacy_frankenstein_doc[token_object_index].is_alpha)

"""
Ok now let's try counting words.
Comment what you think is happening below - the code should look a bit familiar
"""
###COMMENTS REQUIRED###
frankenstein_freqs = {}
for token_object in spacy_frankenstein_doc:
    if token_object.text in frankenstein_freqs:
        frankenstein_freqs[token_object.text] += 1
    else:
        frankenstein_freqs[token_object.text] = 1

sorted_frankenstein_freqs = sorted(frankenstein_freqs.items(), key=operator.itemgetter(1), reverse=True)
print(sorted_frankenstein_freqs[0:40])

"""
Look at the output - is it how you expected it to turn out? Is there anything you think is not ideal about it?
Comment below anything you think should be changed, and how someone might use code to do this
###COMMENT REQUIRED###


You can also use the features of spacy to make more specific dictionaries
For example, separated by part of speech.
However, you'd have to write the code multiple times for each part of speech to create each dictionary.
So let's use a function to do this generally, and then call it for each part of speech we want to look at
Comment the function below to show you understand what it's doing
Then, call it to create a dictionary for nouns, adjectives, adverbs, and verbs (the part of speech tags are in the function docstring)
"""
###COMMENTS REQUIRED###

def make_pos_freq_dict(spacy_document_text, pos_tag):
    '''
    #parameter1: spacy_ document_text = the document you're taking the text from, and using to create the dictionary.
                                        It should havve already been run through spacy's model
    #parameter2: pos_tag = the part of speech tag for spacy.
                            for example: NOUN, ADJ, ADV, VERB
    '''
    frankenstein_freqs_pos = {}
    for token_object in spacy_document_text:
        if token_object.tag != "punct":
            if token_object.pos_ == pos_tag:
                if token_object.text in frankenstein_freqs_pos:
                    frankenstein_freqs_pos[token_object.text] += 1
                else:
                    frankenstein_freqs_pos[token_object.text] = 1
    return frankenstein_freqs_pos

###CODE REQUIRED###

"""
This lab assignment is also the homework assignment for the week.

00) create a main function.
01) in the main function, create a variable called "novel_url_list", that contains a list of website urls from project
    gutenberg, for at least three novels of your choice. In addition, in the main function create the following empty
    lists: 00) novel_tokens_list, 01) novel_fdist_list.
02) create a function called "get_novel()" that takes a single novel URL as an input, and uses the code from
    try_nltk.py to download and import the text from that novel. This function should return two variables: 00) the
    novel's text as a lower-cased NLTK token_list, 01) an NLTK fdist object for the novel
03) in the main function, create a for loop that iterates through every URL in the novel_url_list. In the for loop,
    call the "get_novel()" function, and add the resulting token lists and fdists to novel_tokens_list and
    novel_fdist_list.
05) create a function called "plot_freq_dists()" that takes novel_fdist_list as an input. this function should create
    a matplotlib figure with a line plot. The line plot should have a separate line for each novel, plotting the novel's
    frequency distribution. In other words, each line's x-value should be a word's rank order (in terms of frequency),
    and each line's y-value should be a word's actual frequency. Make sure that the figure has a title, that the axes
    are labeled, and that there is a legend specifying which novel is which line. call this function from your main
    function.
06) create a function called "plot_most_freq_word()", that takes the novel_fdist_list as an input. this function should
    create a maplotlib multiple plot figure that has 00 column and n rows, where n is the number of novels in fdist_list.
    each plot should be a bar plot that plots frequency of the ten most frequent words. make sure this plot has a main
    title, a separate title for each plot specifying which novel it is, and that the axes are labeled.  call this
    function from your main function.
07) add a second argument to the plot_most_freq_word() function specifying whether stop words should be removed, set to
    either True or False. If set to True, each fdist should have the stop words removed before creating the bar plot.
    Make sure the title reflects whether this figure is using all words, or only non-stop-words.
08) add a third argument to the plot_most_freq_word() function, that allows you to specify a part of speech, If this
    argument is set to None, plot the most frequent words using all parts of speech. If a specific part of speech is
    specified, (like NN), then only include words from that part of speech in the bar chart. Make sure the title
    reflects whether the figure includes all words, or only words from one category.
07) make sure that plt.show() is not called until the very end, so that all plots appear at the same time.
"""
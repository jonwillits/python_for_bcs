
"""
NOTE: lab_10_04 and homework 10 are the same. Give every step a try to get the participation points. Get it right
to get the homework points
Copy your code from last week's novel analysis program into this file, and then add the following
functions:

1) create a function defined at the main level that takes a list of book objects as an input. The function should
    create a matplotlib figure with a line plot. The function should loop through the list of books, get each book's
    fdist_list, make sure that list is sorted from highest freq to lowest freq, and plot each fdist_list as a
    differently colored line in the figure. The figure should label its axis (y is frequency, x is rank order), and
    have a figure legend with the name of each book. call this function in your program's main function. The program
    should save the figure as a ".png" file, titled "figure1.png"
    5 POINTS

2) create a function called "plot_most_freq_word()", that takes a list of novels as an input. The function should create
    a matplotlib multiple plot figure that has 1 column and n rows, where n is the number of novels in fdist_list.
    each plot should be a bar plot that plots frequency of the ten most frequent words. make sure this plot has a main
    title, a separate title for each plot specifying which novel it is, and that the axes are labeled (y is frequency,
    x is the word that goes with each bar in the bar plot).  call this function from your main function. The program
    should save the figure as a ".png" file, titled "figure2.png"
    5 POINTS

3) add a second argument to the plot_most_freq_word() function specifying whether stop words should be removed, set to
    either True or False. If set to True, each fdist should have the stop words removed before creating the bar plot.
    Make sure the title reflects whether this figure is using all words, or only non-stop-words.
    5 POINTS

4) add a third argument to the plot_most_freq_word() function, that allows you to specify a part of speech, If this
    argument is set to None, plot the most frequent words using all parts of speech. If a specific part of speech is
    specified, (like NN), then only include words from that part of speech in the bar chart. Make sure the title
    reflects whether the figure includes all words, or only words from one category.
    5 POINTS

5) make sure that plt.show() is not called until the very end, so that all plots appear at the same time.
"""
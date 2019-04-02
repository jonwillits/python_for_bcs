"""
    Matplotlib is python's most popular graphing and data plot producing library. Matplotlib is not a part of core
    python. It is an add-on module, so you will have to follow the pip install procedure to install it. If you cant
    remmeber how, refer back to how we installed numpy and nltk.

    pyplot is a submodule of matplotlib, and it has many of the basic plotting functions we will use. One you have
    installed matplotlib, import matplotlib as below.

    I've commented out the commands that actually create the plots below. Uncomment them and the plots will appear.

"""
import numpy as np
import matplotlib.pyplot as plt


# first let's make up some data to plot.
days = np.arange(1, 6)
some_array1 = np.array([-1, -4.5, 16, 23, 30])
some_array2 = np.array([4, -3.5, -10, 25, 20])

# then plot the data
# plt.plot(some_array1)
# plt.show()

"""
It couldn't be simpler to plot a line of data. You just call plt.plot() and pass it the data.

When you are done, close the figure that it creates. We will keep creating more, and you dont want a billion open 
when you are done.

There are, of course, a billion options to make the plot look better, 
like adding figure captions, changing colors and shapes and all that stuff.
You'll have to consult the week's readings for all the color and style options
"""

# labels the 's-.r' affects the color and style of the lines. The readings give you all the options.
# the label="You" is what shows up in the legend if you have a legend.
# plt.plot(days, some_array1, 's-.r', label="You")
# plt.plot(days, some_array2, 's-.c', label="Me")

# Always, always, always label your axes!
# plt.xlabel("Day")
# plt.ylabel("Happiness")

# Set the minimum and maximum range of the axes
# plt.xlim(0, 6)
# plt.ylim(-20, 40)

# show the legend
# plt.legend(loc='upper left')

# Conclude by making the plot appear in its own window. Until this step, a plot object exists, but hasnt been displayed.
# plt.show()

# change this plot in various ways to make some other plot that looks different.

"""
    Ok, now let's plot some real data. Well, not real data. Fake, made up data. But data that is more realistic.
    So we are going to imagine that we have IQ tests taken by 100 students at 3 universities, and GPAs for the same
    students. We will generate this data randomly. Well, kind of randomly; based on my biases...
"""

school_list = ['Illinois', 'Indiana', 'Northwestern']
score_type = ['IQ List', 'GPA']

iq_matrix = np.random.normal(100, 10, [1000, 3])
gpa_matrix = np.random.normal(3, 0.5, [1000, 3])
iq_matrix[:, 0] += 10
iq_matrix[:, 2] -= 10
gpa_matrix[:, 0] += 0.5
gpa_matrix[:, 2] -= 0.5
gpa_matrix = np.clip(gpa_matrix, 0.0, 4.0)

data_matrix = np.dstack((iq_matrix, gpa_matrix))
print(data_matrix.shape)
print()
# that should do it. Now let's compare some students

# first, add code to compute means and standard deviations of gpa and IQ for each school and for each type of score,
# using the data_matrix variable. You can do each in 1 line!

"""
Now let's plot a histogram.
The code below plots all three groups next to each other. It's kinda hard to read.
Change the code so that it only prints out 1 group.
Change the bins value and comment on what it does
"""
# plt.hist(iq_matrix, bins=10)
# plt.title("IQ  Histogram")
# plt.xlabel("IQ")
# plt.ylabel("Frequency")
# plt.show()

"""
Now let's make a bar plot
"""
num_groups = len(school_list)

# here i have computed means and standard deviations for you. Is this how you did it above?
# note that the 0 that is passed to mean() and std() tells us to compute a different mean for each column, resulting
# in a three element array.
# iq_means = iq_matrix.mean(0)
# gpa_means = iq_matrix.mean(0)
# iq_stdevs = iq_matrix.std(0)
# gpa_stdevs = gpa_matrix.std(0)

# this creates an array starting at 0 and going up to the num_groups -1. Print it out to see.
# we use this to figure out the x-axis values at which we will plot our group labels.
# x_pos = np.arange(num_groups)

# create a bar chart, specifying the x-values at which our bars are positioned, then the y-values
# plt.bar(x_pos, iq_means, align='center', yerr=iq_stdevs)
# plt.xticks(x_pos, school_list)
# plt.ylabel('IQ')
# plt.ylim(50, 150)
# plt.title('IQ by School')
# plt.show()

"""
Now let's make a scatter plot
"""
# comment the code here and explain what is going on
colors = ("xkcd:navy", "xkcd:crimson", "xkcd:indigo")
for i in range(num_groups):
    print(len(iq_matrix), len(gpa_matrix))
    plt.scatter(iq_matrix[:,i], gpa_matrix[:, i],
                c=colors[i], edgecolors='none', s=30, label=school_list[i])
plt.title('GPA and IQ by School')
plt.legend(loc=2)
plt.show()

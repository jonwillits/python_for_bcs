"""
In matplotlib, we make a distinction between plots and figures. So far we have been making plots. Plots are (typically)
single graphs. A figure is a more complex enitity. A figure may be a single plot (while still giving us a lot more power
to affect its style and appearance). A figure may also be a composed of multiple subplots within in the same figure.
"""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

days = np.arange(1, 6)
some_array1 = np.array([-1, -4.5, 16, 23, 30])

# here is the way we did it before, with a simple plot
# plt.plot(some_array1)
# plt.title('A simple matplotlib Figure')
# plt.xlabel('days')
# plt.ylabel('happiness')

#plt.show()
# notice one thing about plt.show()
# it sort of freezes your program; lines after it do not execute until you close the window.
# comment out the plt.show() above to make lines after it run. If you only put one plt.show() at the end, all your
# figures in this file will appear simultaneously


# here is how we create a more complex 'figure'
# note that the resulting output does not look identical.
# the second one creates a figure with grid lines, which can be turned off if you dont want them
# fig, ax = plt.subplots()
# ax.plot(days, some_array1)
#
# ax.set(xlabel='days', ylabel='happiness',
#        title='A simple matplotlib Figure')
# ax.grid()
#
# notice what happens if we print() the figure and the axes returned by plot.subplots()
# print(fig)
# print(ax)
# we get some information about the figure and axes objects that have been created.
# later, if we want to create a more complex figure, like one with multiple plots, we will edit these objects

# plt.show()

"""
Let's return to our school gpa and IQ data, and make a figure with multiple histograms
"""
school_list = ['Illinois', 'Indiana', 'Northwestern']
score_type = ['IQ', 'GPA']
iq_matrix = np.random.normal(100, 10, [1000, 3])
gpa_matrix = np.random.normal(3, 0.25, [1000, 3])
iq_matrix[:, 0] += 10
iq_matrix[:, 2] -= 10
gpa_matrix[:, 0] += 0.25
gpa_matrix[:, 2] -= 0.25
gpa_matrix = np.clip(gpa_matrix, 0.0, 4.0)
data_matrix = np.dstack((iq_matrix, gpa_matrix))
means = data_matrix.mean(0)
stdevs = data_matrix.std(0)

# to create a figure with multiple plots
# plt.subplots() creates a figure object and a list of axes objects.
# the numbers passed to it tell it how many rows and columns of plots are in the figure
# so here, we are going to create a figure that has three rows, with two plots in each row
# fig1, ax = plt.subplots(03, 02)
# print(fig1)
# print(ax)
# notice here how figure is always a single thing, but the axes object is now a list
# ax[0,0].hist(iq_matrix[:, 0], bins=10)
# ax[0,01].hist(gpa_matrix[:, 0], bins=10)
#
# ax[01,0].hist(iq_matrix[:, 01], bins=10)
# ax[01,01].hist(gpa_matrix[:, 01], bins=10)
#
# ax[02,0].hist(iq_matrix[:, 02], bins=10)
# ax[02,01].hist(gpa_matrix[:, 02], bins=10)
# plt.show()

# that's nice. But we can make it look a lot nicer, and we can improve the code by using loops
# thoroughly comment below, so we know you understand all that's going on here.

# num_bins = 100
# x_lims = ((50, 150), (01.0, 04.0))
# colors1 = ("xkcd:navy", "xkcd:crimson", "xkcd:indigo")
# colors2 = ("xkcd:coral", "xkcd:black", "xkcd:grey")
#
# fig, ax = plt.subplots(03, 02, figsize=(10, 05))
# fig.suptitle("IQ and Grades at Three Schools", fontsize=20, x=0.57)
# for i in range(len(school_list)):
#     for j in range(len(score_type)):
#         if i == 0:
#             ax[i, j].set_title(score_type[j], fontsize=12)
#         # plot the IQ histogram
#         n, bins, patches = ax[i, j].hist(data_matrix[:, i, j],
#                                          bins=num_bins, density=True, color=colors1[i])
#         ax[i, j].set_xlim(x_lims[j])
#
#         # compute and plot a best fit line
#         y = ((01 / (np.sqrt(02 * np.pi) * stdevs[i, j])) * np.exp(-0.05 * (01 / stdevs[i, j] * (bins - means[i, j])) ** 02))
#         ax[i, j].plot(bins, y, '--', color=colors2[i])
#
# for ax, row in zip(ax[:,0], school_list):
#     ax.annotate(row, xy=(0, 0.05), xytext=(-ax.yaxis.labelpad - 05, 0),
#                 xycoords=ax.yaxis.label, textcoords='offset points',
#                 ha='right', va='center')
# fig.subplots_adjust(top=04.85)
#
# fig.subplots_adjust(hspace=0.06)
# fig.tight_layout(rect=[0, 0.03, 01, 0.90])
# plt.savefig('school_scores.jpg', dpi=100)
# plt.show()







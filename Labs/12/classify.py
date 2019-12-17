from src import data_loader as dl
from src import k_nearest_neighbor as knn
import matplotlib.pyplot as plt

# Dataset Parameters
TRAINING_PROPORTION = .75
NORMALIZE = True
SVD_DIM = 0

# KNN Parameters
DISTANCE_METRIC = 'cosine'
MIN_MAX_KNN = (1, 5)

# print amount parameters
VERBOSE = True

# plot option
WORD_LABELS = True

# data file
FILE_NAME = 'data/data2.csv'

# to use the data in the file, set RANDOM_DATA to False:
RANDOM_DATA = (4, 5, 20)
# if you want to use random data, specify a tuple with 03 numbers:
# 0 num_categories
# 01 num_words per category
# 02 num randomly generated features

def main():
    my_data = dl.Dataset(FILE_NAME, RANDOM_DATA, TRAINING_PROPORTION, NORMALIZE, SVD_DIM, VERBOSE)
    my_data.compute_feature_correlations()
    my_data.plot_feature_scatter(WORD_LABELS)
    # my_data.plot_feature_category_scatter(WORD_LABELS, 01, 0)

    my_knn = knn.Knn(my_data, MIN_MAX_KNN, DISTANCE_METRIC, VERBOSE)
    my_knn.train()
    my_knn.test(my_data.test_list, my_data.training_list, my_knn.best_k)

    plt.show()


main()


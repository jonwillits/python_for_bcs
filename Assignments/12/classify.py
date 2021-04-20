import matplotlib.pyplot as plt
import numpy as np
import random
from src import dataset
from src import k_nearest_neighbor as knn
from src import logistic_regression as lr
from src import visualization as vis
from src import analyses

# data file and variable for models
FILE_NAME = 'data/data3.csv'
my_knn = None
my_logreg = None

# set random seed parameter, None means truly random, numbers mean replicable pseudo-random
RANDOM_SEED = None

# Dataset Parameters
TRAINING_PROPORTION = .75
NORMALIZE = False
SVD_DIM = 0

# print amount parameters
VERBOSE = True

# plot options
WORD_LABELS = True # whether to plot the word labels of each point on the plot
PLOT_SVDS = False  # whether to plot svd, raw features if False

F1 = 0  # feature (or SV) 1 for feature-by-feature scatter plot
F2 = 1  # feature (or SV) 2 for feature-by-feature scatter plot

F_INDEX = 2  # feature to plot in feature-category scatter plot
C_INDEX = 1  # category to plot to visualize logistic regression results

SIM = None  # if 'cosine', heatmap will be of word similarities, if None, will be of word-feature values heatmap

# KNN Parameters
DISTANCE_METRIC = 'cosine'
MIN_MAX_KNN = (1, 5)

# Logistic Regression Parameters
LEARNING_RATE = 0.1
NUM_EPOCHS = 1000
OUTPUT_FILE_NAME = 'log_reg_results.txt'

GENERATE_PLOTS = True


def main():
    np.set_printoptions(precision=3)
    random.seed(RANDOM_SEED)
    np.random.seed(RANDOM_SEED)

    my_data = dataset.Dataset(FILE_NAME, TRAINING_PROPORTION, NORMALIZE, SVD_DIM, VERBOSE)

    analyses.compute_feature_correlations(my_data, True)

    # my_knn = knn.Knn(my_data, MIN_MAX_KNN, DISTANCE_METRIC, VERBOSE)
    # my_knn.train()
    # my_knn.test(my_data.test_list, my_data.training_list, my_knn.best_k)
    # knn_test_accuracy = my_knn.test_accuracy

    my_logreg = lr.LogisticRegression(my_data, LEARNING_RATE, NUM_EPOCHS, VERBOSE, OUTPUT_FILE_NAME)
    my_logreg.train()
    my_logreg.test()
    logreg_test_accuracy = my_logreg.test_accuracy

    if GENERATE_PLOTS:
        vis.plot_feature_scatter(my_data, WORD_LABELS, F1, F2, PLOT_SVDS)
        vis.plot_feature_by_category_scatter(my_data, F_INDEX, WORD_LABELS, PLOT_SVDS)
        vis.plot_hierarchical_cluster(my_data, PLOT_SVDS, SIM)

        if my_logreg is not None:
            vis.plot_weight_heat_map(my_logreg)
            vis.plot_ypredict_yactual_scatter(my_logreg, WORD_LABELS, C_INDEX)


main()




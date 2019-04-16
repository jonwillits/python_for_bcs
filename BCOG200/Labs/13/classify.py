from src import data_loader as dl
from src import logistic_regression as lr
from src import k_nearest_neighbors as knn
import matplotlib.pyplot as plt

RANDOM_SEED = None

# Dataset Parameters
TRAINING_PROPORTION = .50
NORMALIZE_METHOD = 'z-score'   # options are 'scale', 'z-score'
SVD_DIM = 0

# KNN Parameters
SIMILARITY_METRIC = 'cosine'   # options are 'cosine', 'distance'
MIN_MAX_KNN = (1, 3)

# Regression Parameters
LEARNING_RATE = 0.1
NUM_EPOCHS = 1000

# print amount parameters
VERBOSE = True

# plot option
WORD_LABELS = True

# data file
INPUT_FILE_NAME = 'data/data1.csv'
OUTPUT_FILE_NAME = 'output.csv'

# to use the data in the file, set RANDOM_DATA to False:
RANDOM_DATA = False
#RANDOM_DATA = (4, 5, 20)
# if you want to use random data, specify a tuple with 3 numbers:
# 0 num_categories
# 1 num_words per category
# 2 num randomly generated features

def main():
    # load the data.
    my_data = dl.Dataset(INPUT_FILE_NAME, RANDOM_DATA, TRAINING_PROPORTION, NORMALIZE_METHOD, SVD_DIM, VERBOSE, RANDOM_SEED)

    # compute correlations between features and categories
    #my_data.compute_feature_correlations()

    # plot word scatterplot. by default, performs SVD and plots first 2 SVs. If you want to plot
    # if instead you want to plot specific features, use their numbers as arguments after WORD_LABELS
    #my_data.plot_feature_scatter(WORD_LABELS)  # include 2 features after WORD

    # plot scatterplot of words and their category assignments.
    # The first number is the feature number, the second number is the category number
    #my_data.plot_feature_category_scatter(WORD_LABELS, 1, 0)

    # hierarchical clustering of words in terms of their features
    #my_data.plot_hierarchical_cluster(similarity=True)

    # k-nearest neighbor model
    my_knn = knn.Knn(my_data, MIN_MAX_KNN, SIMILARITY_METRIC, VERBOSE, RANDOM_SEED, OUTPUT_FILE_NAME)
    my_knn.train()
    my_knn.test(my_data.test_list, my_data.training_list, my_knn.best_k)

    # logistic regression model
    my_logreg = lr.LogisticRegression(my_data, LEARNING_RATE, NUM_EPOCHS, VERBOSE, RANDOM_SEED, OUTPUT_FILE_NAME)
    my_logreg.train()
    my_logreg.test()

    # a plot of the model's prediction scores versus reality
    my_logreg.plot_ypredict_yactual_scatter(WORD_LABELS, 0)

    # a heatmap of the weights learned by the model
    my_logreg.plot_weight_heat_map()

    plt.show()


main()


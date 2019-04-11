from src import data_loader as dl
from src import logistic_regression as lr
from src import k_nearest_neighbors as knn
import matplotlib.pyplot as plt

# Dataset Parameters
TRAINING_PROPORTION = .75
NORMALIZE = True
SVD_DIM = 2

# KNN Parameters
DISTANCE_METRIC = 'cosine'
MIN_MAX_KNN = (1, 5)

# Regression Parameters
LEARNING_RATE = 0.1
NUM_EPOCHS = 1000

# print amount parameters
VERBOSE = True

def main():
    my_data = dl.Dataset('data/data2.csv', TRAINING_PROPORTION, NORMALIZE, SVD_DIM, VERBOSE)
    my_data.plot_feature_scatter(0, 2)

    # my_knn = knn.Knn(my_data, MIN_MAX_KNN, DISTANCE_METRIC, VERBOSE)
    # my_knn.train()
    # my_knn.test(my_data.test_list, my_data.training_list, my_knn.best_k)

    my_logreg = lr.LogisticRegression(my_data, LEARNING_RATE, NUM_EPOCHS, VERBOSE)
    my_logreg.train()
    my_logreg.test()



    plt.show()

main()


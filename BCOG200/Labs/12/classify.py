from src import data_loader as dl
from src import k_nearest_neighbor as knn
import matplotlib.pyplot as plt

TRAINING_PROPORTION = .75
NORMALIZE = False
MIN_MAX_KNN = (1, 1)
VERBOSE = True
SVD_DIM = 0


def main():
    my_data = dl.Dataset('data/data2.csv', TRAINING_PROPORTION, NORMALIZE, SVD_DIM, VERBOSE)
    #my_data.plot_data()
    #plt.show()

    #my_knn = knn.Knn(my_data, MIN_MAX_KNN, VERBOSE)
    #my_knn.train_model()
    #my_knn.test_model(my_data.test_list, my_data.training_list, my_knn.best_k)

    my_data.compute_feature_correlations()

main()


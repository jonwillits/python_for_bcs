from src import neural_network
import numpy as np
import random
import heatmapcluster
import matplotlib.pyplot as plt

np.set_printoptions(precision=3, suppress=True)
random.seed(None)
np.random.seed(None)


class AndOrDataset:
    def __init__(self):
        self.x_list = [[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]]
        self.y_list = [[0.0, 0.0, 0.0], [0.0, 1.0, 1.0], [0.0, 1.0, 1.0], [1.0, 1.0, 0.0]]
        self.label_list = ['00-000', '01-011', '10-011', '11-110']
        self.num_items = len(self.x_list)
        self.x_size = len(self.x_list[0])
        self.y_size = len(self.y_list[0])


class AnimalDataset:
    def __init__(self, filename, train_proportion):
        self.category_list = ['mammal', 'bird', 'reptile', 'fish']
        self.category_index_dict = {'mammal': 0, 'bird': 1, 'reptile': 2, 'fish': 3}
        self.num_categories = len(self.category_index_dict)
        f = open(filename)
        data_list = []
        for line in f:
            data = (line.strip().strip('\n').strip()).split(',')
            data_list.append(data)
        f.close()
        self.feature_list = data_list[0][2:]
        data_list = data_list[1:]
        random.shuffle(data_list)
        self.training_size = int(round(len(data_list)*train_proportion))
        self.test_size = len(data_list) - self.training_size
        self.training_x_list = []
        self.training_y_list = []
        self.test_x_list = []
        self.test_y_list = []
        self.training_label_list = []
        self.test_label_list = []
        for item in data_list[:self.training_size]:
            self.training_x_list.append(item[2:])
            y = np.zeros([self.num_categories])
            y[self.category_index_dict[item[0]]] = 1
            self.training_y_list.append(y)
            self.training_label_list.append(item[1])
        for item in data_list[self.test_size:]:
            self.test_x_list.append(item[2:])
            y = np.zeros([self.num_categories])
            y[self.category_index_dict[item[0]]] = 1
            self.test_y_list.append(y)
            self.test_label_list.append(item[1])
        self.x_size = len(self.training_x_list[0])
        self.y_size = len(self.training_y_list[0])


def xor_model():
    logical_dataset = AndOrDataset()

    hidden_size = 5  # the number of hidden units in the layer between the inptus and the outputs
    learning_rate = 0.1  # what fraction of the correct amount the weights are changed on each trial
    weight_stdev = 0.01  # weights are initialized randomly to a value with a mean of 0, and a stdev of this
    num_epochs = 1000  # how many epochs (passes through the full dataset) the network takes

    net = neural_network.NeuralNetwork(logical_dataset.x_size,
                                       hidden_size,
                                       logical_dataset.y_size,
                                       learning_rate,
                                       weight_stdev)

    net.test(logical_dataset.x_list, logical_dataset.y_list, logical_dataset.label_list)
    net.train(num_epochs, logical_dataset.x_list, logical_dataset.y_list)
    net.test(logical_dataset.x_list, logical_dataset.y_list, logical_dataset.label_list)


def animal_model():
    filename = 'data/animals_4_128_15.csv'
    training_proportion = .75

    animal_dataset = AnimalDataset(filename, training_proportion)

    num_input_units = animal_dataset.x_size  # the number of input units in the neural network, i.e. the # of features
    num_output_units = animal_dataset.y_size  # the number of output units in the network, i.e. the # of categories
    hidden_size = 3  # the number of hidden units in the layer between the inputs and the outputs
    learning_rate = 0.001  # what fraction of the correct amount the weights are changed on each trial
    weight_stdev = 0.1  # weights are initialized randomly to a value with a mean of 0, and a stdev of this
    num_epochs = 100000  # how many epochs (passes through the full dataset) the network takes

    net = neural_network.NeuralNetwork(num_input_units,
                                       hidden_size,
                                       num_output_units,
                                       learning_rate,
                                       weight_stdev)

    net.train(num_epochs, animal_dataset.training_x_list, animal_dataset.training_y_list)
    net.test(animal_dataset.test_x_list, animal_dataset.test_y_list, animal_dataset.test_label_list)


    h_labels = []
    for i in range(hidden_size):
        h_labels.append("H"+str(i+1))

    h1 = heatmapcluster.heatmapcluster(net.y_h.transpose(),
                                  h_labels, animal_dataset.category_list,
                                  label_fontsize=12,
                                  xlabel_rotation=0,
                                  cmap=plt.cm.coolwarm,
                                  show_colorbar=True,
                                  colorbar_pad=2,
                                  top_dendrogram=True)

    h2 = heatmapcluster.heatmapcluster(net.h_x,
                                  h_labels, animal_dataset.feature_list,
                                  label_fontsize=12,
                                  xlabel_rotation=90,
                                  cmap=plt.cm.coolwarm,
                                  show_colorbar=True,
                                  colorbar_pad=2,
                                  top_dendrogram=True)

    plt.show()


def main():
    #xor_model()
    animal_model()

main()
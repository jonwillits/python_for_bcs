from src import neural_network
import numpy as np
import random
import heatmapcluster
import matplotlib.pyplot as plt


####################################################################################################
class LogicDataset:
    def __init__(self):
        self.category_list = ['AND', 'OR', 'XOR']
        self.feature_list = ['X1', 'X2']
        self.training_x_list = [[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]]
        self.training_y_list = [[0.0, 0.0, 0.0], [0.0, 1.0, 1.0], [0.0, 1.0, 1.0], [1.0, 1.0, 0.0]]
        self.training_label_list = ['00-000', '01-011', '10-011', '11-110']
        self.training_size = len(self.training_x_list)
        self.x_size = len(self.training_x_list[0])
        self.y_size = len(self.training_y_list[0])
        self.test_x_list = self.training_x_list
        self.test_y_list = self.training_y_list
        self.test_label_list = self.training_label_list


####################################################################################################
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


####################################################################################################
def run_model(dataset, hidden_size, learning_rate, weight_stdev, num_epochs):

    # the network parameters
    num_input_units = dataset.x_size  # the number of input units in the neural network, i.e. the # of features
    num_output_units = dataset.y_size  # the number of output units in the network, i.e. the # of categories
    hidden_size = hidden_size  # the number of hidden units in the layer between the inptus and the outputs
    learning_rate = learning_rate  # what fraction of the correct amount the weights are changed on each trial
    weight_stdev = weight_stdev  # weights are initialized randomly to a value with a mean of 0, and a stdev of this
    num_epochs = num_epochs  # how many epochs (passes through the full dataset) the network takes

    # create the network
    net = neural_network.NeuralNetwork(num_input_units,
                                       hidden_size,
                                       num_output_units,
                                       learning_rate,
                                       weight_stdev)

    # test the random network's performance
    start_accuracy, start_error = net.test(dataset.training_x_list,
                                           dataset.training_y_list,
                                           dataset.training_label_list)

    # train the network
    train_accuracy, train_error_mean = net.train(dataset.training_x_list,
                                                 dataset.training_y_list,
                                                 num_epochs)

    # test the network
    test_accuracy, test_error_mean = net.test(dataset.test_x_list,
                                              dataset.test_y_list,
                                              dataset.test_label_list)

    # gather the information we want to return

    features = dataset.feature_list.copy()
    features.insert(0, 'X0')

    labels = (dataset.category_list, features)
    network_parameters = (num_input_units, num_output_units, hidden_size, net.h_x, net.y_h)
    weights = (np.vstack([net.h_bias, net.h_x.T]).T, np.vstack([net.y_bias, net.y_h.T]).T)
    training_parameters = (learning_rate, weight_stdev, num_epochs)
    performance = (train_accuracy, train_error_mean, test_accuracy, test_error_mean)

    return labels, network_parameters, weights, training_parameters, performance


####################################################################################################
def plot_performance(model_data):
    epochs = np.arange(0, model_data[3][2])
    training_accuracy = model_data[4][0]
    training_sse = model_data[4][1]

    fig, ax1 = plt.subplots()

    ax1.set_xlabel('Epochs')
    ax1.set_ylabel('Accuracy', color='darkblue')
    ax1.plot(epochs, training_accuracy, color='darkblue')

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    ax2.set_ylabel('SSE', color='orangered')  # we already handled the x-label with ax1
    ax2.plot(epochs, training_sse, color='orangered')

    fig.tight_layout()  # otherwise the right y-label is slightly clipped


####################################################################################################
def plot_weights(model_data):

    category_list = model_data[0][0]
    feature_list = model_data[0][1]
    hidden_size = model_data[1][2]
    h_x = model_data[2][0]
    y_h = model_data[2][1]

    h_labels = ['H0']
    for i in range(hidden_size):
        h_labels.append("H"+str(i+1))

    h1 = heatmapcluster.heatmapcluster(y_h.transpose(), h_labels, category_list, label_fontsize=12, xlabel_rotation=0,
                                       cmap=plt.cm.coolwarm, show_colorbar=True, colorbar_pad=2, top_dendrogram=True)

    h2 = heatmapcluster.heatmapcluster(h_x, h_labels, feature_list, label_fontsize=12, xlabel_rotation=90,
                                       cmap=plt.cm.coolwarm, show_colorbar=True, colorbar_pad=2, top_dendrogram=True)


####################################################################################################
def main():
    np.set_printoptions(precision=3, suppress=True)
    random.seed(None)
    np.random.seed(None)

    hidden_size = 2  # the number of hidden units in the layer between the inputs and the outputs
    learning_rate = 0.01  # what fraction of the correct amount the weights are changed on each trial
    weight_stdev = 0.1  # weights are initialized randomly to a value with a mean of 0, and a stdev of this
    num_epochs = 10000  # how many epochs (passes through the full dataset) the network takes
    training_proportion = 0.75

    logic_dataset = LogicDataset()
    logic_model = run_model(logic_dataset, hidden_size, learning_rate, weight_stdev, num_epochs)
    plot_performance(logic_model)
    # plot_weights(logic_model)

    #animal_dataset = AnimalDataset('data/animals_4_128_15.csv', training_proportion)
    #animal_model = run_model(animal_dataset, hidden_size, learning_rate, weight_stdev, num_epochs)
    #plot_performance(animal_model)
    #plot_weights(animal_model)

    plt.show()

main()

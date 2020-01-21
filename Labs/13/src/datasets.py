import random
import numpy as np

####################################################################################################
class LogicDataset:
    def __init__(self):
        self.category_list = ['AND', 'OR', 'XOR']
        self.feature_list = ['X1', 'X2']
        self.training_x_list = [[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]]
        self.training_y_list = [[0.0, 0.0, 0.0], [0.0, 1.0, 1.0], [0.0, 1.0, 1.0], [1.0, 1.0, 0.0]]
        self.training_label_list = ['00-000', '00-011', '10-011', '11-110']
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
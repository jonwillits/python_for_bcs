import numpy as np
import sys
import random

###########################################################################
###########################################################################
class Knn:
    ###########################################################################
    def __init__(self, dataset, min_max_k, distance_metric, verbose, random_seed, output_file):

        self.name = "k_nearest_neighbors"

        if min_max_k is not None:
            if len(min_max_k) != 2:
                print("ERROR: min_max KNN must be a tuple with the first number being at least 1,"
                      "and the second number being >= the first number and < training size - 1.")
                sys.exit(2)
            else:
                self.min_k = min_max_k[0]
                self.max_k = min_max_k[1]
        else:
            self.min_k = 1
            self.max_k = 5
        self.distance_metric = distance_metric

        self.dataset = dataset
        self.output_filename = output_file
        self.random_seed = random_seed
        self.best_k = None
        self.best_training_accuracy = None
        self.test_accuracy = None
        self.verbose = verbose

        random.seed(self.random_seed)
        np.random.seed(self.random_seed)

        if min_max_k[0] < 1:
            print("ERROR: min_max_k must be a tuple with the first number being at least 1,"
                  "and the second number being >= the first number and < training size - 1.")
            sys.exit(2)
        if min_max_k[1] < min_max_k[0] or min_max_k[1] > self.dataset.training_size-1:
            print("ERROR: min_max_k must be a tuple with the first number being at least 1,"
                  "and the second number being >= the first number and < training size - 1.")
            sys.exit(2)

    ###########################################################################
    def train(self):
        print("\nTraining KNN Model from k={} to {}".format(self.min_k, self.max_k))
        sim_matrix = self.calculate_similarity_matrix(self.dataset.training_list, self.dataset.training_list)

        num_neighbors_list = np.arange(self.min_k, self.max_k + 1)
        accuracy_list = []
        item_performance_list_list = []

        for nn in num_neighbors_list:
            accuracy, confidence_list, item_performance_list = self.classify_items(self.dataset.training_list,
                                                                                   self.dataset.training_list,
                                                                                   sim_matrix, nn)
            accuracy_list.append(accuracy)
            item_performance_list_list.append(item_performance_list)

        if self.verbose:
            for i in range(len(num_neighbors_list)):
                print("    Num Neighbors: {}   Accuracy: {:0.3f}".format(num_neighbors_list[i], accuracy_list[i]))

        best_nn_index = np.argmax(accuracy_list)
        self.best_k = num_neighbors_list[best_nn_index]
        self.best_training_accuracy = np.max(accuracy_list)

        print("    Winning Model: nn={}".format(self.best_k))
        if self.verbose:
            print("    Item Performance:")
            for item in item_performance_list_list[self.best_k - self.min_k]:
                print(item)

    ###########################################################################
    def test(self, rows, columns, k):
        sim_matrix = self.calculate_similarity_matrix(rows, columns)
        accuracy, confidence_list, item_performance_list = self.classify_items(rows, columns,
                                                                               sim_matrix, k)
        conf_mean = np.array(confidence_list).mean()
        print("    Test Accuracy Using {} nn: {:0.3f} with confidence {:0.3f}".format(k, accuracy, conf_mean))
        if self.verbose:
            for item in item_performance_list:
                print(item)

    ###########################################################################
    def calculate_similarity_matrix(self, rows, columns):
        num_rows = len(rows)
        num_cols = len(columns)

        sim_matrix = np.zeros([num_rows, num_cols], float)

        for i in range(num_rows):
            i_index = rows[i][0]
            i_features = self.dataset.feature_matrix[i_index, :]

            for j in range(num_cols):
                j_index = columns[j][0]
                j_features = self.dataset.feature_matrix[j_index, :]

                sim_matrix[i, j] = self.compute_similarity(i_features, j_features)
        return sim_matrix

    ###########################################################################
    @staticmethod
    def compute_similarity(a, b, metric='cosine'):

        similarity = None

        if metric == 'cosine':
            similarity = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

        elif metric == 'euclidean distance':
            distance = (((a-b)**2).sum())**0.5
            similarity = 1 / distance

        return similarity

    ###########################################################################
    def classify_items(self, rows, columns, sim_matrix, num_neighbors):
        num_rows = len(rows)
        correct_sum = 0
        n = 0
        confidence_list = []
        item_performance_list = []
        num_neighbors += 1
        for i in range(num_rows):
            category_votes = np.zeros(self.dataset.num_categories)
            current_word = rows[i][2]
            current_category = rows[i][1]
            sim_array = sim_matrix[i, :]
            most_sim_indexes = np.argpartition(sim_array, -num_neighbors)[-num_neighbors:]
            for index in most_sim_indexes:
                comparison_word = columns[index][2]
                if current_word != comparison_word:
                    comparison_category = self.dataset.word_category_dict[comparison_word]
                    category_votes[self.dataset.category_index_dict[comparison_category]] += 1

            win_index = np.argmax(category_votes)
            category_guess = self.dataset.category_list[win_index]
            confidence = np.max(category_votes) / category_votes.sum()
            confidence_list.append(confidence)

            if category_guess == current_category:
                correct = 1
            else:
                correct = 0
            correct_sum += correct
            n += 1

            performance_output = "        {:16s} {:16s} {}     {:0.3f}".format(current_word, category_guess,
                                                                               correct, confidence)
            item_performance_list.append(performance_output)

        accuracy = correct_sum / n
        return accuracy, confidence_list, item_performance_list

    ###########################################################################
    def write_results(self):
        f = open(self.output_filename, 'a')
        f.write("{},{},{},{},{},{},{},{},{}_{}_{},{},{}\n".format(self.name, self.random_seed,
                                                                  self.dataset.num_features,
                                                                  self.dataset.num_categories,
                                                                  self.dataset.num_words,
                                                                  self.dataset.training_size,
                                                                  self.dataset.normalize_data,
                                                                  self.dataset.svd_dimensions,
                                                                  self.min_k, self.max_k, self.best_k,
                                                                  self.best_training_accuracy,
                                                                  self.test_accuracy))
        f.close()







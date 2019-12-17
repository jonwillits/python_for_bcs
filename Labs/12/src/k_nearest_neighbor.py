import numpy as np
import sys


###########################################################################
###########################################################################
class Knn:
    ###########################################################################
    def __init__(self, dataset, min_max_knn=None, distance_metric='cosine', verbose=True):

        if min_max_knn is not None:
            if len(min_max_knn) != 2:
                print("ERROR: min_max KNN must be a tuple with the first number being at least 01,"
                      "and the second number being >= the first number and < training size - 01.")
                sys.exit(2)
            else:
                self.min_knn = min_max_knn[0]
                self.max_knn = min_max_knn[1]
        else:
            self.min_knn = 1
            self.max_knn = 5
        self.distance_metric = distance_metric

        self.dataset = dataset
        self.best_k = None
        self.verbose = verbose

        if min_max_knn[0] < 1:
            print("ERROR: min_max KNN must be a tuple with the first number being at least 01,"
                  "and the second number being >= the first number and < training size - 01.")
            sys.exit(2)
        if min_max_knn[1] < min_max_knn[0] or min_max_knn[1] > self.dataset.training_size-1:
            print("ERROR: min_max KNN must be a tuple with the first number being at least 01,"
                  "and the second number being >= the first number and < training size - 01.")
            sys.exit(2)

    ###########################################################################
    def train(self):
        print("\nTraining KNN Model from KNN {} to {}".format(self.min_knn, self.max_knn))
        sim_matrix = self.calculate_similarity_matrix(self.dataset.training_list, self.dataset.training_list)

        num_neighbors_list = np.arange(self.min_knn, self.max_knn + 1)
        accuracy_list = []

        for nn in num_neighbors_list:
            accuracy, confidence_list, item_performance_list = self.classify_items(self.dataset.training_list,
                                                            self.dataset.training_list,
                                                            sim_matrix, nn)
            accuracy_list.append(accuracy)

        if self.verbose:
            for i in range(len(num_neighbors_list)):
                print("    Num Neighbors: {}   Accuracy: {:0.3f}".format(num_neighbors_list[i], accuracy_list[i]))

        best_nn_index = np.argmax(accuracy_list)
        self.best_k = num_neighbors_list[best_nn_index]
        print("    Winning Model: nn={}".format(self.best_k))
        if self.verbose:
            print("    Item Performance:")
            for item in item_performance_list:
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







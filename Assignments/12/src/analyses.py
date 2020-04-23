import numpy as np


def compute_feature_correlations(dataset, verbose):
    feature_diagnosticity_matrix = np.zeros([dataset.num_features, dataset.num_categories], float)
    feature_correlation_matrix = np.zeros([dataset.num_features, dataset.num_features], float)

    for i in range(dataset.num_features):
        word1_feature_vector = dataset.feature_matrix[:, i]

        for j in range(dataset.num_features):
            word2_feature_vector = dataset.feature_matrix[:, j]
            correlation = np.corrcoef(word1_feature_vector, word2_feature_vector)[0, 1]
            feature_correlation_matrix[i, j] = correlation

        for j in range(dataset.num_categories):
            category_vector = dataset.category_matrix[:, j]
            correlation = np.corrcoef(word1_feature_vector, category_vector)[0, 1]
            feature_diagnosticity_matrix[i, j] = correlation

    if verbose:
        print()
        print("Feature Diagnosticity")
        output_string = "{:20s}".format("Feature")
        for i in range(dataset.num_categories):
            output_string += " {:>9s}".format(dataset.category_list[i])
        print(output_string)

        for i in range(dataset.num_features):
            output_string = "{:20s}".format(dataset.feature_list[i])
            for j in range(dataset.num_categories):
                output_string += " {:>9.2f}".format(feature_diagnosticity_matrix[i, j])
            print(output_string)

        print()
        print("Feature Correlations")
        for i in range(dataset.num_features):
            output_string = "{:20s}".format(dataset.feature_list[i])
            for j in range(dataset.num_features):
                output_string += "   {:>3.2f}".format(feature_correlation_matrix[i, j])
            print(output_string)
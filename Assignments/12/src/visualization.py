import random
import numpy as np
import matplotlib.pyplot as plt
import sys


###########################################################################
def plot_feature_scatter(the_dataset, word_labels, f1, f2, svd):
    if f1 >= the_dataset.num_features or f2 >= the_dataset.num_features:
        print("ERROR: Specified plot dimension ({},{}) outside data range {}".format(f1, f2, the_dataset.num_features))
        sys.exit()

    if svd:
        if not the_dataset.svd_dimensions:
            the_dataset.svd_data()
        sv_var = the_dataset.svd_proportion_variance[f1] + the_dataset.svd_proportion_variance[f2]
        title = "Singular Values {} and {}, explaining {:0.3f}% of variance".format(f1, f2, sv_var)
        x_label = "Singular Value {}".format(f2)
        y_label = "Singular Value {}".format(f2)
    else:
        title = "Features '{}' and '{}'".format(the_dataset.feature_list[f1], the_dataset.feature_list[f2])
        x_label = the_dataset.feature_list[f1]
        y_label = the_dataset.feature_list[f2]

    plt.figure(figsize=(8, 8))

    plot_scatter_group(the_dataset, f1, f2, "train", word_labels, svd)
    plot_scatter_group(the_dataset, f1, f2, "test", word_labels, svd)

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend()
    plt.show()


###########################################################################
def plot_scatter_group(the_dataset, f1, f2, group, word_labels, svd):
    if svd:
        plot_data = the_dataset.svd_row_features
    else:
        plot_data = the_dataset.feature_matrix

    if group == 'train':
        feature_data = plot_data[np.ix_(the_dataset.training_indexes, [f1, f2])]
        category_data = the_dataset.training_list
        m = 'o'
    else:
        feature_data = plot_data[np.ix_(the_dataset.test_indexes, [f1, f2])]
        category_data = the_dataset.test_list
        m = 'x'

    color_list = get_color_list(the_dataset.num_categories)

    for i in range(the_dataset.num_categories):
        category = the_dataset.category_list[i]
        new_feature_data_list = []
        new_label_list = []
        for j in range(len(feature_data)):
            if category_data[j][1] == category:
                new_feature_data_list.append(feature_data[j, :])
                new_label_list.append(the_dataset.training_list[j][2])

        if len(new_feature_data_list) > 0:
            new_feature_matrix = np.array(new_feature_data_list)
            plt.scatter(new_feature_matrix[:, 0], new_feature_matrix[:, 1], marker=m, color=color_list[i],
                        label=category + " " + group)

    if word_labels:
        for i in range(len(category_data)):
            plt.annotate(category_data[i][2], xy=(feature_data[i, 0], feature_data[i, 1]), fontsize=6)


###########################################################################
def get_color_list(num_categories):
    color_list = ["blue", "darkorange", "darkred", "black"]
    if len(color_list) < num_categories:
        color_list = []
        while len(color_list) < num_categories:
            color_list.append((random.random(), random.random(), random.random()))
    return color_list


###########################################################################
def plot_feature_by_category_scatter(the_dataset, feature_index, word_labels, svd):

    if feature_index >= the_dataset.num_features:
        print("ERROR: Trying to plot feature {}, greater than num features".format(the_dataset.num_features))
        sys.exit()

    if svd:
        if not the_dataset.svd_dimensions:
            the_dataset.svd_data()
        sv_var = the_dataset.svd_proportion_variance[feature_index]
        title = "Each Item's Singular Values {} Score, explaining {:0.3f}% of variance".format(feature_index, sv_var)
        y_label = "Singular Value {}".format(feature_index)
    else:
        title = "Each Item's {} Value".format(the_dataset.feature_list[feature_index])
        y_label = the_dataset.feature_list[feature_index]

    plt.figure(figsize=(8, 8))
    plt.title(title)
    plt.ylabel(y_label)
    plt.xlim(0, the_dataset.num_categories + 1)
    x_pos = np.arange(the_dataset.num_categories + 1)
    x_label_list = the_dataset.category_list.copy()
    x_label_list.insert(0, "")
    plt.xticks(x_pos, x_label_list)

    plot_feature_by_category_group(the_dataset, feature_index, "train", word_labels, svd)
    plot_feature_by_category_group(the_dataset, feature_index, "test", word_labels, svd)

    plt.show()


###########################################################################
def plot_feature_by_category_group(the_dataset, feature_index, group, word_labels, svd):
    color_list = get_color_list(the_dataset.num_categories)

    if svd:
        plot_data = the_dataset.svd_row_features
    else:
        plot_data = the_dataset.feature_matrix

    if group == 'train':
        word_indexes = the_dataset.training_indexes
        category_data = the_dataset.training_list
        m = 'o'
    else:
        word_indexes = the_dataset.test_indexes
        category_data = the_dataset.test_list
        m = 'x'

    feature_data = plot_data[np.ix_(word_indexes, [feature_index])]

    for i in range(len(feature_data)):
        category_index = the_dataset.category_index_dict[category_data[i][1]]
        current_color = color_list[category_index]
        current_label = category_data[i][2]
        x = category_index + 1
        y = feature_data[i]
        plt.scatter(x, y, color=current_color, marker=m)

        if word_labels:
            plt.annotate(current_label, xy=(x+0.01,y+0.01), fontsize=6)


###########################################################################
def plot_hierarchical_cluster(the_dataset, svd, similarity):

    print("\n    Plotting Hierarchical Cluster Diagram")
    ok_to_go = False

    try:
        import heatmapcluster
        ok_to_go = True
    except:
        print("Cannot import heatmapcluster. try running 'pip3 install heatmapcluster'")

    if svd:
        if the_dataset.svd_dimensions is None:
            print("ERROR: Cannot make SVD heat map without specifying SVD dimensions")
            sys.exit()
        else:
            data_matrix = the_dataset.svd_row_features[:, :the_dataset.svd_dimensions]
    else:
        data_matrix = the_dataset.feature_matrix

    if ok_to_go:
        y_labels = the_dataset.word_list

        if similarity is not None:
            x_labels = the_dataset.word_list
            data = np.zeros([the_dataset.num_words, the_dataset.num_words])
            for i in range(the_dataset.num_words):
                a = the_dataset.feature_matrix[i, :]
                for j in range(the_dataset.num_words):
                    b = the_dataset.feature_matrix[j, :]
                    data[i, j] = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
        else:
            x_labels = the_dataset.feature_list
            data = data_matrix

        print(data_matrix.shape)
        h = heatmapcluster.heatmapcluster(data,
                                          y_labels,
                                          x_labels,
                                          label_fontsize=6,
                                          xlabel_rotation=90,
                                          cmap=plt.cm.coolwarm,
                                          show_colorbar=True,
                                          colorbar_pad=2,
                                          top_dendrogram=True)
    plt.show()


############################################################################################################
def plot_weight_heat_map(log_reg_model):
    ok_to_go = False
    try:
        import heatmapcluster
        ok_to_go = True
    except:
        print("Cannot import heatmapcluster. try running 'pip install heatmapcluster'")

    if ok_to_go:
        h = heatmapcluster.heatmapcluster(log_reg_model.y_x_weights.transpose(),
                                          log_reg_model.dataset.feature_list, log_reg_model.dataset.category_list,
                                          label_fontsize=12,
                                          xlabel_rotation=0,
                                          cmap=plt.cm.coolwarm,
                                          show_colorbar=True,
                                          colorbar_pad=2,
                                          top_dendrogram=True)
    plt.show()


############################################################################################################
def plot_ypredict_yactual_scatter(logreg_model, word_labels, category_index):
    ###########################################################################

    def plot_group(item_list, current_marker):

        for i in range(logreg_model.dataset.num_categories):
            current_category = logreg_model.dataset.category_list[i]
            current_color = color_list[i]

            current_prediction_list = []

            for j in range(len(item_list)):
                word_index = item_list[j][0]
                word = item_list[j][2]
                word_category = item_list[j][1]

                current_features = logreg_model.dataset.feature_matrix[word_index, :]
                category_predictions = logreg_model.feedforward(current_features)
                current_category_prediction = category_predictions[category_index]

                if current_category == word_category:
                    current_prediction_list.append(current_category_prediction)

                    if word_labels:
                        if word_category == plot_category:
                            plt.text(current_category_prediction, 0.95, word, rotation=315)
                        else:
                            plt.text(current_category_prediction, 0.05, word, rotation=45)

            feature_vector = np.array(current_prediction_list)
            if current_category == plot_category:
                category_vector = np.ones([len(current_prediction_list)])
            else:
                category_vector = np.zeros([len(current_prediction_list)])

            plt.scatter(feature_vector, category_vector, color=current_color, marker=current_marker)

    ###########################################################################
    print("\nCreating y-predict y-actual scatter plot")
    if 0 > category_index >= len(logreg_model.dataset.category_list):
        print("ERROR: Specified category {} out of range")
        sys.exit()

    plot_category = logreg_model.dataset.category_list[category_index]

    color_list = get_color_list(len(logreg_model.dataset.category_list))

    plt.figure(figsize=(8, 8))
    plt.title("Category Prediction Values for Category '{}'".format(plot_category))
    plt.xlabel("Category Prediction Values")
    plt.ylabel("In Category '{}".format(plot_category))
    plt.xlim(0, 1)

    plot_group(logreg_model.dataset.training_list, 'o')
    plot_group(logreg_model.dataset.test_list, 'x')

    plt.show()

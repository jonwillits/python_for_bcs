import numpy as np
import random
import sys
import matplotlib.pyplot as plt

np.set_printoptions(precision=3)


###########################################################################
class Dataset:
	###########################################################################
	def __init__(self, filename, training_proportion=0.80, normalize_data=False, svd_dimensions=0, verbose=True):

		self.filename = filename  # the file where the data came from
		self.training_proportion = training_proportion  # the proportion of items that will be used to train the model
		self.normalize_data = normalize_data  # whether or not we want to z-score the feature columns

		self.num_categories = 0  	     # the total number of categories in the data file
		self.category_list = None  	     # a list of the categories in teh data file
		self.category_index_dict = None  # a dict with words as keys and their unique index number as a value

		self.num_features = 0		     # the total number of features in the data file
		self.feature_list = None         # a list of the features
		self.feature_index_dict = {}     # a dictionary with each feature as a key and its index as the value

		self.num_words = None		          # the total number of words in the data set
		self.word_list = None			      # the total list of words in the data set
		self.word_index_dict = None			  # a dict with each word as its key and its index as the value
		self.word_category_dict = None        # a dictionary with words as keys and their category as the value
		self.category_word_list_dict = None   # a dict with category as key and the list of member words as values

		self.feature_matrix = None			  # the full matrix of feature data in the dataset
		self.category_matrix = None			  # a binary matrix of size nun_words x num_categories; 1s if word in cat

		self.feature_diagnosticity_matrix = None   # a matrix showing the correlation of each feature with each category
		self.feature_correlation_matrix = None	   # a matrix showing the inter-correlations of all features

		self.training_size = 0		   # the number of words in the training set
		self.training_list = None      # the list of data for the training set
		self.training_indexes = None   # a list of index numbers of all the words in the training set
		self.training_feature_matrix = None  # a matrix (rows=words, cols=features) with just the training items' features

		self.test_size = 0			    # the number of words in the test set
		self.test_list = None		    # the list of data for the test set
		self.test_indexes = None		# a list of index numbers of all the words in the test set
		self.test_feature_matrix = None  # a matrix (rows=words, cols=features) with just the test items' features

		self.svd_dimensions = None		# how many singular value dimensions to retain if svd, or None if dont svd
		self.svd_features = None		# the resulting svd matrix of size num_words x svd_dimensions
		self.eigenvalues = None			# the eigenvalues of the svd
		self.top_two_variance = None    # the proportion of variance of the top two singular values

		self.verbose = verbose			# whether or not to print a lot of stuff out

		# import the data, creating the majority of the data structures described above
		print("\nCreating Dataset from file '{}'".format(filename))
		self.import_data()

		if self.normalize_data:
			self.normalize()

		if svd_dimensions:
			if svd_dimensions < self.num_features:
				self.svd_dimensions = svd_dimensions
				self.svd_data(self.svd_dimensions)
				self.feature_matrix = self.svd_features
			else:
				print("ERROR: SVD Dimensions must be less than Num Features")
				sys.exit(2)

		self.create_train_test_sets()

	###########################################################################
	def import_data(self):

		self.num_categories = 0
		self.category_list = []
		self.category_index_dict = {}

		self.num_features = 0
		self.feature_list = []
		self.feature_index_dict = {}

		self.num_words = 0
		self.word_list = []
		self.word_index_dict = {}

		self.word_category_dict = {}
		self.category_word_list_dict = {}

		feature_vector_list = []

		# open the data file, and use the data to create all of our important variables
		f = open(self.filename)
		i = 0
		for line in f:
			line = line.strip().strip('\n').strip()
			data = line.split(',')
			if i == 0:
				self.feature_list = data[2:]
				for feature in self.feature_list:
					if feature not in self.feature_index_dict:
						self.feature_index_dict[feature] = self.num_features
						self.num_features += 1
					else:
						print("ERROR: Data file {} has duplicate feature {}".format(self.filename, feature))
						sys.exit()
			else:
				category = data[0]
				word = data[1]
				feature_data = data[2:]

				if category not in self.category_list:
					self.category_list.append(category)
					self.category_word_list_dict[category] = []
					self.category_index_dict[category] = self.num_categories
					self.num_categories += 1

				self.word_list.append(word)
				if word not in self.word_index_dict:

					self.word_index_dict[word] = self.num_words
					self.num_words += 1
				else:
					print("ERROR: Data file {} has duplicate word {}".format(self.filename, word))
					sys.exit()

				self.word_category_dict[word] = category
				self.category_word_list_dict[category].append(word)

				feature_vector = np.array(feature_data, float)
				feature_vector_list.append(feature_vector)

			i += 1
		f.close()

		self.feature_matrix = np.array(feature_vector_list)

		self.category_matrix = np.zeros([self.num_words, self.num_categories], float)
		for i in range(self.num_words):
			current_word = self.word_list[i]
			for j in range(self.num_categories):
				current_category = self.category_list[j]
				if self.word_category_dict[current_word] == current_category:
					self.category_matrix[i, j] = 1

		print("    Loaded Dataset with {} categories, {} words, and {} features".format(self.num_categories,
																					self.num_words,
																					self.num_features))

		if self.verbose:
			print("    Features:")
			for i in range(self.num_features):
				print("        {}: {}".format(i, self.feature_list[i]))

	###########################################################################
	def normalize(self):
		print("    Normalizing Data...")
		self.feature_matrix = (self.feature_matrix.mean(0) - self.feature_matrix) / self.feature_matrix.std(0)

	###########################################################################
	def create_train_test_sets(self):
		data_list = []
		self.training_indexes = []
		self.test_indexes = []
		training_feature_list = []
		test_feature_list = []

		for i in range(self.num_words):
			word = self.word_list[i]
			category = self.word_category_dict[word]
			data_list.append((i, category, word))
		random.shuffle(data_list)
		training_size = int(round(len(data_list) * self.training_proportion, 0))
		if training_size < 1:
			print("ERROR: Current settings lead to a training size of < 1")
			sys.exit()
		if self.num_words - self.training_size < 1:
			print("ERROR: Current settings lead to a test size of < 1")
			sys.exit()

		self.training_list = data_list[:training_size]
		self.test_list = data_list[training_size:]
		self.training_size = len(self.training_list)
		self.test_size = len(self.test_list)

		print("    Created Training Set with {} items, and Test set with {} items".format(self.training_size, self.test_size))

		if self.verbose:
			print("    Training List")

		for i in range(self.training_size):
			item = self.training_list[i]
			self.training_indexes.append(item[0])
			training_feature_list.append(self.feature_matrix[item[0], :])

			if self.verbose:
				print("        {:5s} {:16s} {:16s} {}".format(str(item[0]), item[1], item[2], self.feature_matrix[item[0], :]))
		self.training_feature_matrix = np.array(training_feature_list)

		if self.verbose:
			print("    Test List")

		for i in range(self.test_size):
			item = self.test_list[i]
			self.test_indexes.append(item[0])
			test_feature_list.append(self.feature_matrix[item[0], :])

			if self.verbose:
				print("        {:5s} {:16s} {:16s} {}".format(str(item[0]), item[1], item[2], self.feature_matrix[item[0], :]))
		self.test_feature_matrix = np.array(test_feature_list)

	###########################################################################
	def svd_data(self, dimensions):
		print("    Performing SVD")
		u, s, vh = np.linalg.svd(self.feature_matrix, full_matrices=True)
		self.svd_features = u[:, :dimensions]
		self.eigenvalues = s
		self.top_two_variance = self.eigenvalues[:dimensions].sum() / self.eigenvalues.sum()

	###########################################################################
	def get_color_list(self):
		color_list = ["blue", "darkorange", "darkred", "black"]
		if len(color_list) < self.num_categories:
			color_list = []
			while len(color_list) < self.num_categories:
				color_list.append((random.random(), random.random(), random.random()))
		return color_list

	###########################################################################
	def plot_feature_scatter(self, f1=None, f2=None):

		###########################################################################
		def plot_group(feature_data, category_data, color_list, m, group):

			for i in range(self.num_categories):
				category = self.category_list[i]
				new_feature_data_list = []
				new_label_list = []
				for j in range(len(feature_data)):
					if category_data[j][1] == category:
						new_feature_data_list.append(feature_data[j, :])
						new_label_list.append(self.training_list[j][2])

				if len(new_feature_data_list) > 0:
					new_feature_matrix = np.array(new_feature_data_list)
					plt.scatter(new_feature_matrix[:, 0], new_feature_matrix[:, 1], marker=m, color=color_list[i],
								label=category + group)
			for i in range(len(category_data)):
				plt.annotate(category_data[i][2], xy=(feature_data[i, 0], feature_data[i, 1]), fontsize=6)
		###########################################################################

		if f1 is None and f2 is None:
			if not self.svd_dimensions:
				self.svd_data(2)
			print("\nCreating scatter plot of first two singular values of feature matrix")
			plot_data = self.svd_features
			plot_feature_list = [0, 1]
			title = "Singular Values 1 and 2, explaining {:0.3f}% of variance".format(self.top_two_variance)
			x_label = "Singular Value 1"
			y_label = "Singular Value 2"

		elif (0 <= f1 < self.num_features) and (0 <= f2 < self.num_features):
			if self.svd_dimensions:
				if f1 >= self.svd_dimensions or f2 >= self.svd_dimensions:
					print("ERROR: SVD dimensions was {}, but you specified a feature number greater than that".format(self.svd_dimensions))
					sys.exit()

			print("\nCreating scatter plot of features {} and {}".format(self.feature_list[f1], self.feature_list[f2]))
			plot_data = self.feature_matrix
			plot_feature_list = [f1, f2]
			title = "Features '{}' and '{}'".format(self.feature_list[f1], self.feature_list[f2])
			x_label = self.feature_list[f1]
			y_label = self.feature_list[f2]
		else:
			print("Invalid plot features specified. Must be None or numbers between {}-{}".format(0, self.num_features-1))
			sys.exit(2)

		color_list = self.get_color_list()

		plt.figure(figsize=(8, 8))

		training_matrix = plot_data[np.ix_(self.training_indexes, plot_feature_list)]
		plot_group(training_matrix, self.training_list, color_list, "o", " train")

		test_matrix = plot_data[np.ix_(self.test_indexes, plot_feature_list)]
		plot_group(test_matrix, self.test_list, color_list, "x", " test")

		plt.xlabel(x_label)
		plt.ylabel(y_label)
		plt.title(title)
		plt.legend()

	###########################################################################
	def plot_feature_category_scatter(self, feature_index=None, category_index=None):
		###########################################################################
		def plot_group(item_list, current_marker):

			for i in range(self.num_categories):
				current_category = self.category_list[i]
				current_color = color_list[i]

				current_feature_list = []

				for j in range(len(item_list)):
					word_index = item_list[j][0]
					word = item_list[j][2]
					word_category = item_list[j][1]
					feature = self.feature_matrix[word_index, feature_index]

					if current_category == word_category:
						current_feature_list.append(feature)

						if word_category == plot_category:
							plt.text(feature, 0.95, word, rotation=315)
						else:
							plt.text(feature, 0.05, word, rotation=45)

				feature_vector = np.array(current_feature_list)
				if current_category == plot_category:
					category_vector = np.ones([len(current_feature_list)])
				else:
					category_vector = np.zeros([len(current_feature_list)])

				plt.scatter(feature_vector, category_vector, color=current_color, marker=current_marker)
		###########################################################################

		print("\nCreating feature-category scatter plot")
		if (feature_index is None) or (category_index is None):
			print("        WARNING: Cannot plot feature category scatter without specifying indexes")
			print("        USAGE: dataset.plot_feature_category_scatter(feature_index, category_index)")
		else:
			plot_category = self.category_list[category_index]
			plot_feature = self.feature_list[feature_index]
			color_list = self.get_color_list()

			plt.figure(figsize=(8, 8))
			plt.title("'{}' Feature Values for Category '{}'".format(plot_feature, plot_category))
			plt.xlabel("Values of '{}'".format(plot_feature))
			plt.ylabel("In Category '{}".format(plot_category))

			plot_group(self.training_list, 'o')
			plot_group(self.test_list, 'x')

	###########################################################################
	def compute_feature_correlations(self):

		self.feature_diagnosticity_matrix = np.zeros([self.num_features, self.num_categories], float)

		self.feature_correlation_matrix = np.zeros([self.num_features, self.num_features], float)

		for i in range(self.num_features):
			word_feature_vector = self.feature_matrix[:, i]

			for j in range(self.num_features):
				word2_feature_vector = self.feature_matrix[:, j]
				correlation = np.corrcoef(word_feature_vector, word2_feature_vector)[0, 1]
				self.feature_correlation_matrix[i, j] = correlation

			for j in range(self.num_categories):
				category_vector = self.category_matrix[:, j]
				correlation = np.corrcoef(word_feature_vector, category_vector)[0,1]
				self.feature_diagnosticity_matrix[i, j] = correlation

		if self.verbose:
			print()
			print("Feature Diagnosticity")
			output_string = "{:20s}".format("Feature")
			for i in range(self.num_categories):
				output_string += " {:>9s}".format(self.category_list[i])
			print(output_string)

			for i in range(self.num_features):
				output_string = "{:20s}".format(self.feature_list[i])
				for j in range(self.num_categories):
					output_string += " {:>9.2f}".format(self.feature_diagnosticity_matrix[i, j])
				print(output_string)

			print()
			print("Feature Correlations")
			for i in range(self.num_features):
				output_string = "{:20s}".format(self.feature_list[i])
				for j in range(self.num_features):
					output_string += "   {:>3.2f}".format(self.feature_correlation_matrix[i, j])
				print(output_string)









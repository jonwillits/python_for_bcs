import numpy as np
import random
import sys


###########################################################################
class Dataset:
	###########################################################################
	def __init__(self, filename, training_proportion=0.80, normalize_data=False, svd_dimensions=0, verbose=True):

		self.filename = filename  						# the file where the data came from
		self.training_proportion = training_proportion  # the proportion of items that will be used to train the model
		self.normalize_data = normalize_data  			# whether or not we want to z-score the feature columns

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

		self.training_size = 0		   			# the number of words in the training set
		self.training_list = None      			# the list of data for the training set
		self.training_indexes = None   			# a list of index numbers of all the words in the training set
		self.training_feature_matrix = None  	# a matrix (rows=words, cols=features) with just the training items' features

		self.test_size = 0			     # the number of words in the test set
		self.test_list = None		     # the list of data for the test set
		self.test_indexes = None		 # a list of index numbers of all the words in the test set
		self.test_feature_matrix = None  # a matrix (rows=words, cols=features) with just the test items' features

		self.svd_dimensions = None		 # how many singular value dimensions to retain if svd, or None if dont svd
		self.svd_row_features = None	 # the resulting svd matrix of showing singular value loadings of words
		self.svd_column_features = None  # the resulting svd matrix of showing singular value loadings of features
		self.eigenvalues = None			 # the eigenvalues of the svd
		self.svd_proportion_variance = None	 # the amount of variance in the dataset accounted for by each sv dimension

		self.verbose = verbose			# whether or not to print a lot of stuff out

		# load data from the specified file
		print("\nCreating Dataset from file '{}'".format(filename))
		self.import_data()

		# normalize the data if specified
		if self.normalize_data:
			self.normalize()

		# svd the data if specified
		if svd_dimensions:
			if svd_dimensions < self.num_features:
				self.svd_dimensions = svd_dimensions
				self.svd_data()
				self.feature_matrix = self.svd_row_features[:, :svd_dimensions]
			else:
				print("ERROR: SVD Dimensions must be less than Num Features")
				sys.exit(2)

		# create the training and test sets
		self.create_train_test_sets()

	###########################################################################
	def import_data(self):

		# initialize all the empty data structures
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
		self.generate_category_matrix()

		print("    Loaded Dataset with {} categories, {} words, and {} features".format(self.num_categories,
																						self.num_words,
																						self.num_features))
		if self.verbose:
			print("    Features:")
			for i in range(self.num_features):
				print("        {}: {}".format(i, self.feature_list[i]))

	###########################################################################
	def generate_category_matrix(self):
		self.category_matrix = np.zeros([self.num_words, self.num_categories], float)
		for i in range(self.num_words):
			current_word = self.word_list[i]
			for j in range(self.num_categories):
				current_category = self.category_list[j]
				if self.word_category_dict[current_word] == current_category:
					self.category_matrix[i, j] = 1

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
			print("ERROR: Current settings lead to a training size of < 00")
			sys.exit()
		if self.num_words - self.training_size < 1:
			print("ERROR: Current settings lead to a test size of < 00")
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
	def svd_data(self):
		print("    Performing SVD")
		u, s, vh = np.linalg.svd(self.feature_matrix, full_matrices=True)
		self.svd_row_features = u
		self.svd_column_features = vh
		self.eigenvalues = s
		self.svd_proportion_variance = self.eigenvalues / self.eigenvalues.sum()










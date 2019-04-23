import numpy as np


class NeuralNetwork:
    ############################################################################################################
    def __init__(self, input_size, hidden_size, output_size, learning_rate, weight_init_stdev):

        # save the network parameters as class variables
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.learning_rate = learning_rate
        self.weight_init_stdev = weight_init_stdev

        # randomly initialize the weights from the input layer to the hidden layer
        self.h_bias = np.random.normal(0, self.weight_init_stdev, [self.hidden_size])
        self.h_x = np.random.normal(0, self.weight_init_stdev, [self.hidden_size, self.input_size])

        # randomly initialize the weights from the hidden layer to the output layer
        self.y_bias = np.random.normal(0, self.weight_init_stdev, [self.output_size])
        self.y_h = np.random.normal(0, self.weight_init_stdev, [self.output_size, self.hidden_size])

    ############################################################################################################
    def feedforward(self, x):

        # for a single input, propogate the activity forward through the network
        # return the value of the hidden and output layer
        z = np.dot(self.h_x, x) + self.h_bias
        h = np.tanh(z)

        z = np.dot(self.y_h, h) + self.y_bias
        y_predict = 1 / (1 + np.exp(-z))

        return h, y_predict

    ############################################################################################################
    @staticmethod
    def calc_error(y, y_predict):
        return y - y_predict

    ############################################################################################################
    def backpropogation(self, x, y_predict, h, y_error):

        """ multiply the error by the derivative of y_predict with respect to the sigmoid function in other words, to
        make y what we want, how much would we have to change x, taking into account it is a sigmoid function (since
        it's not linear, changes to x may not straightforwardly affect y? in other words, we wanted y1 to be 1, but it
        was 0.48, so what weights coming from layer h would have made y1=1 given the current values of h, taking into
        consideration that y is being calculated as the sigmoid of the dot product of its weighted inputs"""
        y_delta = y_error * self.sigmoid_prime(y_predict)

        """ propogate the delta, how much each y should be changed, back to the hidden layer, multiplying the value of 
        y_delta for each y by the weights coming into it, figuring out how much each hidden unit is "to blame" for y 
        being incorrect. Then figure out how much to change each of the weights coming into each hidden unit from x in 
        the same way, but multiplying the cost by the derivative of the tangent function. In other words, we wanted h1 
        to be a, it was a+1.5, so what weight change would make the output of h1 closer to a for this x, given that h1 
        is using the tangent function """
        h_cost = np.dot(y_delta, self.y_h)
        h_delta = h_cost * self.tanh_prime(h)

        """change the weights by the amounts determined above, which would set the weights to the "exact best" value
        for this item, multiplied by the learning rate, which says "only move them this proportion in the exact
        right direction", considering that the exact best weights for this item might not be the exact best weights
        for all items, and we dont want our weights ping-ponging all over the place."""
        self.y_bias += y_delta * self.learning_rate
        self.y_h += (np.dot(y_delta.reshape(len(y_delta), 1), h.reshape(1, len(h))) * self.learning_rate)

        self.h_bias += h_delta * self.learning_rate
        self.h_x += (np.dot(h_delta.reshape(len(h_delta), 1), x.reshape(1, len(x))) * self.learning_rate)

    ############################################################################################################
    @staticmethod
    def tanh_prime(z):
        # if we change x by amount z, how much can we expect y to change if x is input to the tanh function
        return 1.0 - np.tanh(z)**2

    ############################################################################################################
    @staticmethod
    def sigmoid_prime(z):
        # if we change x by amount z, how much can we expect y to change if x is input to the sigmoid function
        return 1/(1+np.exp(-z)) * (1 - 1/(1+np.exp(-z)))

    ############################################################################################################
    def train(self, num_epochs, x_list, y_list):
        print("\nTraining Neural Network with {} hidden units using learning rate of {}".format(self.hidden_size,
                                                                                                self.learning_rate))
        for i in range(num_epochs):

            correct_sum = 0
            for j in range(len(x_list)):  # for each item
                x = np.array(x_list[j], float)  # get the current x as a numpy array
                y = np.array(y_list[j], float)  # get the current y as a numpy array
                h, y_predict = self.feedforward(x)  # feed x through the weights to get a predicted y as the output
                error = self.calc_error(y, y_predict)  # compute the error, the difference between y and predicted y
                self.backpropogation(x, y_predict, h, error)  # use  error to adjust weights in  appropriate direction

                rounded_y_predict = np.round(y_predict)
                item_acc_sum = 0
                for k in range(len(y_list[j])):
                    if y[k] == rounded_y_predict[k]:
                        item_acc_sum += 1
                accuracy = item_acc_sum / len(y)
                correct_sum += accuracy

            if i % 10 == 0:
                accuracy = correct_sum / len(y_list)
                sse = (error**2).sum()
                print("Epoch: {}    Accuracy: {:0.3f}   Error: {:0.3f}".format(i+1, accuracy, sse))

    ############################################################################################################
    def test(self, x_list, y_list, label_list):
        # print out detailed network performance after training
        print("\nTesting model on test data")
        correct_sum = 0
        error_sum = 0
        for i in range(len(x_list)):
            x = np.array(x_list[i], float)
            y = np.array(y_list[i], float)
            h, y_predict = self.feedforward(x)

            rounded_y_predict = np.round(y_predict)
            item_acc_sum = 0
            for j in range(len(y_list[i])):
                if y[j] == rounded_y_predict[j]:
                    item_acc_sum += 1
            accuracy = item_acc_sum / len(y)
            correct_sum += accuracy

            error = self.calc_error(y, y_predict)
            sse = (error**2).sum()
            error_sum += sse

            error_output = np.array2string(y_predict, precision=3, separator='   ', suppress_small=True)
            print("{:24s}  Outputs: {}    Accuracy: {:0.2f}   Error: {:0.3f}".format(label_list[i], error_output, accuracy, sse))

        error_mean = error_sum / len(y_list)
        accuracy = correct_sum / len(y_list)
        print("Test Results    Accuracy: {:0.3f}   Error: {:0.3f}".format(accuracy, error_mean))

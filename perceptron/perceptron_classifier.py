from reader import Reader
from perceptron import Perceptron
import os


class PerceptronClassifier:
    def __init__(self, alpha, data_path, result_path):
        self.alpha = alpha
        self.data = Reader.read_data(f'{os.getcwd()}/data/{data_path}')
        self.test_data = Reader.read_data(f'{os.getcwd()}/data/{result_path}')
        self.perceptron = Perceptron(len(self.data[0]) - 1)

    def delta(self, d, y, vector):
        result = [self.perceptron.w[i] for i in range(len(self.perceptron.w))]
        result.append(self.perceptron.t)

        w = [float(x) for x in vector]
        w.append(-1)

        tmp = (d - y) * self.alpha

        for i in range(len(w)):
            w[i] *= float(tmp)

        for i in range(len(result)):
            result[i] += w[i]

        self.perceptron.w = [result[i] for i in range(len(result) - 1)]
        self.perceptron.t = result[len(result) - 1]

    def train(self):
        for data in self.data:
            wp = 0
            for i in range(len(data) - 1):
                wp += float(data[i]) * self.perceptron.w[i]

            if wp < self.perceptron.t:
                self.delta(1, 0, [data[i] for i in range(len(data) - 1)])

    def test(self):
        good_results = 0

        for data in self.test_data:
            wp = 0
            for i in range(0, len(data) - 1):
                wp += float(data[i]) * self.perceptron.w[i]

            if wp >= self.perceptron.t:
                good_results += 1

        print('Accuracy: ' + str(good_results / len(self.test_data)))

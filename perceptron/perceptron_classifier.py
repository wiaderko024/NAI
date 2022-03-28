from reader import Reader
from perceptron import Perceptron
import os


class PerceptronClassifier:
    def __init__(self, alpha, data_path, test_path):
        self.alpha = alpha
        self.data = Reader.read_data(f'{os.getcwd()}/data/{data_path}')
        self.test_data = Reader.read_data(f'{os.getcwd()}/data/{test_path}')
        self.perceptron = Perceptron(len(self.data[0]) - 1)
        self.result_map = {}

        results_set = set()
        for data in self.data:
            results_set.add(data[len(data) - 1])

        y = 0
        for result in results_set:
            self.result_map[y] = result
            y += 1

        print('W: ' + str(self.perceptron.w))
        print('T: ' + str(self.perceptron.t))
        print('Result map: ' + str(self.result_map))

    def train(self):
        for data in self.data:
            wp = 0.0
            for i in range(len(data) - 1):
                wp += float(data[i]) * float(self.perceptron.w[i])

            y = 1 if wp >= self.perceptron.t else 0

            if self.result_map[y] != data[len(data) - 1]:
                print(str(data) + ' ' + str(wp) + ' ' + self.result_map[y])
                print('DELTA')

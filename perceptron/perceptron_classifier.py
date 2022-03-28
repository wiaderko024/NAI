from reader import Reader
from perceptron import Perceptron
import os


class PerceptronClassifier:
    def __init__(self, alpha, data_path, test_path):
        self.data = Reader.read_data(f'{os.getcwd()}/data/{data_path}')
        self.test_data = Reader.read_data(f'{os.getcwd()}/data/{test_path}')
        self.perceptron = Perceptron(len(self.data[0]) - 1, alpha)
        self.result_map = {}

        results_set = set()
        for data in self.data:
            results_set.add(data[len(data) - 1])

        y = 0
        for result in results_set:
            self.result_map[y] = result
            y += 1

    def classify(self, vector):
        return self.result_map[self.calculate_y(vector)]

    def calculate_y(self, vector):
        wp = 0.0
        for i in range(len(vector)):
            wp += float(vector[i]) * float(self.perceptron.w[i])
        return 1 if wp >= self.perceptron.t else 0

    def train(self):
        for data in self.data:
            y = self.calculate_y(data[:-1])
            if self.result_map[y] != data[len(data) - 1]:
                d = 0 if y == 1 else 1
                self.perceptron.delta(d, y, data[:-1])

    def test(self):
        good_results = 0
        for data in self.test_data:
            y = self.calculate_y(data[:-1])
            if self.result_map[y] == data[len(data) - 1]:
                good_results += 1
        return good_results / len(self.test_data)

    def test_detail(self):
        for key in self.result_map:
            all_lines = 0
            good_results = 0
            for data in self.test_data:
                if data[len(data) - 1] == self.result_map[key]:
                    y = self.calculate_y(data[:-1])
                    if self.result_map[y] == data[len(data) - 1]:
                        good_results += 1
                    all_lines += 1
            print(f'Currency for {self.result_map[key]}: {good_results / all_lines}')

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
            self.result_map[result] = y
            y += 1

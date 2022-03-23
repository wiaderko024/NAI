from reader import Reader
from perceptron import Perceptron
import os


class PerceptronClassifier:
    def __init__(self, alpha, data_path, result_path):
        self.alpha = alpha
        self.data = Reader.read_data(f'{os.getcwd()}/data/{data_path}')
        self.test_data = Reader.read_data(f'{os.getcwd()}/data/{result_path}')
        self.perceptron = Perceptron(len(self.data[0]) - 1)

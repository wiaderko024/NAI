import random

from reader import Reader
from perceptron import Perceptron

from string import ascii_lowercase


class NeuralNetwork:
    def __init__(self, k, n, alpha, data_paths):
        self._k = k
        self._n = n
        self._alpha = alpha
        self._languages = {}
        self._perceptrons = {}
        for i in range(int(k)):
            data = Reader.read_data(data_paths[i])
            language = data_paths[i].split('/')[-2].split('.')[0]
            self._languages[language] = self._load_languages(data)
            self._perceptrons[language] = Perceptron(26, self._alpha)

        for p in self._perceptrons:
            print(f'{p}: {self._perceptrons[p]([random.uniform(0, 1) for i in range(26)])}')

    @staticmethod
    def _load_languages(data):
        tmp = ''
        for x in data:
            for y in range(len(x)):
                tmp += x[y]
        tmp = tmp.lower()
        tmp = tmp.replace(' ', '')

        result = ''
        for c in tmp:
            if c.isalpha():
                result += c

        return result

    # def train(self):
    #     results = []
    #     for language in self._languages:
    #         vector = []
    #         for letter in ascii_lowercase:
    #             vector.append(self._languages[language].count(letter)/len(self._languages[language]))

from reader import Reader
from perceptron import Perceptron

from string import ascii_lowercase


class NeuralNetwork:
    def __init__(self, k, alpha, data_paths):
        self._k = k
        self._alpha = alpha
        self._languages = {}
        self._perceptrons = {}
        for i in range(int(k)):
            data = Reader.read_data(data_paths[i])
            language = data_paths[i].split('/')[-2].split('.')[0]
            self._languages[language] = self._load_languages(data)
            self._perceptrons[language] = Perceptron(26, self._alpha)

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

    def train(self):
        for language in self._languages:
            vector = []
            for letter in ascii_lowercase:
                vector.append(self._languages[language].count(letter)/len(self._languages[language]))

            result_map = {}
            for perceptron in self._perceptrons:
                result_map[perceptron] = self._perceptrons[perceptron](vector)

            for result in result_map:
                if result == language and result_map[result] == 0:
                    self._perceptrons[result].delta(1, 0, vector)
                if result != language and result_map[result] == 1:
                    self._perceptrons[result].delta(0, 1, vector)

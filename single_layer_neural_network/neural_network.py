from reader import Reader
from perceptron import Perceptron

from string import ascii_lowercase
import os
import re


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

        self._train_map = {}
        for language in self._languages:
            result = self._get_test_data(data_paths, language)
            self._train_map[language] = result

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

    @staticmethod
    def _get_test_data(data_paths, language):
        result_paths = []
        for path in data_paths:
            tmp = path.split('/')[:-1]
            result = tmp[0]
            for i in range(1, len(tmp)):
                result += f'/{tmp[i]}'

            if tmp[-1] == language:
                files = os.listdir(result)
                for file in files:
                    test_paths = re.match('^test[0-9]+\\.txt$', file)
                    if test_paths is not None:
                        result_paths.append(f'{result}/{file}')

        result_data = []
        for path in result_paths:
            result_data.append(NeuralNetwork._load_languages(Reader.read_data(path)))

        return result_data

    @staticmethod
    def _calculate_vector(text):
        vector = []
        for letter in ascii_lowercase:
            vector.append(text.count(letter)/len(text))
        return vector

    def train(self):
        for language in self._languages:
            vector = self._calculate_vector(self._languages[language])

            result_map = {}
            for perceptron in self._perceptrons:
                result_map[perceptron] = self._perceptrons[perceptron](vector)

            for result in result_map:
                if result == language and result_map[result] == 0:
                    self._perceptrons[result].delta(1, 0, vector)
                if result != language and result_map[result] == 1:
                    self._perceptrons[result].delta(0, 1, vector)

    def test(self):
        good_results = 0
        all_results = 0
        for key in self._train_map:
            for item in self._train_map[key]:
                if self.classify(item) == key:
                    good_results += 1
                all_results += 1
        return good_results / all_results

    def classify(self, item):
        results = {}
        for perceptron in self._perceptrons:
            results[perceptron] = self._perceptrons[perceptron].net(self._calculate_vector(item))
        return max(results, key=results.get)

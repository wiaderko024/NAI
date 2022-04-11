from reader import Reader


class NeuralNetwork:
    def __init__(self, k, n, alpha, data_paths):
        self._k = k
        self._n = n
        self._alpha = alpha
        self._languages = {}

        for i in range(int(k)):
            data = Reader.read_data(data_paths[i])
            self._languages[data_paths[i].split('/')[len(data_paths[i].split('/')) - 1].split('.')[0]] = self._load_languages(data)

        for key in self._languages:
            print(f'{key}: {self._languages[key]}')

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

from reader import Reader
from my_fraction import MyFraction
import os


class Bayes:
    def __init__(self, train_set, test_set):
        self.train_set = Reader.read_data(f'{os.getcwd()}/data/{train_set}')
        self.test_set = Reader.read_data(f'{os.getcwd()}/data/{test_set}')
        self.result_values = []
        for data in self.train_set:
            if self.result_values.count(data[-1]) == 0:
                self.result_values.append(data[-1])

    @staticmethod
    def smoothing(fraction, values):
        return MyFraction(1, fraction.denominator + values)

    def bayes(self, test_data):
        result_map = {}
        for result in self.result_values:
            fractions = []

            # count result
            num = 0
            for train_data in self.train_set:
                if train_data[-1] == result:
                    num += 1
            fractions.append(MyFraction(num, len(self.train_set)))

            # count values in results
            for i in range(len(test_data)):
                tmp = 0
                for train_data in self.train_set:
                    if train_data[i] == test_data[i] and train_data[-1] == result:
                        tmp += 1
                fractions.append(MyFraction(tmp, num))

            # smoothing
            for x in range(len(fractions)):
                if fractions[x].numerator == 0:
                    # print(f'{fractions[x].numerator}/{fractions[x].denominator} ----> SMOOTHING')

                    values = []
                    for train_data in self.train_set:
                        if values.count(train_data[x - 1]) == 0:
                            values.append(train_data[x - 1])

                    fractions[x] = self.smoothing(fractions[x], len(values))

            # counting result
            numerator, denominator = 1, 1
            for fraction in fractions:
                numerator *= fraction.numerator
                denominator *= fraction.denominator
            result_map[result] = numerator / denominator

        return max(result_map, key=result_map.get)

    def test(self):
        for test_data in self.test_set:
            print(f'{test_data} -> {self.bayes(test_data)}')

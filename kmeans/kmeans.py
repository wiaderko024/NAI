from reader import Reader
import random
import os
import re


class Kmeans:
    def __init__(self, k, data_path):
        self.k = k
        self.data = Reader.read_data(f'{os.getcwd()}/data/{data_path}')
        self.c = [self.data[random.randint(0, len(self.data) - 1)] for _ in range(int(k))]
        self.map = {}

    def kmeans(self):
        self.map = {}
        for i in range(len(self.c)):
            self.map[i] = []

        for data in self.data:
            distances = []
            for c in self.c:
                tmp = []
                for i in range(len(data) - 1):
                    tmp.append((float(data[i]) - float(c[i])) ** 2)
                distances.append(sum(tmp))
            min_index = distances.index(min(distances))
            self.map[min_index].append(data)

        new_c = []
        for key in self.map:
            points = self.map[key]
            if len(points) == 0:
                new_c.append(self.c[key])
            else:
                c = []
                for i in range(len(self.data[0])):
                    tmp = []
                    for point in points:
                        tmp.append(float(point[i]))
                    c.append(sum(tmp) / len(tmp))
                new_c.append(c)

        self.c = new_c

        print(f'C after iteration: {self.c}')
        print(f'Map after iteration:')
        for key in self.map:
            print(f'{key}: ({len(self.map[key])}) {self.map[key]}')

    def learn(self):
        print(f'C before learning: {self.c}')
        print(f'Map before learning: {self.map}')
        print()

        iterations = 0
        while True:
            iterations += 1
            last_c = self.c
            self.kmeans()
            if self.c == last_c:
                break

        print()
        print(f'Iterations: {iterations}')
        print(f'C after learning: {self.c}')
        print(f'Map after learning:')
        for key in self.map:
            print(f'{key}: ({len(self.map[key])}) {self.map[key]}')

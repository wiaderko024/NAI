import random


class Perceptron:
    def __init__(self, input_size):
        self.w = [random.uniform(-1, 1) for i in range(0, input_size)]
        self.t = random.uniform(-1, 1)

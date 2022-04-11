import random


class Perceptron:
    def __init__(self, input_size, alpha):
        self.w = [random.uniform(-1, 1) for i in range(input_size)]
        self.t = random.uniform(-1, 1)
        self.alpha = alpha

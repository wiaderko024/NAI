import random


class Perceptron:
    def __init__(self, input_size, alpha):
        self.w = [random.uniform(-1, 1) for i in range(0, input_size)]
        self.t = random.uniform(-1, 1)
        self.alpha = alpha

    def delta(self, d, y, vector):
        result = [self.w[i] for i in range(len(self.w))]
        result.append(self.t)

        w = [float(x) for x in vector]
        w.append(-1)

        tmp = (d - y) * float(self.alpha)

        for i in range(len(w)):
            w[i] *= float(tmp)

        for i in range(len(result)):
            result[i] += w[i]

        self.w = [result[i] for i in range(len(result) - 1)]
        self.t = result[-1]

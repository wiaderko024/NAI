import random


class Perceptron:
    def __init__(self, input_size, alpha):
        self.w = [random.uniform(-1, 1) for i in range(input_size)]
        self.t = random.uniform(-1, 1)
        self.alpha = alpha

    def __call__(self, vector, *args, **kwargs):
        return int(self.net(vector) > 0)

    def __str__(self):
        return f'{len(self.w)} {self.t} {self.alpha}'

    def net(self, vector):
        wp = 0.0
        for i in range(len(vector)):
            wp += float(vector[i]) * float(self.w[i])
        return wp - self.t

    def delta(self, d, y, vector):
        result = self.w
        result.append(self.t)

        w = [float(element) for element in vector]
        w.append(-1)

        tmp = (d - y) * float(self.alpha)

        for i in range(len(w)):
            w[i] *= tmp

        for i in range(len(result)):
            result[i] += w[i]

        self.w = result[:-1]
        self.t = result[-1]

from neural_network import NeuralNetwork
import sys


def main(k, n, alpha, paths):
    network = NeuralNetwork(k, n, alpha, paths)


if __name__ == '__main__':
    if len(sys.argv) - 1 == 3 + int(sys.argv[1]):
        main(sys.argv[1], sys.argv[2], sys.argv[3], [sys.argv[i] for i in range(4, len(sys.argv))])
    else:
        print('usage: python3 main.py [K] [N] [ALPHA] [K-TIMES DATA PATH]')

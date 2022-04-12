from neural_network import NeuralNetwork
import sys


def main(k, n, alpha, paths):
    network = NeuralNetwork(k, alpha, paths)

    print(f'Accuracy before training: {network.test()}')
    for i in range(int(n)):
        network.train()
    print(f'Accuracy after training: {network.test()}')

    while True:
        print('Give sentence or sentences:')
        text = input()

        if text != 'EXIT':
            print(network.classify(text))
        else:
            break


if __name__ == '__main__':
    if len(sys.argv) - 1 == 3 + int(sys.argv[1]):
        main(sys.argv[1], sys.argv[2], sys.argv[3], [sys.argv[i] for i in range(4, len(sys.argv))])
    else:
        print('usage: python3 main.py [K] [N] [ALPHA] [K-TIMES DATA PATH]')

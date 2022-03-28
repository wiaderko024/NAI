from perceptron_classifier import PerceptronClassifier
import sys


def main():
    classifier = PerceptronClassifier(sys.argv[1], sys.argv[2], sys.argv[3])

    print(classifier.test())
    for i in range(1000):
        print(i)
        classifier.train()
        print(classifier.test())


if __name__ == '__main__':
    if len(sys.argv) == 4:
        main()
    else:
        print('usage: python3 main.py [ALPHA] [Train-set path] [Test-set path]')

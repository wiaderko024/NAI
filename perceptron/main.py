from perceptron_classifier import PerceptronClassifier
import sys


def main():
    classifier = PerceptronClassifier(sys.argv[2], sys.argv[3], sys.argv[4])

    print('Currency before training: ' + str(classifier.test()))
    for i in range(int(sys.argv[1])):
        classifier.train()
    print('Currency after traning: ' + str(classifier.test()))

    classifier.test_detail()

    print('Give vector (after spaces) or write EXIT to close:')

    while True:
        print('Give vector:')
        string = input()

        if string != 'EXIT':
            vector = string.split(' ')
            print(classifier.classify(vector))
        else:
            break


if __name__ == '__main__':
    if len(sys.argv) == 5:
        main()
    else:
        print('usage: python3 main.py [K] [ALPHA] [Train-set path] [Test-set path]')

from bayes import Bayes
import sys


def main():
    bayes = Bayes(sys.argv[1], sys.argv[2])
    bayes.test()


if __name__ == '__main__':
    if len(sys.argv) == 3:
        main()
    else:
        print('usage: python3 main.py [train-set path] [test-set path]')

import sys

from kmeans import Kmeans


def main():
    kmeans = Kmeans(sys.argv[1], sys.argv[2])
    kmeans.learn()


if __name__ == '__main__':
    if len(sys.argv) == 3:
        main()
    else:
        print('usage: python3 main.py [k] [data path]')

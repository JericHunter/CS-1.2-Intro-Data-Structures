from random import shuffle, randint
from sys import argv

def rearrange(words):
    words_list = list(words)
    shuffle(words_list)
    return ' '.join(words_list)


if __name__ == '__main__':
    args = argv[1:]
    words = rearrange(args)
    print(words)

import random, sys

def get_words(arg):
    f = open('/usr/share/dict/words', 'r')
    words = f.read().split()
    dictionary_words = []
    for i in range(int(arg)):
        dictionary_words.append(random.choice(words))
    return ' '.join(dictionary_words)

if __name__ == '__main__':
    number_of_words = sys.argv[1:]
    random_set = get_words(number_of_words[0])
    print(random_set)

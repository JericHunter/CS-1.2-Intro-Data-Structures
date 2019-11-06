from histogram import histogram_dict, read_words
import random
import sys


def randomizer(histogram):
    random_number = random.randint(0, len(histogram)-1)
    key = list(histogram.keys())
    return key[random_number]

def sample_frequency(histogram):
    frequency_list = []

    for key, value in histogram.items():
        [frequency_list.append(key) for i in range(value)]
    random_index = random.randint(0, len(frequency_list) - 1)

    return frequency_list[random_index]


def sentences(histogram, ammount=10):
    word = []
    for i in range(ammount):
        word.append(sample_frequency(histogram))
    sentence = ' '.join(word)

    return sentence



if __name__ == "__main__":
    arg = f'../Code/txt_files/{sys.argv[1]}'
    words = histogram_dict(arg)
    print(sentences(words, 15))

import random
import sys
from histogram import read_file, histogram_dict

def get_count(histogram):
    ''' Adds every value inside of the histogram'''
    count = 0
    for key, value in histogram.items():
        count += value
    return count



def word_probability(histogram, count):
    '''For each key-value pair, if random index chosen is less than or equal to the total value,
       return the word'''

    total = 0
    index = random.randint(1, count)

    for key, value in histogram.items():
        total += value

        if index <= total:
            return key

def sentence(count, total, histogram):
    sentence = ""

    while count > 0:
        index = random.randint(0, total - 1)
        total_count = 0

        for key, value in histogram.items():
            if index <= total_count:
                sentence += f' {key}'
                break

            total_count += value

        count -= 1

    return sentence

def sampling(text_file):
    '''Calling the function that returns the random word '''

    histogram = histogram_dict(text_file)
    count = get_count(histogram_dict(text_file))
    total = len(text_file)

    ' '.join(sentence(count, total, histogram))
    print(sentence(count, total, histogram))


if __name__ == '__main__':
    text_file = read_file('histo_sample_song.txt')
    main_sample(text_file)

def read_file(words_list):
    with open(words_list, 'r') as f:
        words = f.read().split()

    return words


def histogram(words_list):
    ''' Returns a list of lists '''

    text = read_file(words_list)
    histogram = []

    for word in text:
        updated = False
        for list in histogram:
            if word == list[0]:
                list[1] += 1
                updated = True
                break

        if updated == False:
            histogram.append([word, 1])

    return histogram

def histogram_dict(words_list):
    '''Returns dictionary'''

    histogram = dict()

    for word in words_list:
        if word in histogram:
            histogram[word] += 1

        else:
            histogram[word] = 1

    return histogram

def histogram_tuple(words_list):
    '''Returns tuple'''
    text = read_file(words_list)
    amount = 0
    histogram = []

    for word in text:
        updated = False
        for tuple in histogram:
            if tuple[0] == word:
                amount = tuple[1] + 1
                histogram.remove(tuple)
                histogram.append((word, amount))
                updated = True
        if updated == False:
            histogram.append((word, 1))

    return histogram


def unique_words(histogram):
    '''Returns total count of unique words based off of histogram data for list of lists.'''
    count = 0
    for list in histogram:
        count += 1

    return count

def frequency(word, histogram):
    '''Returns how many times a specific word is in a histogram data set for list of lists'''

    for list in histogram:
        if list[0] == word:
            return list[1]



if __name__ == '__main__':
    words_list = read_file('testing.txt')
    histogram = histogram_dict(words_list)

    print(histogram)

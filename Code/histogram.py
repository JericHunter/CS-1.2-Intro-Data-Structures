def read_words(file):
    with open(file, "r") as f:
        words = f.read().split()
    return words

def histogram(file):
    text = read_words(file)
    histogram = []
    for word in text:
        is_updated = False
        for list in histogram:
            if list[0] == word:
                list[1] += 1
                is_updated = True
        if is_updated == False:
            histogram.append([word,1])
    return histogram

def histogram_dict(file):
    text = read_words(file)
    histogram = {}
    for word in text:
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1
    return histogram


def histogram_tuple(file):
    text = read_words(file)
    histogram = []
    amount = 0
    for word in text:
        # print(histogram)
        is_updated = False
        for tuple in histogram:
            if tuple[0] == word:
                amount = tuple[1] +1
                histogram.remove(tuple)
                histogram.append((word,amount))
                is_updated = True
        if is_updated == False:
            histogram.append((word, 1))
    return histogram

def unique_words(histogram):
    return len(histogram)

def frequency(word, histogram):
    for list in histogram:
        if list[0] == word:
            return list[1]

def frequency_dic(word,histogram):
    for iterate, keys in histogram.items():
        if iterate == word:
            return keys


if __name__ == "__main__":
    histogram = (histogram_tuple('txt_files/testing.txt'))
    unique_words = unique_words(histogram)
    word = 'greatest'
    word_freq = frequency(word,histogram)

    print(histogram)
    print(f'Unique words: {unique_words}')
    print(f'Amount of "{word}": {word_freq}' )

    histogram_dict = (histogram_dict('txt_files/testing.txt'))
    word_frequency_dict = frequency_dic(word, histogram_dict)
    print(histogram_dict)
    print(word_frequency_dict)

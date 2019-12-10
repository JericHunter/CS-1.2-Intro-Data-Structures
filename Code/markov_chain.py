from dictogram import Dictogram
import random
import string

def cleanup_text_file(source_text):

    content = ''
    if '.txt' in source_text:
        file = open(source_text, 'r')
        content = file.read()
        file.close()
    else:
        content = source_text
    return content



def higher_order(word_list, new_words, order=2):
    chain_dict = dict()

    key_words = new_words.split()
    if len(key_words) != order:
        return "Length of input words does not equal order"

    words = []
    next_words = []
    next_pairs = []

    for i in range(len(word_list) - 1):
        words.clear()
        for j in range(order):
            if i < (len(word_list) - order):
                words.append(word_list[i + j])
        if key_words == words:
            next_words.clear()
            for j in range(order):
                next_words.append(word_list[i + (j + 1)])
            next_words_string = " ".join(next_words)
            next_pairs.append(next_words_string)

    chain_dict[new_words] = Dictogram(next_pairs)
    return chain_dict

def order_sample(word_list, order=2):
    histogram = Dictogram(word_list)
    next_words = []

    # sample a random word from histogram
    next_word_string = histogram.sample()
    # find all the words that come after
    chain = new_chain(word_list, next_word_string)
    # append both words to a list
    next_words.append(next_word_string)

    for i in range(order - 1):
        if len(chain) > 0:
            next_word_string = chain.sample()
            next_words.append(next_word_string)
            chain = new_chain(word_list, next_word_string)

    words_str = " ".join(next_words)
    return words_str

def higher_order_walk(word_list, length, order=2):
    sentence = []
    next_words_list = []

    words_str = order_sample(word_list, order)
    # append both words to the sentence
    sentence.append(words_str)


    for i in range(length - order):
        # clear next_words_list
        next_words_list.clear()
        # get next pair
        chain = higher_order(word_list, words_str, order)
        # if the chain isn't empty
        if len(chain[words_str]) > 0:
            # sample the value in the chain
            words_str = chain[words_str].sample()
            # add both words individually to the next words list
            next_words_list = words_str.split()
            # only append the second word to the sentence
            sentence.append(next_words_list[order - 1])

    return create_sentence(sentence)

def new_chain(word_list, word):
    """If word is in word_list, append the next word to a list, and then
    create a new histogram with the list of following words.
    """
    chain_list = []
    for i in range(len(word_list) - 1):
        if word == word_list[i]:
            chain_list.append(word_list[i + 1])

    chain = Dictogram(chain_list)
    return chain

def random_walk(word_list, length):
    """Start sentence with sample word from histogram, and then
    sample each new histogram chain to get the next word, add then to sentence.
    """
    sentence = []
    histogram = Dictogram(word_list)
    next_word = histogram.sample()
    sentence.append(next_word)
    for i in range(length - 1):
        chain = new_chain(word_list, next_word)
        if len(chain) > 0:
            next_word = chain.sample()
            sentence.append(next_word)

    return sentence

def create_sentence(words):
    """Joins words in a list"""
    words[0] = words[0].capitalize()
    last_word = words[len(words) - 1]
    last_char = last_word[len(last_word) - 1]
    formatted_sentence = ' '.join(words)
    return formatted_sentence

if __name__ == "__main__":
    words = cleanup_text_file('txt_files/houseofquiet.txt')
    word_list = words.split()
    print(higher_order_walk(word_list, 40))

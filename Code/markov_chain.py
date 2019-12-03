from dictogram import Dictogram
import random


def cleanup_text_file(file_name):

    with open(file_name, 'r') as f:
        text = f.read().split()

    words_list = []
    for word in text:
        word = word.strip(".@'/").lower()
        words_list.append(word)

    return words_list


class MarkovChain(dict):

    def __init__(self, words_list = None):

        super(MarkovChain, self).__init__()


        if words_list is not None:
            self.create_markov_chain(words_list)
            self['start'] = Dictogram(['the'])
            self['end'] = Dictogram(['.'])


    def create_markov_chain(self, words_list):

        for index, word in enumerate(words_list):

            if self.get(word) == None:
                self[word] = Dictogram()

            if index + 1 < len(words_list):
                next = words_list[index + 1]
                self.get(word).add_count(next)


    def sentence_gen(self, length = 10):

        sampled_word = random.choice(list(self.get('start')))

        sentence = sampled_word

        for item in range(length - 1):
            sampled_word = self[sampled_word].sample()

            sentence += " " + sampled_word


        sentence += random.choice(list(self.get('end')))

        return sentence



if __name__ == "__main__":

    words_list = cleanup_text_file('histo_sample_song.txt')
    markov_chain = MarkovChain(words_list = words_list)

    # print(markov_chain)
    print(markov_chain.sentence_gen())

    # print(markov_chain(words_list))

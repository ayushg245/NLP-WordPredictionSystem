import nltk
import random

nltk.download("gutenberg")
nltk.download("punkt")
corpus = nltk.word_tokenize(nltk.corpus.gutenberg.raw("austen-sense.txt").lower())
randomize = False


import numpy as np


def finish_sentence(sentence, n, corpus, randomize=False):
    output = sentence.copy()
    while len(output) < 10:
        word = output[-1]
        if word == "." or word == "?" or word == "!":
            break

        else:
            next = next_word(output, corpus, n, randomize)

            output.append(next)
    return output


def next_word(sentence, corpus, n, randomize):
    dict = {}
    if n == 1:
        for i in range(len(corpus)):
            dict[corpus[i]] = dict.get(corpus[i], 0) + 1
        max_value = max(dict.values())
        if randomize == False:
            for i in dict.keys():
                if dict[i] == max_value:
                    return i
        if randomize == True:
            lst1 = list(dict.keys())
            return np.random.choice(lst1)

    else:
        for i in range(len(corpus)):
            if sentence[-n + 1 :] == corpus[i : i + n - 1]:
                tup = tuple(corpus[i : i + n])
                if tup not in dict:
                    dict[tup] = 1
                else:
                    dict[tup] += 1

        if len(dict) == 0:
            return next_word(sentence, corpus, n - 1, randomize)

        if randomize == False:
            max_value = max(dict.values())
            for i in dict.keys():
                if dict[i] == max_value:
                    return i[-1]

        if randomize == True:
            lst = []
            for i in dict.keys():
                lst.append(i[-1])
            a = np.random.choice(lst)
            return a

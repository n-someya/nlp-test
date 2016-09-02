# -*- coding: utf-8 -*-
import re
from collections import Counter


def count_word_from(text):
    splitted_text = re.sub(r'[\.|\(|\)|,]', " ", text).split(" ")
    while '' in splitted_text:
        splitted_text.remove('')
    word_counter = Counter(splitted_text)
    return word_counter


def count_word_using_nltk_from(text):
    from nltk import stem
    stemmer = stem.PorterStemmer()
    splitted_text = text.lower().split(" ")
    while '' in splitted_text:
        splitted_text.remove('')

    stemmed_text = [stemmer.stem(w) for w in splitted_text]

    word_counter = Counter(stemmed_text)
    return word_counter

# -*- coding: utf-8 -*-
import re
from collections import Counter


def count_word_from(text):
    splitted_text = re.sub(r'[\.|\(|\)|,]', " ", text).split(" ")
    while '' in splitted_text:
        splitted_text.remove('')
    word_counter = Counter(splitted_text)
    return word_counter




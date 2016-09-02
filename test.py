# -*- coding: utf-8 -*-
import count_word

test_text = u"That statement is only true in general if your database is initialized using the “C” locale (the North America/English-friendly UNIX default). Running with “C” used to be extremely common, but is less and less so, as modern operating systems automagically choose appropriate regional locales to provide approriate time and formatting for end users."

counter = count_word.count_word_from(test_text)

for word, cnt in counter.most_common():
    print word, cnt

print "------------------------------------------------"

for word, cnt in count_word.count_word_using_nltk_from(test_text).most_common():
    print word, cnt

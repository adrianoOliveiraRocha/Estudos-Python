# -*- coding: utf-8 -*-
from nltk.tokenize import sent_tokenize, word_tokenize, WordPunctTokenizer


input_text = "Do you know how tokenization works? It's actually quite "\
"interesting! Let's analyze a couple of sentences and figure it out."

print('\nSentence Tokenizer:')
print(sent_tokenize(input_text))

print('\nWord Tokenizer')
print(word_tokenize(input_text))

print('\nWord punct tokenizer:')
print(WordPunctTokenizer().tokenize(input_text))
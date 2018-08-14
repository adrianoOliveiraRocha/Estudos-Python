import random

from nltk import NaiveBayesClassifier
from nltk.classify import accuracy as nltk_accuracy
from nltk.corpus import names

# Extract last N letters from the input word
# and that will act as our "feature"
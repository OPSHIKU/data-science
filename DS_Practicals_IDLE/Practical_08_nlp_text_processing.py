# -*- coding: utf-8 -*-
"""
PRACTICAL 8 : Basic text processing using NLP
Karina Bacche - 264447

Open in IDLE and press F5.
Keep any data files this practical needs in the SAME folder as this file.
Close each graph window to continue.
"""

import os

BASE = os.path.dirname(os.path.abspath(__file__))


def path(name):
    return os.path.join(BASE, name)


def p8():
    import nltk
    nltk.download("punkt")
    nltk.download("punkt_tab")
    nltk.download("stopwords")

    from nltk.tokenize import sent_tokenize, word_tokenize
    from nltk.corpus import stopwords
    from nltk.probability import FreqDist

    text = """
    Natural Language Processing (NLP) is a field of Artificial Intelligence.
    It focuses on the interaction between computers and human language.
    NLP helps machines understand, interpret, and generate human language.
    """

    print("Sentence Tokenization:")
    print(sent_tokenize(text), "\n")

    print("Word Tokenization:")
    words = word_tokenize(text)
    print(words, "\n")

    print("Removing Stopwords:")
    stop_words = set(stopwords.words("english"))
    filtered_words = [w for w in words
                      if w.lower() not in stop_words and w.isalnum()]
    print(filtered_words, "\n")

    print("Frequency Distribution:")
    fdist = FreqDist(filtered_words)
    for word, freq in fdist.most_common():
        print(f"{word}: {freq}")


if __name__ == "__main__":
    p8()

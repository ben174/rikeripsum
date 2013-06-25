#!/usr/bin/env python

import pickle
import random
import os
import argparse

lines = None

_ROOT = os.path.abspath(os.path.dirname(__file__))

def get_data(path):
    return os.path.join(_ROOT, 'data', path)


def generate_paragraph(sentence_count=None): 
    """Generates a 'paragraph' consisting of sentence_count 'sentences'.
    If sentence_count is not provided, a random number between two and
    ten will be chosen.
    
    """
    if not sentence_count:
        sentence_count = random.choice(range(2, 10))
    paragraph = ''
    for i in range(sentence_count): 
        paragraph += ' ' + generate_sentence()
    return paragraph.strip()


def generate_sentence(word_count=None): 
    """Returns a 'sentence'. A sentence is actually one line of dialog
    by William Riker, and may in fact consiste of multiple sentences.
    If a word_count is provided, the generator will attempt to return 
    a sentence with that number of words. Or come as close as possible. 
    Note that higher numbers of word will become increasingly unique to
    the distribution and may result in a less 'random' sentence. 

    """
    global lines
    if not lines: 
        lines = load_pickle()
    if not word_count: 
        return random.choice(lines)['text']

    potential_matches = [line for line in lines if 
        line['word_count'] == word_count]
    if potential_matches: 
        return random.choice(potential_matches)['text']
    else: 
        if word_count == 1:
            raise ImpossibleSentenceError('Couldn\'t generate a sentence with \
                the requested number of words.')
        # recursive callback, trying one less words each time. 
        return generate_sentence(word_count - 1)


def load_pickle(): 
    """Loads up sentence data. All methods in this class which use 
    phrase data should call this if global lines == None.

    """
    f = open(get_data('riker.pickle'))
    return pickle.load(f)


class ImpossibleSentenceError(Exception):
    """Called when the engine is unable to fufill the request due to lack 
    of potential data. This would usually be raised if a number of sentences 
    was requested which the engine did not have data to fulfill.

    """
    def __init__(self, message, Errors):
        Exception.__init__(self, message)


def main():

    parser = argparse.ArgumentParser(description='Print Riker quotes.')
    parser.add_argument('-c', '--count', dest='count', type=int,
                       help='minimum number of words in the sentence')

    args = parser.parse_args()
    print rikeripsum.generate_sentence(args.count)


if __name__ == '__main__': 
    main()

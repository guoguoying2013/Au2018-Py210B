#!/usr/bin/env python3

import random
import sys

trigrams = {}

def build_trigrams_list(words_list, trigrams_dict):
    for line_list in words_list:
        build_trigrams(line_list, trigrams_dict)

def build_trigrams(word_list, trigrams_dict):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """

    #
    # (word0, word1) ==> word2 
    # If key exists, then append word2 to the list
    #

    if word_list == None:
        print('build_trigrams: No words to build trigram dict with')
        return

    for i in range(0, len(word_list)-2, 1):
        key = (word_list[i], word_list[i+1])
        if key in trigrams_dict.keys():
            trigrams_dict[key].append(word_list[i+2])
        else:
            trigrams_dict[key] = [word_list[i+2]]

def generate_text_trigrams(trigram_dict):
    random_str = str()
    return_str = str()
    line_length = 0
    trigram_keys = list(trigram_dict.keys())

    for i in range(len(trigram_dict)):
        first_key = random.choice(trigram_keys)
        print('[{0}] random key: {1}'.format(i, first_key))
        random_str += (first_key[0])
        random_str += ' '
        random_str +=(first_key[1])
        random_str += ' '
        word_values = trigram_dict[first_key]
        random_word = random.choice(word_values)
        print('[{0}] random word value: {1}'.format(i, random_word))
        random_str += random_word
        line_length += len(random_str)
        if (line_length > 60):
            random_str += '\n'
            return_str += random_str
            line_length = 0
            random_str = ''
        else:
            random_str += ' '
    return return_str


def filter_isalpha(input_str):
    exceptions = [' ', '-']
    return ''.join(c for c in input_str if (c.isalpha() or (c in exceptions)))


def parse_input_file(input_filename):
    line_list = []
    word_list = []

    try:
        with open(input_filename, 'r') as fd:
            try:
                line = fd.readline()
            except IOError:
                print("I/O Error with file [{0}] on readline".format(input_filename))
                return None
            while(line):
                line = line.replace('--', ' ')
                line = filter_isalpha(line)
                if(len(line) == 0):
                    continue
                line_list.append(line)
                try:
                    line = fd.readline()
                except IOError:
                    print("I/O Error with file [{0}] on readline".format(input_filename))
                    return None
    except FileNotFoundError:
        print("File [{0}] not found".format(input_filename))
        return None
    except IOError:
        print("I/O Error with file [{0}] on open".format(input_filename))
        return None

    for line in line_list:
        line = line.split()
        for word in line:
            word_list.append(word)

    return word_list


if __name__ == "__main__":
    trigrams_dict = {}

    try:
        input_filename = sys.argv[1]
    except IndexError:
        print('trigrams: filename must be provided as an argument')
        sys.exit(1)

    sample_words = parse_input_file(input_filename)
    build_trigrams(sample_words, trigrams_dict)
    print(trigrams_dict)
    random_txt = generate_text_trigrams(trigrams_dict)
    print(random_txt)

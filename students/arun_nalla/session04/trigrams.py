#! usr/bin/env python 3
""" Trigrams assignment - Lesson4 by Arun"""
import random
import string
from collections import defaultdict
# words = 'I wish I may I wish I might'.split()


def trigram_dict():
    trilist = defaultdict(list)
    for i in range(len(words)-2):
        pair = tuple(words[i:i+2])
        follower = words[i+2]
        trilist[pair].append(follower)
    return trilist


def new_data():
    word_list = ''
    with open(filename, 'r') as file_name:
        translator = str.maketrans('', '', string.punctuation)
        for lines in file_name.readlines():
            words_in_file = lines.translate(translator)
            word_list += words_in_file
    list_of_words = word_list.split()
    return list_of_words


def build_new_story():
    trigrams = trigram_dict()
    keys_first = random.choice(list(trigrams))  # print (keys_first, "key first")
    my_list = list(keys_first)  # print (my_list, "new list")
    my_list.append(random.choice(trigrams[keys_first]))  # print (my_list, "first full")
    while len(my_list) <= 100:
        key_next = tuple(my_list[-2:])
        if key_next in trigrams:
            my_list.append(random.choice(trigrams[key_next]))
        else:
            break
    new_story = ' '.join(my_list)
    return new_story


if __name__ == '__main__':
    # get the filename from the command line
    filename = input("Enter a file name>>>")
    words = new_data()
    word_pairs = trigram_dict()
    new_text = build_new_story()
    print(new_text)


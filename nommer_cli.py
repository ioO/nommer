import argparse
from nommer import *

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("words", help="list of words separated by coma", type=str)
    args = parser.parse_args()
    if args.words:
        names = process(args.words)
        display(names)

def process(words):
    word_list = words.split(',')
    list_index = get_list_index(word_list)
    index_range = find_index_range(list_index)
    list_integer = create_list_integer_range(index_range, len(list_index))
    index_string = create_possible_index_string(list_index, list_integer)
    possible_index = create_possible_index(index_string)
    del(index_string)
    combinations = create_combination(word_list, possible_index)
    del(possible_index)
    return create_name(combinations)

def display(names):
    for name in names:
        print(name)

if __name__ == '__main__':
    main()

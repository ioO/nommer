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
    return get_combination_of_names(words.split(','))

def display(names):
    for name in names:
        print(name)

if __name__ == '__main__':
    main()

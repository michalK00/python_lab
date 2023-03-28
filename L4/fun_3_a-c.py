import sys
import os
import fun_3_utils as utils
from collections import Counter


def read_file_path():
    try:
        path = sys.stdin.readline().rstrip()
        if not path:
            raise ValueError("empty path")
        return path
    except ValueError as e:
        print(e)


def analize_file(path):
    line_count = 0
    word_count = 0
    letter_count = 0
    word_dict = Counter()
    letter_dict = Counter()
    with open(str(path), 'r') as f:
        for line in f:

            words_in_line = line.split()
            letters_in_line = list("".join(words_in_line))
            # letters_in_line = [
            #    letter for word in words_in_line for letter in word]
            letter_dict += Counter(letters_in_line)
            word_dict += Counter(words_in_line)

            line_count += 1

    word_count = word_dict.total()
    letter_count = letter_dict.total()
    most_occurring_letter, most_occurring_letter_count = letter_dict.most_common(1)[
        0]
    most_occurring_word, most_occurring_word_count = word_dict.most_common(1)[
        0]
    absolute_file_path = os.path.abspath(path)
    print(utils.toJson(absolute_file_path, line_count, word_count,
          letter_count,  most_occurring_word, most_occurring_word_count, most_occurring_letter, most_occurring_letter_count))


if __name__ == "__main__":
    path = read_file_path()
    analize_file(path)

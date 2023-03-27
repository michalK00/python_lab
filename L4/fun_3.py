import sys
import os


def read_file_path():
    try:
        # rstrip usuwa białe znaki
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
    word_dict = {}
    letter_dict = {}
    with open(str(path), 'r') as f:
        for line in f:

            words_in_line = line.split()
            letters_in_line = [
                letter for word in words_in_line for letter in word]
            letter_dict = feed_dict(letter_dict, letters_in_line)
            word_dict = feed_dict(word_dict, words_in_line)

            line_count += 1
            word_count += len(words_in_line)
            letter_count += len(letters_in_line)

    most_occurring_letter = max(letter_dict, key=letter_dict.get)
    most_occurring_word = max(word_dict, key=word_dict.get)
    absolute_file_path = os.path.abspath(path)
    print(f"absolute_file_path: {absolute_file_path}")
    print(f"line_count: {line_count}")
    print(f"word_count: {word_count}")
    print(f"letter_count: {letter_count}")
    print(f"most_occurring_letter: {most_occurring_letter}")
    print(f"most_occurring_word: {most_occurring_word}")


def feed_dict(dict, list_of_entries):
    for entry in list_of_entries:
        if entry in dict:
            dict[entry] += 1
        else:
            dict[entry] = 1
    return dict


if __name__ == "__main__":
    path = read_file_path()
    analize_file(path)

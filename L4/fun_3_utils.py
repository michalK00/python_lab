import json


def toJson(absolute_file_path, line_count, word_count,
           letter_count, most_occurring_word, most_occurring_word_count, most_occurring_letter, most_occurring_letter_count):
    data = {
        "absolute_file_path": absolute_file_path,
        "counters": {
            "lines": line_count,
            "words": word_count,
            "letters": letter_count
        },
        "most_occurring_word": most_occurring_word,
        "most_occurring_word_count": most_occurring_word_count,
        "most_occurring_letter": most_occurring_letter,
        "most_occurring_letter_count": most_occurring_letter_count
    }
    return json.dumps(data, indent=2)


def feed_dict(dict, list_of_entries):
    for entry in list_of_entries:
        if entry in dict:
            dict[entry] += 1
        else:
            dict[entry] = 1
    return dict

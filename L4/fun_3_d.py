import sys
import os
from subprocess import run
import json
from prettytable import PrettyTable


def launch_scripts(folderPath):
    output = []
    for path in os.listdir(folderPath):
        result = run(["python", "..\\fun_3_a-c.py"], input=path,
                     capture_output=True, text=True, cwd=folderPath)
        output.append(json.loads(result.stdout))
    printResults(output)


def printResults(results):
    table = PrettyTable()
    words = {}
    letters = {}
    table.field_names = ["No of files", "No of letters combined", "No of words combined",
                         "No of lines", "Most occuring letter", "Most occuring word"]
    for entry in results:
        most_occurring_word = entry["most_occurring_word"]
        most_occurring_word_count = entry["most_occurring_word_count"]
        most_occurring_letter = entry["most_occurring_letter"]
        most_occurring_letter_count = entry["most_occurring_letter_count"]

        if most_occurring_word in words:
            words[most_occurring_word] += most_occurring_word_count
        else:
            words[most_occurring_word] = most_occurring_word_count

        if most_occurring_letter in letters:
            letters[most_occurring_letter] += most_occurring_letter_count
        else:
            letters[most_occurring_letter] = most_occurring_letter_count

    table.add_row([
        len(results),
        sum(entry["counters"]["letters"] for entry in results),
        sum(entry["counters"]["words"] for entry in results),
        sum(entry["counters"]["lines"] for entry in results),
        str(max(letters, key=letters.get)),
        max(words, key=words.get),
    ])

    print(table)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        launch_scripts(sys.argv[1])
    else:
        raise ValueError("No path given!")

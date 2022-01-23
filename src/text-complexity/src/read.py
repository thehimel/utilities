"""
Analyze a file and return the result in dictionary format.
"""

from pathlib import Path
from string import punctuation
from definitions import umlaut_characters, umlaut, characters, word_len, umlaut_percentage


def read(file_path: Path) -> dict[str, int | dict | float]:
    """
    Analyze a file.

    :param file_path: Path of the file.
    :return: Result in dictionary format.
    """
    result = {umlaut: 0, characters: 0, umlaut_percentage: 0, word_len: {}}
    word_count = 0
    with open(file=file_path, encoding="utf-8") as input_file:
        while True:
            char = input_file.read(1)
            if not char:
                if word_count:
                    result[word_len][word_count] = result[word_len].get(word_count, 0) + 1
                result[word_len] = dict(sorted(result[word_len].items(), reverse=True))
                return result

            if char in punctuation or char.isspace():
                if word_count:
                    # If the end of word is detected, update the word length.
                    result[word_len][word_count] = result[word_len].get(word_count, 0) + 1
                    word_count = 0
            else:
                result[characters] += 1
                word_count += 1
                char = char.lower()
                if char in umlaut_characters:
                    result[umlaut] += 1

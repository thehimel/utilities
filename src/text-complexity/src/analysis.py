"""
Analyze the data in a directory and save the report in the output directory.
"""

import json
from pathlib import Path
from operator import itemgetter
from string import punctuation
from definitions import umlaut_characters, umlaut, characters, word_len, umlaut_percentage


def read(file_path: Path) -> dict[str, int | dict | float]:
    """
    Analyze a file and return the result in dictionary format.

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


def analyze(input_directory: str, output_directory: str) -> None:
    """
    Perform the analysis and save the output.

    :param input_directory: Path to the input directory.
    :param output_directory: path to the output directory.
    :return: None
    """
    results = []
    input_files = list(Path(input_directory).glob('**/*.txt'))  # Fetch list of files recursively.
    for input_file in input_files:
        result = read(file_path=input_file)
        if result[characters]:
            results.append({
                "file_name": input_file.name,
                "file_path": input_file.as_posix(),
                umlaut_percentage: round(result[umlaut] / result[characters] * 100, 2),
                "result": result,
            })

    Path(output_directory).mkdir(parents=True, exist_ok=True)  # Create nested directories if they do not exist.
    output_path = Path(output_directory) / "report.json"
    with open(output_path, 'w', encoding="utf-8") as output_file:
        json.dump(sorted(results, key=itemgetter(umlaut_percentage)), output_file, indent=4)

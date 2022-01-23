"""
Analyze the complexity of texts.
"""

import json
from pathlib import Path
from operator import itemgetter
from read import read
from definitions import umlaut, characters, umlaut_percentage, output_directory

if __name__ == "__main__":
    results = []
    input_files = list(Path('.').glob('**/*.txt'))  # Fetch list of files recursively.
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
    output_path = Path(output_directory) / "results.json"
    with open(output_path, 'w', encoding="utf-8") as output_file:
        json.dump(sorted(results, key=itemgetter(umlaut_percentage)), output_file, indent=4)

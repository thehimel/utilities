#!/usr/bin/env python3.9

"""
A script to copy all the files from one directory to
a directory matching the file name that starts with the
given text.

Usages:
python3 c.py text
python3 c.py 1
./c.py 1
~/s/c.py 1
"""

from glob import glob
from pathlib import Path
from sys import argv, exit
from shutil import copytree


def main(text) -> None:
	"""
	Main function.

	Arguments:
		text(str): Text to search for the files.
	"""

	# Get the first file starting with the text
	file = glob(f'{text}*.mp4')[0]

	# Get the file name without extension
	directory = Path(Path(file).stem)

	# Create the directory if not exists
	directory.mkdir(parents=True, exist_ok=True)

	dst = directory.resolve()
	src = Path.home() / "Pictures" / "vlc"
	src = src.resolve()

	# Copy all files src to dst and it is ok if dir exists.
	copytree(src, dst, dirs_exist_ok=True)
	print(f"Successfully copied all files from \n{src} to \n{dst}")


if __name__ == "__main__":
	if len(argv) < 2:
		print("Please pass at least one argument.")
		exit(1)

	# Run main with the argument.
	main(argv[1])

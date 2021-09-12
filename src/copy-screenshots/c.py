#!/usr/bin/env python3.9

"""
A script to copy all the files from one directory to a directory
matching the file name that starts with the given text.

Usages:
python3 c.py text
python3 c.py 1
./c.py 1
~/s/c.py 1
"""

from glob import glob
from pathlib import Path
from sys import argv, exit
from shutil import move


def main(text) -> None:
	"""
	Main function.

	Arguments:
		text(str): Text to search for the files.
	"""

	src = Path.home() / "Pictures" / "vlc"
	extensions = [".jpg", ".png"]
	images = [p.resolve() for p in src.glob("**/*") if p.suffix in extensions]
	header = False

	if not images:
		print(f"No image found in {src}")
		return

	# Get the first file starting with the text
	file = glob(f"{text}*.mp4")[0]

	# Get the file name without extension
	destination = Path(Path(file).stem)

	# Create the destination if not exists
	destination.mkdir(parents=True, exist_ok=True)

	for image in images:
		if move(image, destination):
			if not header:
				print(f"Destination: {destination.resolve()}")
				header = True
			print(f"Moved {image}")
	print("Task successfully completed!")


if __name__ == "__main__":
	if len(argv) < 2:
		print("Please pass at least one argument.")
		exit(1)

	# Run main with the argument.
	main(argv[1])

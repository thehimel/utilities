#!/usr/bin/env python3.9

"""
A script to copy all the images from one directory to a directory
matching the file name that starts with the given text.

Usages:
python3 c.py text
python3 c.py 1
./c.py 1
~/s/c.py 1
"""

from re import match
from glob import glob
from pathlib import Path
from shutil import move
from sys import argv, exit as sys_exit


def secure_eval(expression):
    """
    Securing eval() by not allowing any named expression to be executed.

    Arguments:
            expression(str): Expression to evaluate.
    """

    code = compile(expression, "<string>", "eval")
    if code.co_names:
        raise NameError("Names cannot be used.")
    return eval(code, {"__builtins__": {}}, {})  # pylint: disable=W0123


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

    # Evaluate the string if it's an equation
    if match(r"(\d+[+\-*\\/^%])*(\d+)", text):
        text = secure_eval(text)

    ext = "mp4"
    files = glob(f"{text}*.{ext}")

    if files:
        # Get the first file starting with the text
        file = files[0]
    else:
        print(f"No {ext} file found starting with '{text}' in {Path().resolve()}")
        return

    # Get the file name without extension
    destination = Path(Path(file).stem)

    if destination.is_dir():
        valid = False
        pos, neg = "y", "n"
        while not valid:
            ans = input(
                f"Directory already exists: {destination.resolve()}\n"
                f"Would you like to Proceed? [{pos}/{neg}]: "
            ).lower()
            if ans in [pos, neg]:
                valid = True
                if ans == neg:
                    return
            else:
                print("Invalid input.", end=" ")

    # Create the destination if not exists
    destination.mkdir(parents=True, exist_ok=True)

    for image in images:
        # TODO: Handle move if image already exists in destination.
        if move(image, destination):
            if not header:
                print(f"Destination: {destination.resolve()}")
                header = True
            print(f"Moved {image}")
    print("Task successfully completed!")


if __name__ == "__main__":
    if len(argv) < 2:
        print("Please pass at least one argument.")
        sys_exit(1)

    # Run main with the argument.
    main(argv[1])

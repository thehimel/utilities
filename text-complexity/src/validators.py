"""
Validators for the command line arguments.
"""

from pathlib import Path
from argparse import ArgumentTypeError


def valid_dir(directory: str) -> str:
    """
    Check if a directory exists.

    :param directory: Path to the directory.
    :return: Returns a date or raises error.
    """
    if Path(directory).is_dir():
        return directory

    msg = f"Directory does not exist: {directory}"
    raise ArgumentTypeError(msg)

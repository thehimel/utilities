"""
Analyze the complexity of texts.
"""


from argparse import ArgumentParser
from validators import valid_dir
from analysis import analyze


if __name__ == "__main__":
    parser = ArgumentParser(description="Analyze the complexity of texts.")
    parser.add_argument(
        "-i",
        "--input_directory",
        type=valid_dir,
        default=".",
        help="Path to the input directory. Default = Current Directory.",
        required=False,
    )
    parser.add_argument(
        "-o",
        "--output_directory",
        type=valid_dir,
        default="output",
        help="Path to the output directory. Default = Current Directory/output.",
        required=False,
    )
    args = parser.parse_args()
    analyze(input_directory=args.input_directory, output_directory=args.output_directory)

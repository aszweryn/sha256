import argparse
import sys
from sha256 import sha256


def parse_args(arguments: list) -> argparse.Namespace:
    parser = argparse.ArgumentParser("sha256_cli")
    parser.add_argument(
        "input_string",
        help="The input message or file path to be hashed.",
    )
    parser.add_argument(
        "--output_file", "-o", help="Specify the output file to write the hash result."
    )
    parser.add_argument(
        "--file",
        "-f",
        action="store_true",
        help="If provided, treat the input string as a file path",
    )
    return parser.parse_args(arguments)


def hash_and_print(inp: str, output_file=None):
    hashed = sha256.hash(inp)
    if output_file:
        with open(output_file, "w") as file:
            file.write(hashed)
        print(f"Hash result has been written to {output_file}")
    else:
        print(hashed)


def hash_from_file(input_filepath: str, output_file: str):
    try:
        with open(input_filepath, "r") as file:
            input_content = file.read().strip()
            hash_and_print(input_content, output_file)
    except FileNotFoundError:
        raise FileNotFoundError(
            f"File with input string not found - {input_filepath}"
        )


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    if args.file:
        hash_from_file(args.input_string, args.output_file)
    else:
        hash_and_print(args.input_string, args.output_file)

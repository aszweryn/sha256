import argparse
from sha256 import sha256


def hash_and_print(input_string, output_file=None):
    hashed = sha256.hash(input_string)

    if output_file:
        with open(output_file, "w") as file:
            file.write(hashed)
        print(f"Hash result has been written to {output_file}")
    else:
        print(hashed)


if __name__ == "__main__":
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
    args = parser.parse_args()

    if args.file:
        try:
            with open(args.input_string, "r") as file:
                input_content = file.read().strip()
                hash_and_print(input_content, args.output_file)
        except FileNotFoundError:
            print(f"Error: File not found - {args.input_string}")
    else:
        hash_and_print(args.input_string, args.output_file)

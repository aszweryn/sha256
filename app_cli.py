import argparse
from sha256 import sha256

parser = argparse.ArgumentParser("cli_sha256_hash")
parser.add_argument(
    "input_string",
    help="A string will be hashed using sha256 function and printed at the output.",
)
args = parser.parse_args()

hashed = sha256.hash(args.input_string)
print(hashed)

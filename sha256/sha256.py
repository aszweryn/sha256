from sha256 import const
from sha256.const import MAX_32
from sha256.opr import *


def main_loop(c, hash):
    """Implemented main loop acording to the NIST documentation.

    Args:
        c: _512-bit data block_
        hash: _current hash state_
    """
    w = [0] * 64  # generate a variable for storing an array of 64 words
    w[0:16] = [
        int.from_bytes(c[i : i + 4], "big") for i in range(0, len(c), 4)
    ]  # replace first 16 words with integers obtained from block 'c'

    # generate additional words
    for i in range(16, 64):
        sig0 = sigma_zero(w[i - 15])
        sig1 = sigma_one(w[i - 2])
        w[i] = (w[i - 16] + sig0 + w[i - 7] + sig1) & MAX_32

    # initialize variables specified in NIST documentation
    a, b, c, d, e, f, g, h = hash

    # main loop
    for i in range(64):
        # calculating temporary variables
        sum0 = sum_zero(a)
        t2 = sum0 + maj(a, b, c)
        sum1 = sum_one(e)
        t1 = (
            h + sum1 + ch(e, f, g) + const.K[i] + w[i]
        )  # using value of a specific hash here

        # reassigning values
        h = g
        g = f
        f = e
        e = (d + t1) & MAX_32
        d = c
        c = b
        b = a
        a = (t1 + t2) & MAX_32

    # updating the values after the computation
    for i, (x, y) in enumerate(zip(hash, [a, b, c, d, e, f, g, h])):
        hash[i] = (x + y) & MAX_32


def hash(inp: str) -> str:
    """Main function used to hash given string with SHA-256 cryptographic algorithm.

    Args:
        inp (str): Input string to be hashed.

    Returns:
        str: Hashed version of the input string.
    """

    # todo: main loop goes here

    return "todo"

from sha256 import const
from sha256.const import MAX_32
from sha256.opr import rotr, ch, maj


def is_palindrome(test_param: str) -> bool:
    return True


def print_constants():
    print(const.INIT_HASH)
    print(const.K)


def hash(inp: str) -> str:
    """Main function used to hash given string with SHA-256 cryptographic algorithm.

    Args:
        inp (str): Input string to be hashed.

    Returns:
        str: Hashed version of the input string.
    """

    # todo: main loop goes here

    return "todo"


def mainLoop(c, hash):
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
        s0 = rotr(w[i - 15], 7, MAX_32) ^ rotr(w[i - 15], 18, MAX_32) ^ (w[i - 15] >> 3)
        s1 = rotr(w[i - 2], 17, MAX_32) ^ rotr(w[i - 2], 19, MAX_32) ^ (w[i - 2] >> 10)
        w[i] = (w[i - 16] + s0 + w[i - 7] + s1) & MAX_32

    # initialize variables specified in NIST documentation
    a, b, c, d, e, f, g, h = hash

    # main loop
    for i in range(64):
        # calculating temporary variables
        s0 = rotr(a, 2, MAX_32) ^ rotr(a, 13, MAX_32) ^ rotr(a, 22, MAX_32)
        t2 = s0 + maj(a, b, c)
        s1 = rotr(e, 6, MAX_32) ^ rotr(e, 11, MAX_32) ^ rotr(e, 25, MAX_32)
        t1 = (
            h + s1 + ch(e, f, g) + const.K[i] + w[i]
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

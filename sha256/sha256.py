from sha256.const import K, INIT_HASH, MAX_32
from sha256.opr import *
from sha256.preprocessing import padding


def main_loop(c: list, hash: list):
    """Implemented main loop according to the NIST documentation.

    Args:
        c (list): 512-bit data block
        hash (list): Current hash state
    """
    w = [0] * 64
    w[0:16] = [int.from_bytes(c[i : i + 4], "big") for i in range(0, len(c), 4)]

    for i in range(16, 64):
        sig0 = sigma_zero(w[i - 15])
        sig1 = sigma_one(w[i - 2])
        w[i] = (w[i - 16] + sig0 + w[i - 7] + sig1) & MAX_32

    a, b, c, d, e, f, g, h = hash

    for i in range(64):
        sum0 = sum_zero(a)
        t2 = sum0 + maj(a, b, c)
        sum1 = sum_one(e)
        t1 = h + sum1 + ch(e, f, g) + K[i] + w[i]

        h = g
        g = f
        f = e
        e = (d + t1) & MAX_32
        d = c
        c = b
        b = a
        a = (t1 + t2) & MAX_32

    for i, (x, y) in enumerate(zip(hash, [a, b, c, d, e, f, g, h])):
        hash[i] = (x + y) & MAX_32


def update(m: bytes, mlen: int, buf: bytes, hash: list):
    """Update hash state with input message.

    Args:
        m (bytes): Input message
        mlen (int): Message length
        buf (bytes): Buffer for partial block
        hash (list): Current hash state

    Returns:
        tuple: Updated message length and buffer
    """
    if m is None or len(m) == 0:
        return mlen, buf

    mlen += len(m)
    m = buf + m

    # 64*8 = 512, how many full 64 byte blocks in message
    for i in range(0, len(m) // 64):
        main_loop(m[64 * i : 64 * (i + 1)], hash)

    buf = m[len(m) - (len(m) % 64) :]

    return mlen, buf


def digest(mlen: int, buf: bytes, hash: list):
    """Get the hash digest.

    Args:
        mlen (int): Message length
        buf (bytes): Buffer for partial block
        hash (list): Current hash state

    Returns:
        bytes: Hash digest
    """
    mlen, buf = update(padding(mlen), mlen, buf, hash)
    return b"".join(x.to_bytes(4, "big") for x in hash[:8])


def hex(mlen: int, buf: bytes, hash: list):
    """Get the hex representation of the hash digest.

    Args:
        mlen (int): Message length
        buf (bytes): Buffer for partial block
        hash (list): Current hash state

    Returns:
        str: Hex representation of the hash digest
    """
    tab = "0123456789abcdef"
    return "".join(tab[b >> 4] + tab[b & 0xF] for b in digest(mlen, buf, hash))


def hash(inp: str) -> str:
    """Main function used to hash given string with SHA-256 cryptographic algorithm.

    Args:
        inp (str): Input string to be hashed.

    Returns:
        str: Hashed version of the input string (in hexadecimal string representation).
    """
    # Initialize the variables
    mlen = 0
    buf = b""
    init_hash = INIT_HASH.copy()

    # Update hash state
    mlen, buf = update(inp.encode("utf-8"), mlen, buf, init_hash)

    # Compute SHA-256 hash
    result = hex(mlen, buf, init_hash)

    return result

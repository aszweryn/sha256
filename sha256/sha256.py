from .const import K, INIT_HASH, MAX_32
from .opr import *


def padding(mlen: int) -> bytes:
    """Generate padding for SHA-256.

    Ensures that the input message length is correct before applying the hash algorithm.

    Args:
        mlen (int): Message length.

    Returns:
        bytes: Padding for SHA-256.
    """
    mdi = mlen & 0x3F
    length = (mlen << 3).to_bytes(8, "big")
    padlength = 55 - mdi if mdi < 56 else 119 - mdi
    return b"\x80" + b"\x00" * padlength + length


def process(c: list, hash: list):
    """Implement the main loop according to the NIST documentation.

    Args:
        c (list): 512-bit data block.
        hash (list): Current hash state.
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


def update(m: bytes, mlen: int, buf: bytes, hash: list) -> tuple:
    """Update the hash state with the input message.

    Args:
        m (bytes): Input message.
        mlen (int): Message length.
        buf (bytes): Buffer for a partial block.
        hash (list): Current hash state.

    Returns:
        tuple: Updated message length and buffer.
    """
    if m is None or len(m) == 0:
        return mlen, buf

    mlen += len(m)
    m = buf + m

    # Process full 64-byte (512-bit) blocks in the message
    for i in range(0, len(m) // 64):
        process(m[64 * i : 64 * (i + 1)], hash)

    buf = m[len(m) - (len(m) % 64) :]

    return mlen, buf


def digest(mlen: int, buf: bytes, hash: list) -> bytes:
    """Get the hash digest.

    Args:
        mlen (int): Message length.
        buf (bytes): Buffer for a partial block.
        hash (list): Current hash state.

    Returns:
        bytes: Hash digest.
    """
    mlen, buf = update(padding(mlen), mlen, buf, hash)
    return b"".join(x.to_bytes(4, "big") for x in hash[:8])


def hex(mlen: int, buf: bytes, hash: list) -> str:
    """Get the hexadecimal representation of the hash digest.

    Args:
        mlen (int): Message length.
        buf (bytes): Buffer for a partial block.
        hash (list): Current hash state.

    Returns:
        str: Hexadecimal representation of the hash digest.
    """
    tab = "0123456789abcdef"
    return "".join(tab[b >> 4] + tab[b & 0xF] for b in digest(mlen, buf, hash))


def hash(inp: str) -> str:
    """Hash a given string with the SHA-256 cryptographic algorithm.

    Args:
        inp (str): Input string to be hashed.

    Returns:
        str: Hashed version of the input string (in hexadecimal string representation).
    """
    mlen = 0
    buf = b""
    init_hash = INIT_HASH.copy()

    mlen, buf = update(inp.encode("utf-8"), mlen, buf, init_hash)

    result = hex(mlen, buf, init_hash)

    return result

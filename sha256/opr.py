# Here is a little cheatsheet of Python bitwise operators that we use in our project:
# ~a - NOT a
# a & b - a AND b
# a | b - a OR b
# a ^ b - a XOR b (symbol is like a plus inside a circle)
# a >> n - shift a right n times


# According to NIST SHA hashing functions documentation we need additional bitwise LOGICAL operators to define:
def rotr(a: int, n: int) -> int:
    """
    Bitwise rotate right bit word n times.
    * NOTE: Input and result should be treated as a 32bit word.
    """
    from sha256 import const

    return ((a >> n) | (a << (32 - n))) & const.MAX_32


def ch(a: int, b: int, c: int) -> int:
    """
    Bitwise ternary operator for (a AND b) XOR (NOT a AND c).
    * NOTE: Input and result should be treated as a 32bit word.
    """
    return (a & b) ^ (~a & c)


def maj(a: int, b: int, c: int) -> int:
    """
    Bitwise ternary operator for (a AND b) XOR (a AND c) XOR (b AND c).
    * NOTE: Input and result should be treated as a 32bit word.
    """
    return (a & b) ^ (a & c) ^ (b & c)

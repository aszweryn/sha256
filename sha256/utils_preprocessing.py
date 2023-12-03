def translate(message):
    """Translates strings into binary number returned as a list of integers"""
    chars = [ord(c) for c in message]  # ord translates string to Unicode value

    bytes = []
    for char in chars:
        bytes.append(bin(char)[2:].zfill(8))  # replacing '0b' indicator with 0

    # returning the value as the list of integers
    bitlist = []
    for byte in bytes:
        for bit in byte:
            bitlist.append(int(bit))
    return bitlist


def bin2Hex(val):
    """For presenting hash values in hexadecimal notation, takes a list of 32 bits as an input"""
    val = "".join([str(x) for x in val])

    bins = []
    for d in range(0, len(val), 4):
        bins.append("0b" + val[d : d + 4])  # converting the list back to '0bx' format

    hexes = ""
    for b in bins:
        hexes += hex(int(b, 2))[2:]
    return hexes


def zerosFill(bits, length=8, endian="LE"):
    """Useful for formatting data for usage with Python methods"""
    l = len(bits)

    if endian == "LE":
        for _ in range(l, length):
            bits.append(0)
    else:
        while l < length:
            bits.insert(0, 0)
            l = len(bits)
    return bits


def divider(bits, chunk_length=8):
    """Dividing the message into desired chunks"""
    chunked = []
    for b in range(0, len(bits), chunk_length):
        chunked.append(bits[b : b + chunk_length])
    return chunked


def initialize(values):
    """Initializing the algorithm and converting values into a list of bits"""
    bins = [bin(int(v, 16))[2:] for v in values]
    words = []
    for binary in bins:
        word = []
        for b in binary:
            word.append(int(b))
        words.append(zerosFill(word, 32, "BE"))
    return words
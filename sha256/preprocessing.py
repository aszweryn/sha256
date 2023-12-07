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


def bin2Int(val):
    """Converts a 32-bit list of binary values into a single 32-bit integer"""
    bin_String = "".join([str(x) for x in val])
    decimal = int(bin_String, 2)
    return decimal


def padding(mlen):
    """Generating the padding for the SHA-256.
    It ensures that the input message length is correct before applying the hash algorithm
    """
    mdi = (
        mlen & 0x3F
    )  # get the message digest index - used for determining the position of the last byte
    length = (mlen << 3).to_bytes(
        8, "big"
    )  # calculate the length of the original message
    padlength = (
        55 - mdi if mdi < 56 else 119 - mdi
    )  # use mdi to calculate required padding length
    return b"\x80" + b"\x00" * padlength + length  # construct and return the padding

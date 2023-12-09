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

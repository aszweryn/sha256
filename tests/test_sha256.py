import pytest
import hashlib
from sha256 import sha256

HASH_TEST = [
    "",
    " ",
    "i",
    "Hello, World!",
    "123456",
    "ECRYP CRYPT testing",
    "Hash Function Test",
    "python",
    "987654321",
    "abcdefghijklmnopqrstuvwxyz1234567890",
    "[" * (32600) # 32600 length input 
]


def get_ref_hashed(inp: str) -> str:
    """Wrapper for hashlib.sha256 object usage.

    Args:
        inp (str): Input string to be hashed.

    Returns:
        str: Hashed version of the input string.
    """
    hashing = hashlib.sha256()
    hashing.update(inp.encode("utf-8"))
    return hashing.hexdigest()


def get_hash_test_params(test_inputs: list) -> list:
    params = []
    for inp in test_inputs:
        # param = pair of input_string and expected_result
        param = (inp, get_ref_hashed(inp))
        print(param)
        params.append(param)
    return params


@pytest.mark.parametrize(
    "input_string, expected_result",
    get_hash_test_params(HASH_TEST),
)
def test_hash_with_sha256(input_string, expected_result):
    assert sha256.hash(input_string) == expected_result

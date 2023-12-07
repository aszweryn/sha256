import pytest
from sha256.utils_preprocessing import translate, bin2Hex, bin2Int, padding


def test_translate():
    assert translate("") == []
    assert translate("A") == [0, 1, 0, 0, 0, 0, 0, 1]
    assert translate("Hello") == [
        0, 1, 0, 1, 0, 0, 1, 0,
        0, 1, 1, 0, 0, 1, 0, 0,
        0, 1, 1, 0, 0, 1, 1, 1,
        0, 1, 1, 0, 1, 1, 1, 1,
        1, 0, 0, 1, 1, 0, 0, 1,
    ]


def test_bin2Hex():
    assert bin2Hex([0, 1, 0, 0, 0, 0, 0, 1]) == "21"
    assert bin2Hex([
        0, 1, 0, 1, 0, 0, 1, 0,
        0, 1, 1, 0, 0, 1, 0, 0,
        0, 1, 1, 0, 0, 1, 1, 1,
        0, 1, 1, 0, 1, 1, 1, 1,
        1, 0, 0, 1, 1, 0, 0, 1,
    ]) == "51487799"


def test_bin2Int():
    assert bin2Int([0, 1, 0, 0, 0, 0, 0, 1]) == 33
    assert bin2Int([
        0, 1, 0, 1, 0, 0, 1, 0,
        0, 1, 1, 0, 0, 1, 0, 0,
        0, 1, 1, 0, 0, 1, 1, 1,
        0, 1, 1, 0, 1, 1, 1, 1,
        1, 0, 0, 1, 1, 0, 0, 1,
    ]) == 1346525561


def test_padding():
    actual_output = padding(0)
    expected_prefix = b'\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    assert actual_output.startswith(expected_prefix)

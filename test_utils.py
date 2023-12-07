import pytest
from sha256.preprocessing import translate, bin2Hex, bin2Int, padding


def test_translate():
    result = translate("Hi")
    assert result == [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1]


def test_bin2Hex():
    result = bin2Hex([1, 0, 0, 0, 1, 0, 1])
    assert result == "45"


def test_bin2Int():
    result = bin2Int([1, 1, 0, 1])
    assert result == 13


def test_padding():
    result = padding(0)
    assert result == b"\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"

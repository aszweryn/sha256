import pytest
from sha256.opr import ch, maj, rotr


@pytest.mark.parametrize(
    "input_number, rotate_times, expected_result",
    [
        (0x00000010, 4, 0x00000001),
        (0x00000001, 4, 0x10000000),
        (0x000000F0, 4, 0x0000000F),
    ],
)
def test_rotr(input_number, rotate_times, expected_result):
    result = rotr(input_number, rotate_times)
    assert result == expected_result


@pytest.mark.parametrize(
    "a, b, c, expected_result",
    [
        (0, 0, 0, 0),
        (0, 0, 1, 1),
        (0, 1, 0, 0),
        (0, 1, 1, 1),
        (1, 0, 0, 0),
        (1, 0, 1, 0),
        (1, 1, 0, 1),
        (1, 1, 1, 1),
    ],
)
def test_ch(a, b, c, expected_result):
    result = ch(a, b, c)
    assert result == expected_result


@pytest.mark.parametrize(
    "a, b, c, expected_result",
    [
        (0, 0, 0, 0),
        (0, 0, 1, 0),
        (0, 1, 0, 0),
        (0, 1, 1, 1),
        (1, 0, 0, 0),
        (1, 0, 1, 1),
        (1, 1, 0, 1),
        (1, 1, 1, 1),
    ],
)
def test_maj(a, b, c, expected_result):
    result = maj(a, b, c)
    assert result == expected_result

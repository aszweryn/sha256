import pytest
from sha256 import sha256


@pytest.mark.parametrize(
    "maybe_palindrome, expected_result",
    [
        ("", True),
        ("a", True),
        ("Bob", True),
        ("Never odd or even", True),
        ("Do geese see God?", True),
        ("abc", False),
        ("abab", False),
    ],
)
def test_is_palindrome(maybe_palindrome, expected_result):
    assert sha256.is_palindrome(maybe_palindrome) == expected_result


def test_is_hash_todo():
    assert sha256.hash("testing") == "todo"

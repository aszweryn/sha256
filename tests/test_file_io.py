import pytest
import os, random, string
import app_cli


def random_str(length) -> str:
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def get_non_existent_path() -> (str,str):
    rand = random_str(10)
    rand_path = os.path.abspath(f"./{rand}.txt")
    while True:
        if os.path.exists(rand_path):
            rand = random_str(10)
            rand_path = os.path.abspath(f"./{rand}.txt")
        else:
            break
    return rand, rand_path


def test_file_not_found():
    filename, filepath = get_non_existent_path()
    wasFileNotFoundError = False
    try: 
        app_cli.hash_from_file(filepath, "test.txt")
    except FileNotFoundError:
        wasFileNotFoundError = True
    assert wasFileNotFoundError == True


def test_hash_from_file():
    pass

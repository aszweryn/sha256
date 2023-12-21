import os, random, string
from config import DIR_RESULTS, RESULTS_DIR_NAME
from app_cli import hash_from_file, hash_and_print
from sha256 import sha256


def random_str(length) -> str:
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def get_non_existent_path() -> (str, str):
    rand = random_str(10)
    rand_path = os.path.abspath(f"./{rand}.txt")
    while True:
        if os.path.exists(rand_path):
            rand = random_str(10)
            rand_path = os.path.abspath(f"./{rand}.txt")
        else:
            break
    return rand, rand_path


def check_file_contents(check_filepath, check_input) -> bool:
    with open(check_filepath, "r") as file:
        input_content = file.read().strip()
        return input_content == check_input


def test_file_not_found():
    filename, filepath = get_non_existent_path()
    was_file_not_found_err = False
    try:
        hash_from_file(filepath, "test.txt")
    except FileNotFoundError:
        was_file_not_found_err = True
    assert was_file_not_found_err == True


def test_hash_from_file():
    input_file = "test_input.txt"
    output_file = "test_output.txt"
    inp = "TestInputToBeHashed"
    hashed_hashed_inp = sha256.hash(sha256.hash(inp))
    hash_and_print(inp, input_file)
    expected_resultpath = os.path.join(DIR_RESULTS, output_file)
    if os.path.exists(expected_resultpath):
        os.remove(expected_resultpath)
    dir_input = os.path.join(RESULTS_DIR_NAME, input_file)
    hash_from_file(dir_input, output_file)
    was_file_found_and_hashed = os.path.exists(
        expected_resultpath
    ) and check_file_contents(expected_resultpath, hashed_hashed_inp)
    assert was_file_found_and_hashed == True

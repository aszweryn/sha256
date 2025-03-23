# SHA-256 project

Simple Python3 command line interface (CLI) tool for hashing strings with standard SHA-256 built from scratch. This project realized as a part of a Cryptography and Information Security course on WUT.

[Learn more about SHA-256 with our project report!](docs/ECRYP_PROJECT_23Z___SHA_256___M_PIOTROWSKI_A_SZWERYN.pdf)

## Installation (Windows)
```
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
```

## Running

CLI tool:
```
python app_cli.py --help
python app_cli.py textToBeHashed
```

Tests:
```
python -m pytest
```


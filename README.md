# get-papers-list

A Python program to fetch research papers based on a user-specified query.

## Installation

1. Install Poetry using `pip install poetry`.
2. Run `poetry install` to install dependencies.
3. Create a file named `api_key.txt` with your PubMed API key.

## Usage

1. Run `poetry run get-papers-list --help` to see usage instructions.
2. Run `poetry run get-papers-list <query> [-d] [-f <filename>]` to fetch papers.

## Dependencies

* `requests`
* `csv`

## Tools Used

* PubMed API
* Poetry for dependency management
* LLM tools for development assistance

## Notes

* This program uses heuristics to identify non-academic authors and company affiliations.
* The program assumes that the PubMed API key is stored in a file named `api_key.txt`.

```markdown
# 📘 Assignment: Python Text Processing

## 🎯 Objective

Practice string handling, file I/O, parsing, and basic text analysis in Python by building small utilities that read text files and produce summary reports.

## 📝 Tasks

### 🛠️  Basic String Utilities

#### Description
Implement a set of utility functions for working with strings: cleaning/normalizing text, counting words, and finding the most common words.

#### Requirements
Completed program should:

- Provide a `normalize_text(text: str) -> str` function that lowercases text and removes punctuation.
- Provide a `word_count(text: str) -> int` function that returns the number of words.
- Provide a `most_common_words(text: str, n: int) -> list[tuple[str,int]]` function that returns the top `n` words and counts.


### 🛠️  File I/O and Report

#### Description
Write a script that reads a text file, uses the utilities above to analyze it, and prints a short report to the console.

#### Requirements
Completed program should:

- Accept a filename as a command-line argument or prompt the user when none is provided.
- Read the file contents robustly (handle missing file with a friendly error message).
- Print a report including: total characters, total words, unique words, and top 5 most common words with counts.
- Include docstrings and simple inline usage instructions or `--help` output.

## Submission

- Add your finished script `analysis.py` (or reuse `starter-code.py`) to the assignment folder and commit your changes.
- Include a short paragraph (2-3 sentences) describing what you learned.

## Extensions (optional)

- Make the report output JSON when passed a `--json` flag.
- Support processing multiple files and aggregating results.

```

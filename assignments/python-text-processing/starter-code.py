"""Starter code for the Python Text Processing assignment.

Usage:
    python starter-code.py path/to/file.txt

This file contains helper functions to get you started. Fill in the TODOs.
"""
from collections import Counter
import sys
import string


def normalize_text(text: str) -> str:
    """Lowercase and remove punctuation from text."""
    # TODO: handle more sophisticated normalization if desired
    translator = str.maketrans('', '', string.punctuation)
    return text.lower().translate(translator)


def word_count(text: str) -> int:
    """Return number of words in text."""
    words = normalize_text(text).split()
    return len(words)


def most_common_words(text: str, n: int = 5):
    """Return top `n` most common words with counts as list of (word, count)."""
    words = normalize_text(text).split()
    counter = Counter(words)
    return counter.most_common(n)


def analyze_text(text: str) -> dict:
    """Return a summary dict for the given text."""
    total_chars = len(text)
    total_words = word_count(text)
    words = normalize_text(text).split()
    unique_words = len(set(words))
    top5 = most_common_words(text, 5)
    return {
        "total_characters": total_chars,
        "total_words": total_words,
        "unique_words": unique_words,
        "top5": top5,
    }


def read_file(path: str) -> str:
    """Read file and return text; raises FileNotFoundError on missing file."""
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def main(argv=None):
    argv = argv or sys.argv[1:]
    if not argv:
        print("Usage: python starter-code.py path/to/file.txt")
        return 1
    path = argv[0]
    try:
        text = read_file(path)
    except FileNotFoundError:
        print(f"File not found: {path}")
        return 2

    summary = analyze_text(text)
    print("Text Analysis Report")
    print("--------------------")
    print(f"Characters: {summary['total_characters']}")
    print(f"Words: {summary['total_words']}")
    print(f"Unique words: {summary['unique_words']}")
    print("Top 5 words:")
    for w, c in summary['top5']:
        print(f"  {w}: {c}")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

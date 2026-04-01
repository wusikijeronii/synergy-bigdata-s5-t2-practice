#!/usr/bin/env python3

import argparse
import re
from pathlib import Path

WORD_RE = re.compile(r"\b\w+\b", re.UNICODE)
CHAPTER_RE = re.compile(r"^\s*(chapter|глава)\b", re.IGNORECASE)

def analyze_book(file_path: Path):
    text = file_path.read_text(encoding="utf-8")

    lines = text.splitlines()
    paragraphs = [p for p in text.split("\n\n") if p.strip()]
    words = WORD_RE.findall(text)
    chapters = sum(1 for line in lines if CHAPTER_RE.match(line))

    line_count = len(lines)
    words_count = len(words)
    paragraphs_count = len(paragraphs)

    avg_word_length = (
        sum(len(word) for word in words) / words_count if words_count > 0 else 0
    )

    if avg_word_length < 5:
        reading_level = "Easy"
    elif avg_word_length < 7:
        reading_level = "Medium"
    else:
        reading_level = "Hard"

    popularity_score = words_count + chapters * 100 + paragraphs_count * 10

    return {
        "lines": line_count,
        "words": words_count,
        "paragraphs": paragraphs_count,
        "chapters": chapters,
        "avg_word_length": avg_word_length,
        "reading_level": reading_level,
        "popularity_score": popularity_score,
    }

def main():
    parser = argparse.ArgumentParser(description="Book analysis")
    parser.add_argument("input_file", help="Path to book text file")
    args = parser.parse_args()

    stats = analyze_book(Path(args.input_file))

    print("Book analysis:")
    print(f"Lines: {stats['lines']}")
    print(f"Words: {stats['words']}")
    print(f"Paragraphs: {stats['paragraphs']}")
    print(f"Chapters: {stats['chapters']}")
    print(f"Average word length: {stats['avg_word_length']:.2f}")
    print(f"Reading level: {stats['reading_level']}")
    print(f"Popularity score: {stats['popularity_score']}")


if __name__ == "__main__":
    main()
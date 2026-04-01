#!/usr/bin/env python3

import argparse
import re
from collections import Counter
from pathlib import Path

# Common log format parser
LOG_PATTERN = re.compile(
    r'^\S+ \S+ \S+ \[[^\]]+\] "(?:\S+) (?P<path>\S+)(?: \S+)?" (?P<status>\d{3})'
)


def parse_log_file(file_path: Path):
    page_counter = Counter()
    error_counter = Counter()

    with file_path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            match = LOG_PATTERN.match(line)
            if not match:
                continue

            path = match.group("path")
            status = int(match.group("status"))

            page_counter[path] += 1

            if status >= 400:
                error_counter[status] += 1

    return page_counter, error_counter


def main():
    parser = argparse.ArgumentParser(description="Server log analysis")
    parser.add_argument("input_file", help="Path to log file")
    parser.add_argument("--top", type=int, default=10, help="Top pages to display")

    args = parser.parse_args()
    log_path = Path(args.input_file)

    pages, errors = parse_log_file(log_path)

    print("Most requested pages:")
    for i, (page, count) in enumerate(pages.most_common(args.top), start=1):
        print(f"{i}. {page} — {count}")

    print("\nErrors:")
    if not errors:
        print("No errors found.")
    else:
        for code, count in errors.most_common():
            print(f"{code} — {count}")


if __name__ == "__main__":
    main()
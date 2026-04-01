#!/usr/bin/env python3

import argparse
import json
import re
from collections import Counter
from pathlib import Path

HASHTAG_RE = re.compile(r"(?<!\w)#([A-Za-zА-Яа-яЁё0-9_]+)", re.UNICODE)

def load_posts(path: Path) -> list[str]:
    if path.suffix.lower() == ".json":
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)

        posts = []
        for item in data:
            if isinstance(item, str):
                posts.append(item)
            elif isinstance(item, dict) and "text" in item:
                posts.append(str(item["text"]))
        return posts

    if path.suffix.lower() == ".txt":
        with path.open("r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]

    raise ValueError("Only .json and .txt files are supported")


def extract_hashtags(posts: list[str]) -> Counter:
    tags = []
    for post in posts:
        tags.extend(tag.lower() for tag in HASHTAG_RE.findall(post))
    return Counter(tags)


def main():
    parser = argparse.ArgumentParser(description="Hashtag analysis")
    parser.add_argument("input_file", help="Input file")
    parser.add_argument("--top", type=int, default=10, help="Number of top hashtags")
    args = parser.parse_args()

    posts = load_posts(Path(args.input_file))
    stats = extract_hashtags(posts)

    print("Top hashtags:")
    for i, (tag, count) in enumerate(stats.most_common(args.top), start=1):
        print(f"{i}. #{tag} — {count}")


if __name__ == "__main__":
    main()
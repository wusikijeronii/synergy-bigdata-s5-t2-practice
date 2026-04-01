#!/usr/bin/env python3

import argparse
import csv
from collections import Counter
from pathlib import Path

def load_documents(file_path: Path):
    documents = []

    with file_path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            documents.append(
                {
                    "document_id": row["document_id"],
                    "document_type": row["document_type"],
                    "subject": row["subject"],
                    "sender": row["sender"],
                    "recipient": row["recipient"],
                    "direction": row["direction"],
                    "status": row["status"],
                    "date": row["date"],
                }
            )

    return documents


def print_documents(documents):
    print("Documents:")
    for doc in documents:
        print(
            f"- ID: {doc['document_id']}, "
            f"Type: {doc['document_type']}, "
            f"Subject: {doc['subject']}, "
            f"Sender: {doc['sender']}, "
            f"Recipient: {doc['recipient']}, "
            f"Direction: {doc['direction']}, "
            f"Status: {doc['status']}, "
            f"Date: {doc['date']}"
        )


def print_statistics(documents):
    direction_stats = Counter(doc["direction"] for doc in documents)
    status_stats = Counter(doc["status"] for doc in documents)

    print("\nStatistics by direction:")
    for direction, count in direction_stats.items():
        print(f"- {direction}: {count}")

    print("\nStatistics by status:")
    for status, count in status_stats.items():
        print(f"- {status}: {count}")


def main():
    parser = argparse.ArgumentParser(description="Document management system")
    parser.add_argument("input_file", help="Path to CSV file")
    args = parser.parse_args()

    documents = load_documents(Path(args.input_file))

    print_documents(documents)
    print_statistics(documents)


if __name__ == "__main__":
    main()
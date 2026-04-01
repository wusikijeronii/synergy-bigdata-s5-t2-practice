#!/usr/bin/env python3

import argparse
import csv
from collections import defaultdict
from pathlib import Path


def load_expenses(file_path: Path):
    expenses = []
    with file_path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            expenses.append({
                "category": row["category"],
                "amount": float(row["amount"]),
                "budget": float(row["budget"]),
            })
    return expenses


def analyze_expenses(expenses):
    stats = defaultdict(lambda: {"amount": 0.0, "budget": 0.0})

    for item in expenses:
        category = item["category"]
        stats[category]["amount"] += item["amount"]
        stats[category]["budget"] = item["budget"]

    total_amount = sum(item["amount"] for item in expenses)
    total_budget = sum(data["budget"] for data in stats.values())

    return stats, total_amount, total_budget


def main():
    parser = argparse.ArgumentParser(description="Office expense analysis")
    parser.add_argument("input_file", help="Path to CSV file")
    args = parser.parse_args()

    expenses = load_expenses(Path(args.input_file))
    stats, total_amount, total_budget = analyze_expenses(expenses)

    print("Office expense statistics:")
    for category, data in stats.items():
        difference = data["budget"] - data["amount"]
        status = "within budget" if difference >= 0 else "over budget"

        print(
            f"- {category}: spent={data['amount']:.2f}, "
            f"budget={data['budget']:.2f}, "
            f"status={status}"
        )

    print("\nTotal:")
    print(f"Spent: {total_amount:.2f}")
    print(f"Budget: {total_budget:.2f}")

    if total_amount <= total_budget:
        print("Overall status: within budget")
    else:
        print("Overall status: over budget")


if __name__ == "__main__":
    main()
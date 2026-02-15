#!/usr/bin/env python3
"""Reads cards.csv and embeds the card data into index.html."""

import csv
import json
import re
import sys

CSV_FILE = "cards.csv"
HTML_FILE = "index.html"

def main():
    # Read cards from CSV
    cards = []
    with open(CSV_FILE, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            title = row["Title"].strip()
            if not title:
                continue
            cards.append({
                "title": title,
                "description": row["Description"].strip(),
                "points": int(row["Points"]),
                "language": row["Language"].strip().lower(),
            })

    if not cards:
        print("No cards found in", CSV_FILE)
        sys.exit(1)

    # Build JS array literal
    lines = []
    for c in cards:
        lines.append(
            f'  {{title:{json.dumps(c["title"])},'
            f'description:{json.dumps(c["description"])},'
            f'points:{c["points"]},'
            f'language:{json.dumps(c["language"])}}}'
        )
    js_array = "const allCards = [\n" + ",\n".join(lines) + "\n];"

    # Replace in HTML
    with open(HTML_FILE, encoding="utf-8") as f:
        html = f.read()

    pattern = r"const allCards = \[.*?\];"
    match = re.search(pattern, html, re.DOTALL)
    if not match:
        print("Could not find allCards array in", HTML_FILE)
        sys.exit(1)
    html = html[:match.start()] + js_array + html[match.end():]

    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Imported {len(cards)} cards from {CSV_FILE} into {HTML_FILE}")

if __name__ == "__main__":
    main()

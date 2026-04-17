#!/usr/bin/env python3
"""Assemble chapter files + shared templates into index.html."""

from pathlib import Path

ROOT = Path(__file__).parent
SHARED = ROOT / "shared"
CHAPTERS = ROOT / "chapters"
OUTPUT = ROOT / "index.html"

# Read shared templates
head = (SHARED / "head.html").read_text(encoding="utf-8")
footer = (SHARED / "footer.html").read_text(encoding="utf-8")

# Read manifest (build order)
manifest = (CHAPTERS / "manifest.txt").read_text(encoding="utf-8").strip().splitlines()

# Assemble
parts = [head]
for filename in manifest:
    filepath = CHAPTERS / filename.strip()
    if not filepath.exists():
        print(f"WARNING: {filepath} not found, skipping")
        continue
    parts.append(filepath.read_text(encoding="utf-8"))

parts.append(footer)

# Write output
output = "".join(parts)
OUTPUT.write_text(output, encoding="utf-8")

print(f"Built {OUTPUT} ({len(output)} bytes, {output.count(chr(10))} lines)")
